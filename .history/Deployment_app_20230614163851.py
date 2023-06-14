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


def show_diff_images(official_path, demo_path): 
    official_iamge = get_image(official_path)
    demo_image = get_image(demo_path)
    if(official_iamge == demo_image):
        print("Không có sự khác biệt")
        return 
    # In ra key có trong demo mà không có trong official
    diff_demo_official = demo_image - official_iamge
    if diff_demo_official:
        print("Các keys có trong demo mà không có trong official: ",diff_demo_official)

    # In ra keys có trong official mà không có trong demo
    diff_official_demo = key_set_official - key_list_demo
    if diff_official_demo:
        print("Các keys có trong official mà không có trong demo: ",diff_official_demo)
    return diff_demo_official,diff_official_demo

official_files = set(get_file_names(folder_path_official))
demo_files = set(get_file_names(folder_path_demo))
print("=============================================================")
print("Các file có trong official mà không có trong demo")
#In ra các file có trong official mà không có trong demo
print(official_files - demo_files)
print("các file có trong demo mà không có trong official")
#In ra các file có trong demo mà không có trong official
print(demo_files - official_files)
common_elements = official_files & demo_files
for file in common_elements:
    print("==============================================================")
    print("Kiểm tra: "+file)
    official_path = os.path.join(folder_path_official,file)
    demo_path = os.path.join(folder_path_demo,file)
    show_diff_config(official_path,demo_path)