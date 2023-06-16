import yaml

def get_image(path):
    with open(path) as f: 
        yaml_data = yaml.load(f,Loader=yaml.FullLoader)
        for key in yaml_data.keys(): 
            print(key)
            for data_key in yaml_data['spec'].keys():
                #print(data_key)
    retủn
get_image("kube-2023-06-14-demo/deployment.apps/acm-api-dep.yaml")