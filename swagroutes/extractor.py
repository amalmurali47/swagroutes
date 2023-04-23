import yaml
import json
from pathlib import Path


def load_yaml_file(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def extract_routes(swagger_data, include_params=False):
    routes = set()
    base_path = swagger_data.get('basePath', '')
    paths = swagger_data.get('paths', {})

    http_methods = {'get', 'put', 'post', 'delete', 'options', 'head', 'patch', 'trace'}

    for path, methods in paths.items():
        for method, details in methods.items():
            if method.lower() in http_methods:
                route = f'{method.upper()} {base_path}{path}'
                if include_params:
                    parameters = details.get('parameters', [])
                    query_params = [param['name'] for param in parameters if param['in'] == 'query']
                    if query_params:
                        route += '?' + '&'.join(query_params)
                routes.add(route)

    return routes


def process_swagger_files(files, include_params=False):
    all_routes = set()

    for file in files:
        file_extension = file.suffix.lower()
        if file_extension == '.yaml':
            swagger_data = load_yaml_file(file)
        elif file_extension == '.json':
            swagger_data = load_json_file(file)
        else:
            continue
        routes = extract_routes(swagger_data, include_params)
        all_routes.update(routes)

    return all_routes

