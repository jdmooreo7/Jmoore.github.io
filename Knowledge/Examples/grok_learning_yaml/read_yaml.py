import yaml

#loads the yaml file jon.yml, the script can now use this
with open('jon.yml', 'r') as file:
    data = yaml.safe_load(file)
#prints the data in the yaml file
print(data)

#only prints the name of the person
print(data['student']['name'])