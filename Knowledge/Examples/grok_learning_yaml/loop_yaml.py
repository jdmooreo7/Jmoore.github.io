import yaml

# Load the YAML from a file
with open('jon.yml', 'r') as file:
    data = yaml.load(file, Loader=yaml.SafeLoader)

# Get the list of favorite subjects
subjects = data['student']['favorite_subject']
name = data['student']['name']

# Loop through the subjects
for subject in subjects:
    print(f"{name} likes: {subject}")


# How It Works
#data['student']['favorite_subjects']:
#data is the dictionary from the YAML.
#data['student'] gets the nested dictionary under student.
#data['student']['favorite_subjects'] grabs the list ['Math', 'Econ'].
#for subject in subjects::
#This is a Python for loop. It iterates over each item in the subjects list.
#subject takes the value of each item (Math, then Econ) one at a time.
#print(f"Jon likes: {subject}"):
#The f-string (f"...") lets us mix text and variables.
#{subject} inserts the current subject into the string.