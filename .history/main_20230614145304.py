import yaml
def get_config_keys(): 
    key_list = []
    with open('kube-2023-06-14/configmap/acm-api-config.yaml','r') as f:
        yaml_data = yaml.load(f,Loader=yaml.FullLoader)
        for key in yaml_data.keys(): 
            for data_key in yaml_data['data'].keys():
                print(type(data_key))
                key_list.append(data_key)
        return 