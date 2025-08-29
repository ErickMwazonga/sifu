import json

def parse_json_file(input_file, output_file):
    with open(input_file, 'r') as file:
        json_string = file.read()
        file.close()

    data = json.loads(json_string)

    with open(output_file, 'w') as file:
        file.write(data)
        file.close()


input_file = '/Users/erimwazo/Documents/input.json'
output_file = '/Users/erimwazo/Documents/output.json'

parse_json_file(input_file, output_file)
