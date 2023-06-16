import yaml
import os

#Nhập đường dẫn đến folder chính thức và demo
folder_path_official = 'kube-2023-06-14/deployment.apps' 
folder_path_demo = 'kube-2023-06-14-demo/deployment.apps'
output_file_path = 'output.txt' # Đường dẫn đến file txt bạn muốn tạo

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
        return "Không có sự khác biệt"
    else: 
        return f"Có sự khác biệt( Chính thức: {official_version[1]} Demo: {demo_version[1]}"

def show_diff_images(official_path, demo_path): 
    #Lấy hai image và so sánh version
    official_image = get_image(official_path)
    demo_image = get_image(demo_path)
    return compare_versions(official_image, demo_image)

def main(): 
    #Lấy tên file của hai folder demo và chính thức
    official_files = set(get_file_names(folder_path_official))
    demo_files = set(get_file_names(folder_path_demo))
    
    # Ghi ra file txt
    with open(output_file_path, 'w',encoding='utf-8') as f:
        f.write("Các file có trong official mà không có trong demo:\n")
        f.write('\n'.join(official_files - demo_files))
        f.write("\n\n")
        f.write("Các file có trong demo mà không có trong official:\n")
        f.write('\n'.join(demo_files - official_files))
        f.write("\n\n")
    
        #Lấy các file chung giữa hai folder
        common_elements = official_files & demo_files
        for file in common_elements:
            f.write("=============================\n")
            f.write("Kiểm tra: " + file + "\n")
            official_path = os.path.join(folder_path_official, file)
            demo_path = os.path.join(folder_path_demo, file)
            diff = show_diff_images(official_path, demo_path)
            f.write(diff + "\n")

    print("Đã ghi")

main()
