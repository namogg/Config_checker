import yaml
def get_config_keys(path): 
    key_list = []
    with open(path,'r') as f:
        yaml_data = yaml.load(f,Loader=yaml.FullLoader)
        for key in yaml_data.keys(): 
            for data_key in yaml_data['data'].keys():
                print(data_key)
                key_list.append(data_key)
        return key_list

key_list = get_config_keys('kube-2023-06-14/configmap/acm-api-config.yaml')
key_list = get_config_keys('/')
set_official = set(key_list)
set_demo = 