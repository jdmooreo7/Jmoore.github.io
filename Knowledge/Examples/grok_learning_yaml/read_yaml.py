import yaml

with open('jon.yml', 'r') as file:
    data = yaml.safe_load(file)
    print(data)