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
    -------
        - file_names: List các tên file
    """
    file_names = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_names.append(file)
    return file_names

def get_image(path):
    """
    Lấy ra image trong deployment app

    Arg: 
    --------
        - path: Đường dẫn đến file deployment app
     Return: 
    -------
        - image: nội dung image

    """
    with open(path) as f: 
        yaml_data = yaml.load(f,Loader=yaml.FullLoader)
        image = yaml_data['spec']['template']['spec']['containers'][0]['image']
    return image
 
def compare_versions(official_image, demo_image):
    """
    So sánh version hai image 

    Arg: 
    --------
        - official_image: image bản chính thức
        - demo_imageL image bản demo
     Return: 
    -------
        - official_version: version của bản chính thức
        - demo_vesion: version bản demo
    """
    official_version = official_image.split(":")
    demo_version = demo_image.split(":")
    if(official_version[1] == demo_version[1]):
        print("Không có sự khác biệt")
    else: 
        print("Có sự khác biệt() Chính thức"+official_version[1],demo_version[1])
    official_version = official_image.split(":")
    return official_version,demo_version

def show_diff_images(official_path, demo_path): 
    #Lấy hai image và so sánh version
    official_image = get_image(official_path)
    demo_image = get_image(demo_path)
    compare_versions(official_image,demo_image)

def main(): 
    #Lấy tên file của hai folder demo và chính thức
    official_files = set(get_file_names(folder_path_official))
    demo_files = set(get_file_names(folder_path_demo))
    print("=============================================================")
    print("Các file có trong official mà không có trong demo")
    print(official_files - demo_files)
    print("các file có trong demo mà không có trong official")
    print(demo_files - official_files)
    #Lấy các file chung giữa hai folder
    common_elements = official_files & demo_files
    for file in common_elements:
        print("==============================================================")
        print("Kiểm tra: "+file)
        official_path = os.path.join(folder_path_official,file)
        demo_path = os.path.join(folder_path_demo,file)
        show_diff_images(official_path,demo_path)

main()