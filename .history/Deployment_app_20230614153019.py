import yaml
import os
def get_image(path):
    with open(path) as f: 
        yaml_data = yaml.load(f,Loader=yaml.FullLoader)
        # for key in yaml_data.keys(): 
        #     for data_key in yaml_data['spec'].keys():
        #         key
        print(yaml_data['spec']['template']['spec']['containers'][0]['image'])
    return
get_image("kube-2023-06-14-demo/deployment.apps/acmadmin-api-dep.yaml")
folder_path = '/path/to/folder'  # Replace with the actual folder path

# Get all file paths in the folder
file_paths = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_paths.append(os.path.join(root, file))