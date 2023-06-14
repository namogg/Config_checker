import yaml
def get_config_keys(path): 
    key_list = []
    with open(path,'r') as f:
        yaml_data = yaml.load(f,Loader=yaml.FullLoader)
        for data_key in yaml_data['data'].keys():
            print(data_key)
            key_list.append(data_key)
        return key_list
def get_path():
    folder_path = 'kube-2023-06-14-demo/deployment.apps'  
# Get all file paths in the folder
file_paths = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_paths.append(os.path.join(root, file))

for path in file_paths: 
    get_image(path)

def show_diff(): 
    key_list = get_config_keys('kube-2023-06-14/configmap/acm-api-config.yaml')
    key_list_demo = get_config_keys('kube-2023-06-14-demo/configmap/acm-api-config.yaml')
    set_official = set(key_list)
    set_demo = set(key_list_demo)
    #In ra key có trong demo mà không có trong official
    print(set_demo-set_official)
    #In ra keys có trong offical mà khôgn có trong demo 
    print(set_official - set_demo)