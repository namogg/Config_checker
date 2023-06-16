import yaml
import os
folder_path_official = 'kube-2023-06-14-demo/deployment.apps' 
folder_path_demo = 'kube-2023-06-14-demo/deployment.apps'

def get_config_keys(path): 
    key_list = []
    with open(path,'r') as f:
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

def show_diff(officail_path, demo_path): 
    key_list = get_config_keys(officail_path)
    key_list_demo = get_config_keys(demo_path)
    set_official = set(key_list)
    set_demo = set(key_list_demo)
    #In ra key có trong demo mà không có trong official
    print(set_demo-set_official)
    #In ra keys có trong offical mà khôgn có trong demo 
    print(set_official - set_demo)

show_diff()