import argparse
from pathlib import Path
from .extractor import process_swagger_files


def main():
    parser = argparse.ArgumentParser(description='Extract routes from Swagger files.')
    parser.add_argument('input', metavar='input', type=str, nargs='+', help='Input file(s) or directory containing Swagger files.')
    parser.add_argument('-o', '--output', type=str, help='Output file to store the results.')

    args = parser.parse_args()

    input_files = []

    for input_path in args.input:
        path = Path(input_path)
        if path.is_file():
            input_files.append(path)
        elif path.is_dir():
            input_files.extend(path.glob('**/*.yaml'))
            input_files.extend(path.glob('**/*.json'))

    all_routes = process_swagger_files(input_files)

    if args.output:
        with open(args.output, 'w') as outfile:
            outfile.write('\n'.join(all_routes))
    else:
        for route in all_routes:
            print(route)

