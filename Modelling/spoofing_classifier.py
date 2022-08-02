import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Input, ConvLSTM2D, Conv2D, MaxPool3D, GlobalAveragePooling3D, Dense, Dropout, BatchNormalization, Concatenate
from tensorflow.keras.models import Model, load_model, save_model
from tensorflow.keras.optimizers import Adam    
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.callbacks import EarlyStopping,ModelCheckpoint
from data_loader import DataLoader
from keras import backend as K
from metrics_f1 import Metrics


class SpoofingClassifier:
    def __init__(self):
        self.model = None
        #self.labels = {0 : 0, 1 : 1}
        #self.label_map = {l:idx for idx, l in enumerate(self.labels)}
        
    def save_model(self):
        save_model(self.model, 'models/anti_spoofing_training-11-04_best.h5')
       
    def build_model(self):
        #input: video has 5 shapes ([number of samples, width, height, depth, length])
        input_layer = Input(shape = [240, 320, 3, 10])

        lstm_layer_1 = ConvLSTM2D(filters = 512, kernel_size = 1, padding = 'valid', return_sequences = True)(input_layer)
        
        # # # # Block 1
        conv_layer_1 = Conv2D(filters = 256, kernel_size = 1, padding = 'valid', activation = 'relu')(lstm_layer_1)
        batch_layer_1 = BatchNormalization()(conv_layer_1)
        maxpool_layer_1 = MaxPool3D(pool_size=(3, 3, 1), padding = 'valid')(batch_layer_1)   

        # # # # #Block 2
        conv_layer_2 = Conv2D(filters = 128, kernel_size = 2, padding = 'valid', activation = 'relu')(maxpool_layer_1)
        batch_layer_2 = BatchNormalization()(conv_layer_2)
        maxpool_layer_2  = MaxPool3D(pool_size=(3, 3, 1), padding = 'valid')(batch_layer_2)  
        
        # # # # #Block 3
        conv_layer_3 = Conv2D(filters = 64, kernel_size = 1, padding = 'valid', activation = 'relu')(maxpool_layer_2)
        batch_layer_3 = BatchNormalization()(conv_layer_3)
        maxpool_layer_3 = MaxPool3D(pool_size=(3, 3, 1), padding = 'valid')(batch_layer_3)   

        lstm_layer_2 = ConvLSTM2D(filters = 32, kernel_size = 1, padding = 'same', return_sequences = True)(maxpool_layer_3) 
        drop_layer = Dropout(0.2)(lstm_layer_2)
        lstm_layer_3 = ConvLSTM2D(filters = 16, kernel_size = 1, padding = 'same', return_sequences = True)(drop_layer)        

        gap_layer_1 = GlobalAveragePooling3D()(lstm_layer_3)
        
        dense_layer = Dense(8, activation='softmax')(gap_layer_1)
        output_layer = Dense(2, activation = 'softmax')(dense_layer)
        
        model = Model(input_layer, output_layer)
        optimizer = Adam(learning_rate = 0.0001)
        loss = BinaryCrossentropy() 

        model.compile(loss = loss, optimizer = optimizer)   
        model.summary()
        self.model = model


    def load_model (self):
        #self.model = load_model('models/anti_spoofing_1_test.h5')
        self.model = load_model('models/anti_spoofing_training-11-04_best.h5')

        
    ### Put specific location of x_train, y_train for each train/valid path
    ### Ex: model.train('content/RAS/train/x_train', 'content/RAS/train/y_train', 'content/RAS/valid/x_valid', 'content/RAS/valid/y_valid',)
    def train(self, train_path, valid_path):#, y_valid_path):            
        BS = 1
        train_loader = DataLoader(BS, train_path)
        valid_loader = DataLoader(BS, valid_path)

        e_callbacks = EarlyStopping(verbose=1, patience=4, mode='min')
        ckpt_model = ModelCheckpoint('models/best_model_test_24-04.h5', verbose=1, save_best_only=True, monitor='val_loss', mode='min')
        ckpt_weight = ModelCheckpoint('models/best_model_weight_24-04.h5', verbose=1, save_best_only=True, save_weights_only=True, monitor='val_loss', mode='min')
        self.model.fit( 
                        train_loader, 
                        validation_data = valid_loader, 
                        epochs = 25, 
                        #steps_per_epoch = 1000,  
                        callbacks = [                  
                                      e_callbacks,
                                      ckpt_model, 
                                      ckpt_weight,
                                      Metrics()
                                    ]
                       )

    def predict(self, file_npy):
        np_test = np.array([np.load(file_npy)])
        #print(np_test.shape)
        y_prob = self.model.predict(np_test)
        y_predict = np.argmax(y_prob, axis = 1)
        return y_predict[0]