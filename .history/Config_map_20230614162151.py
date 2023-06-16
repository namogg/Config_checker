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


def show_diff_config(officail_path, demo_path): 
    key_list = get_config_keys(officail_path)
    key_list_demo = get_config_keys(demo_path)
    set_official = set(key_list)
    set_demo = set(key_list_demo)
    #In ra key có trong demo mà không có trong official
    print(set_demo-set_official)
    #In ra keys có trong offical mà không có trong demo 
    print(set_official - set_demo)

official_files = set(get_file_names(folder_path_official))
demo_files = set(get_file_names(folder_path_demo))

#In ra các file có trong official mà không có trong demo
print(official_files - demo_files)
#In ra các file có trong demo mà không có trong official
print(set(demo_files) - official_files
common_elements = set(list1) & set(list2)
for file in set()