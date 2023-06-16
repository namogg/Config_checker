import yaml

with open('file.yaml', 'r') as file:
    yaml_data = yaml.load(file, Loader=yaml.FullLoader)

# Access the data from the YAML file
print(yaml_data)