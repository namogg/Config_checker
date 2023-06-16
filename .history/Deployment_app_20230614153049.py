import yaml
import os
def get_image(path):
    with open(path) as f: 
        yaml_data = yaml.load(f,Loader=yaml.FullLoader)
        image = yaml_data['spec']['template']['spec']['containers'][0]['image']
        print()
    return
get_image("kube-2023-06-14-demo/deployment.apps/acmadmin-api-dep.yaml")
folder_path = ''  

# Get all file paths in the folder
file_paths = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_paths.append(os.path.join(root, file))