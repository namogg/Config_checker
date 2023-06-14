import yaml

def get_image(path):
    with open(path) as f: 
        yaml_data = yaml.load(f,Loader=yaml.FullLoader)
        for key in yaml_data.keys(): 
            for data_key in yaml_data['data'].keys():
                print(data_key)
        return key_list
