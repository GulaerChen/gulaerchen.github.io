# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 12:39:48 2022

@author: Gulae
"""

import pickle
import os
import numpy as np
from tqdm import tqdm

def get_diff_pitch_trend(path, folder, file):
    
    # read the pitch data extract from crepe
    # Github: https://github.com/marl/crepe
    with open( path + folder + file, 'rb') as f:
        pitch_data = pickle.load(f)
      
    vocA_pitch = pitch_data['vocA_pitch'].numpy()
    vocB_pitch = pitch_data['vocB_pitch'].numpy()
    
    diff_vocA = np.diff(vocA_pitch)
    diff_vocB = np.diff(vocB_pitch)
    
    # set a high a penalty value if all pitches in a channel are zero
    if max(vocA_pitch[0]) == 0 or max(vocB_pitch[0]) == 0:
        return 999999
    
    diff_AB = []
    
    for i in range(len(vocA_pitch[0])-2):
        if  vocA_pitch[0][i] > 0 and vocB_pitch[0][i] > 0                \
        and vocA_pitch[0][i-1] > 0 and vocB_pitch[0][i-1] > 0            \
        and vocA_pitch[0][i+1] > 0 and vocB_pitch[0][i+1] > 0:
           diff_AB.append(abs(diff_vocA[0][i]-diff_vocB[0][i]))
        else:
           diff_AB.append(0)
    
    sum_diff_AB = sum(diff_AB)
    return sum_diff_AB

def auto_selection_model(path, file):
    diff_en_d = get_diff_pitch_trend(path, 'EN_D/', file)
    diff_ch_d = get_diff_pitch_trend(path, 'CH_D/', file)
    diff_en_s = get_diff_pitch_trend(path, 'EN_S/', file)
    
    if min([diff_en_d, diff_ch_d, diff_en_s])==diff_en_d:
        return 'EN_D'
    elif min([diff_en_d, diff_ch_d, diff_en_s])==diff_ch_d:
        return'CH_D'
    else:
        return'EN_S'

if __name__ == '__main__':    
    
    src_root = './pitch_data_in_auto_selection/EN_D'
    audio_names = os.listdir(src_root)
    path = './pitch_data_in_auto_selection/'
    a = []
    for file in audio_names:
        print("======================")
        print('Song ID:' + file.split('.')[0])
        print('Auto-Selection model:' + auto_selection_model(path, file))