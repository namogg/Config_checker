import yaml
import os
#Nhập đường dẫn đến folder chính thức và demo
folder_path_official = 'kube-2023-06-14/deployment.apps' 
folder_path_demo = 'kube-2023-06-14-demo/deployment.apps'

def get_file_names(folder_path):
    """
    Lấy tên các file

    Arg: 
    --------
        - folder_path: Đường dẫn đến folder
     Return: 
     List các tên file
    """
    file_names = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_names.append(file)
    return file_names

def get_image(path):
    """
    Lấy ra image trong deployment app

    """
    with open(path) as f: 
        yaml_data = yaml.load(f,Loader=yaml.FullLoader)
        image = yaml_data['spec']['template']['spec']['containers'][0]['image']
    return image
 
def compare_versions(version1, version2):
    official_version = version1.split(":")
    demo_version = version2.split(":")
    if(official_version[1] == demo_version[1]):
        print("Không có sự khác biệt")
    else: 
        print("Có sự khác biệt: "+official_version[1],demo_version[1])

def show_diff_images(official_path, demo_path): 
    official_image = get_image(official_path)
    demo_image = get_image(demo_path)
    compare_versions(official_image,demo_image)

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
    show_diff_images(official_path,demo_path)