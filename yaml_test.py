import yaml

with open("application.yaml", "r") as yamlFile:
    config = yaml.load(yamlFile)

for section in config:
    print(section)
