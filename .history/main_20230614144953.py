import yaml

with open('kube-2023-06-14/configmap/acm-api-config.yaml','r') as f:
    yaml_data = yaml.load(f,Loader=yaml.FullLoader)
    for key in yaml_data.keys(): 
        print(yaml_data['data']