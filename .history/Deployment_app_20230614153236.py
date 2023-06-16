import yaml
import os

def get_image(path):
    with open(path) as f: 
        yaml_data = yaml.load(f,Loader=yaml.FullLoader)
        image = yaml_data['spec']['template']['spec']['containers'][0]['image']
        print(image)
    return image
get_image("kube-2023-06-14-demo/deployment.apps/acmadmin-api-dep.yaml")

folder_path = 'kube-2023-06-14-demo/deployment.apps'  
# Get all file paths in the folder
file_paths = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_paths.append(os.path.join(root, file))

for path in file_paths: 
    get_image(path)