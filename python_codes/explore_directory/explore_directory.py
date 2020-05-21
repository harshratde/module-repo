# -*- coding: utf-8 -*-
"""
Created on Thu May 21 12:47:09 2020

@author: harsh
"""


import os 

INPUT_DIR_PATH = 'C:/Users/harsh/projects/mmm_sage'

os.listdir(INPUT_DIR_PATH )

def get_dir_details(DIR_PATH,level = 1, dir_repo = {}):
    
    if f'level_{level}' not in dir_repo.keys():
        dir_repo.update({f'level_{level}':{
                                    'PATH' : [DIR_PATH]
                                ,   'number_of_items': 0
                                ,   'dir_len' : 0
                                ,   'dir_space' : 0
                                ,   'files_len'   : 0
                                ,   'files_space' : 0
                                }
                        })
    else:
        dir_repo[f'level_{level}']['PATH'].append(DIR_PATH)

    
    list_of_files = os.listdir(DIR_PATH)
    dir_repo[f'level_{level}']['number_of_items'] = dir_repo[f'level_{level}']['number_of_items'] + len(list_of_files)
       
    track_dir = 0
    if len(list_of_files)>0:
        for item in list_of_files:
            # item = list_of_files[-1]

            ITEM_PATH = os.path.join(DIR_PATH,item)
            
            if os.path.isdir(ITEM_PATH):
                
                track_dir = track_dir +1
                
                dir_repo[f'level_{level}']['dir_len'] = dir_repo[f'level_{level}']['dir_len'] + 1
                print(f'Levels: {level} - track_dir : {track_dir}')      
                dir_repo = get_dir_details(ITEM_PATH,level+1, dir_repo)
                
            else:
                dir_repo[f'level_{level}']['files_space']    = dir_repo[f'level_{level}']['files_space']  + os.path.getsize(ITEM_PATH)/1000
                dir_repo[f'level_{level}']['files_len']      = dir_repo[f'level_{level}']['files_len'] + 1
            
    if track_dir >0:
        dir_repo[f'level_{level}']['dir_space']     = dir_repo[f'level_{level+1}']['dir_space'] + dir_repo[f'level_{level+1}']['files_space']
        
    return dir_repo

out_repo = get_dir_details(INPUT_DIR_PATH)
    