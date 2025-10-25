import yaml
from pathlib import Path

# Load the YAML from a file located next to this script
here = Path(__file__).parent
jon_path = here / 'jon.yml'
with jon_path.open('r', encoding='utf-8') as file:
    data = yaml.load(file, Loader=yaml.SafeLoader)

# Get the list of favorite subjects and other fields
student = data.get('student', {})
subjects = student.get('favorite_subject', [])
name = student.get('name', 'Unknown')
bio = student.get('bio', '').strip()
age = student.get('age', None)
email = student.get('email', None)

# Print the bio, age, and email (preserve multi-line formatting)
if bio:
    print(f"\n{name}'s bio:\n{bio}\n")

if age:
    print(f"{name} is {age} years old.\n")

if email:
    print(f"Contact {name} at: {email}\n")

# Loop through the subjects
for subject in subjects:
    print(f"{name} likes: {subject}")


# How It Works (short)
# - YAML is loaded into a Python dict via yaml.safe_load (yaml.load with SafeLoader).
# - We access nested keys with .get to avoid KeyError if a field is missing.
# - The bio field is a multi-line string (block scalar) in the YAML and is printed as-is.