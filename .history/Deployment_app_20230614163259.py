import yaml
import os

folder_path_official = 'kube-2023-06-14/configmap' 
folder_path_demo = 'kube-2023-06-14-demo/configmap'

def get_file_names(folder_path):
    # Get all file names in the folder
    file_names = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_names.append(file)
    return file_names

def get_image(path):
    with open(path) as f: 
        yaml_data = yaml.load(f,Loader=yaml.FullLoader)
        image = yaml_data['spec']['template']['spec']['containers'][0]['image']
        print(image)
    return image
