import yaml

def get_image(path):
    with open(path) as f: 
        yaml_data = yaml.load(f,Loader=yaml.FullLoader)
        # for key in yaml_data.keys(): 
        #     for data_key in yaml_data['spec'].keys():
        #         key
        print(yaml_data['spec']['template'][])
    return
get_image("kube-2023-06-14-demo/deployment.apps/acmadmin-api-dep.yaml")
