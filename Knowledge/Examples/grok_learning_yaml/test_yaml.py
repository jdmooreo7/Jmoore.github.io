import yaml

# Your YAML content as a string for testing
yaml_content = """
student:
  name: Jon
  age: 43
  favorite_subjects:
    - Math
    - Econ
  bio: |
    Jon lives in Ohio.
    Jon is awesome.
"""

# Load and print the data
data = yaml.safe_load(yaml_content)
print(data)