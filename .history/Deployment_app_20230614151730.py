import yaml

def get_image(path):
    with open(path) as f: 
        yaml_data = yaml.load(f,Loader=yaml.FullLoader)
        for key in yaml_data.keys(): 
            for data_key in yaml_data['data'].keys():
                print(data_key)

get_image("kube-2023-06-14-demo/deployment.apps/acm-api-dep.yaml")