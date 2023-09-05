import yaml


def yaml_parser():
    with open('db_creds.yaml', 'r') as file:
        parser = yaml.safe_load(file)
        return parser
