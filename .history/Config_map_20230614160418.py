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
    
def get_file_path(folder_path):
    # Get all file paths in the folder
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def show_diff_config(officail_path, demo_path): 
    key_list = get_config_keys(officail_path)
    key_list_demo = get_config_keys(demo_path)
    set_official = set(key_list)
    set_demo = set(key_list_demo)
    #In ra key có trong demo mà không có trong official
    print(set_demo-set_official)
    #In ra keys có trong offical mà không có trong demo 
    print(set_official - set_demo)


official_paths = set(get_file_path(folder_path_official))
demo_paths = set(get_file_path(folder_path_demo))
unique_files = official_paths.symmetric_difference(demo_paths)

from itertools import zip_longest

for official_path, demo_path in zip_longest(official_paths, demo_paths):
    if official_path and demo_path:
        filename = os.path.basename(official_path)
        filename_demo = os.path.basename(demo_path)
        
        if filename == filename_demo:
            print(f"Difference for file: {filename}")
            show_diff_config(official_path, demo_path)
            print()
        else:
            print(f"File names do not match: {filename} and {filename_demo}")
    elif official_path:
        filename = os.path.basename(official_path)
        print(f"File missing in demo: {filename}")
    elif demo_path:
        filename = os.path.basename(demo_path)
        print(f"File missing in official: {filename}")
