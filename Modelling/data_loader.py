import os
import glob
import numpy as np
from PIL import Image
from tensorflow.keras.utils import Sequence


class DataLoader(Sequence):
    def __init__(self, batch_size, data_x_path):
        self.batch_size = batch_size;
        self.list_files_x = glob.glob(os.path.join(data_x_path, '*.npy'))
        #self.list_files_y = glob.glob(os.path.join(data_y_path, '*.npy'))
        self.labels = {'attack' : 0, 'real' : 1}
        self.indices = np.random.permutation(len(self.list_files_x))


    def __len__(self):
        return int(len(self.list_files_x)/(self.batch_size+3))  # 4500/ 4


    def __getitem__(self, idx): 
        list_subvideos = []
        list_labels = []

        list_files_x = self.list_files_x
        #list_files_y = self.list_files_y

        list_files_x.sort()
       # list_files_y.sort()

        for idx_item in range(self.batch_size):
            idx_indices = idx * self.batch_size + idx_item
            idx_list_filenames = self.indices[idx_indices]
            filename_x = list_files_x[idx_list_filenames]
            #filename_y = list_files_y[idx_list_filenames]

            np_image = np.load(filename_x)
            list_subvideos.append(np_image) 
            label = [self.labels[str(filename_x.split('_')[-1].split('.')[-2])]]
            list_labels.append(label)

        return np.array(list_subvideos), np.array(list_labels)
                   

    def on_epoch_end(self):
      self.indices = np.random.permutation(len(self.list_files_x))