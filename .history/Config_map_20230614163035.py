import yaml
import os
from itertools import zip_longest
folder_path_official = 'kube-2023-06-14/configmap' 
folder_path_demo = 'kube-2023-06-14-demo/configmap'

def get_config_keys(path): 
    key_list = []
    with open(path,'r',encoding='utf-8') as f:
        yaml_data = yaml.load(f,Loader=yaml.FullLoader)
        for data_key in yaml_data['data'].keys():
            key_list.append(data_key)
        return key_list

def get_file_names(folder_path):
    # Get all file names in the folder
    file_names = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_names.append(file)
    return file_names


def show_diff_config(official_path, demo_path): 
    key_set_official = set(get_config_keys(official_path))
    key_list_demo = set(get_config_keys(demo_path))
    if(key_set_official == key_list_demo):
        print("Không có sự khác biệt")
        return 
    # In ra key có trong demo mà không có trong official
    diff_demo_official = key_list_demo - key_set_official
    if diff_demo_official:
        print("Các keys có trong demo mà không có trong official: ",diff_demo_official)

    # In ra keys có trong official mà không có trong demo
    diff_official_demo = key_set_official - key_list_demo
    if diff_official_demo:
        print("Các keys có trong official mà không có trong demo: ",diff_official_demo)



official_files = set(get_file_names(folder_path_official))
demo_files = set(get_file_names(folder_path_demo))
print("=============================================================")

#In ra các file có trong official mà không có trong demo
print(official_files - demo_files)
#In ra các file có trong demo mà không có trong official
print(demo_files - official_files)
common_elements = official_files & demo_files
for file in common_elements:
    print("==============================================================")
    print("Kiểm tra: "+file)
    official_path = os.path.join(folder_path_official,file)
    demo_path = os.path.join(folder_path_demo,file)
    show_diff_config(official_path,demo_path)