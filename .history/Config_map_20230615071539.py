import yaml
import os

#Nhập folder demo và chính thức
folder_path_official = 'kube-2023-06-14/configmap' 
folder_path_demo = 'kube-2023-06-14-demo/configmap'
output_file_path = 'output_config.txt'

def get_file_names(folder_path):
    """
    Lấy tên các file
    ===============================
    Arg: Đường dẫn đến folder
    Return: List các tên file
    """
    file_names = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_names.append(file)
    return file_names

def get_config_keys(path): 
    """
    Lấy các key trong configmap 
    ===============================
    Arg: Đường dẫn đến file
    Return: List các keys
    """
    key_list = []
    with open(path, 'r', encoding='utf-8') as f:
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        for data_key in yaml_data['data'].keys():
            key_list.append(data_key)
    return key_list

def show_diff_config(official_path, demo_path): 
    """
    In ra sự khác biệt của config  
    ===============================
    Arg: Đường dẫn đến 2 file
    Return: Sự khác biệt giữa các key của 2 file
    """
    key_set_official = set(get_config_keys(official_path))
    key_list_demo = set(get_config_keys(demo_path))
    diff_demo_official = key_list_demo - key_set_official
    diff_official_demo = key_set_official - key_list_demo

    # Ghi kết quả vào file txt với bộ mã UTF-8
    with open(output_file_path, 'a', encoding='utf-8') as f:
        if diff_demo_official or diff_official_demo:
            f.write("====================================)
            f.write(f"Kiểm tra: {os.path.basename(official_path)}\n")
        if diff_demo_official:
            f.write("Các keys có trong demo mà không có trong official: ")
            f.write(', '.join(diff_demo_official))
            f.write("\n")
        if diff_official_demo:
            f.write("Các keys có trong official mà không có trong demo: ")
            f.write(', '.join(diff_official_demo))
            f.write("\n")

def main():
    #Lấy tên file của hai folder demo và chính thức
    official_files = set(get_file_names(folder_path_official))
    demo_files = set(get_file_names(folder_path_demo))

    # Ghi kết quả vào file txt với bộ mã UTF-8
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write("Các file có trong official mà không có trong demo\n")
        f.write(', '.join(official_files - demo_files))
        f.write("\n\n")
        f.write("Các file có trong demo mà không có trong official\n")
        f.write(', '.join(demo_files - official_files))
        f.write("\n\n")

    #Lấy ra các file chung giữa hai folder 
    common_elements = official_files & demo_files
    for file in common_elements:
        official_path = os.path.join(folder_path_official, file)
        demo_path = os.path.join(folder_path_demo, file)
        show_diff_config(official_path, demo_path)

main()
