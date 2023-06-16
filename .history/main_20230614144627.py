import yaml

with open('/','r') as f:
    yaml_data = yaml.load(f,Loader=yaml.FullLoader)