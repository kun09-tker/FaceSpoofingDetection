import random
import numpy as np
from keras import backend as K
from tensorflow.keras.callbacks import Callback
from sklearn.metrics import f1_score, recall_score, precision_score
from data_loader import DataLoader

class Metrics(Callback):
    def __init__(self):
        super(Callback, self).__init__()
        self.validation_data = DataLoader(1,'/content/ReplayAttackSample/valid')

    def on_train_begin(self, logs={}):
        self.val_f1s = []
        self.val_recalls = []
        self.val_precisions = []

    def on_epoch_end(self, epoch, logs={}):
      #pick randomly 100 files in Validation data to evaluate model to avoid OOM
      val_predicts = []
      val_targets = []
      idx_sample = random.sample(range(len(self.validation_data)), 50)
      for idx in idx_sample:
        val_sub_video, val_label = self.validation_data[idx]  #240,320,3,10; ,1
        val_predicts.append(np.argmax(self.model.predict(val_sub_video), axis = 1)[0])
        val_targets.append(val_label[0])
        # print(val_label[0])
        # print(np.argmax(self.model.predict(val_sub_video), axis = 1)[0].astype(float))

      # print(np.unique(np.array(val_predicts)))
      # print(np.unique(np.array(val_targets)))

      _val_f1 = f1_score(val_targets, val_predicts, zero_division = 1)
      _val_recall = recall_score(val_targets, val_predicts, zero_division = 1)
      _val_precision = precision_score(val_targets, val_predicts, zero_division = 1)

      self.val_f1s.append(_val_f1)
      self.val_recalls.append(_val_recall)
      self.val_precisions.append(_val_precision)
      print (' — val_f1: ',_val_f1,' — val_precision: ',_val_precision, ' — val_recall: ',_val_recall)