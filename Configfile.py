import json
import os
from flask import Flask, jsonify
config_file_path = 'configuration.ini'
def parse_config_file(file_path):
    config = {}
    try:
        with open(file_path, 'r') as file:
            section = None
            for line in file:
                line = line.strip()
                if line.startswith('[') and line.endswith(']'):  # Section header
                    section = line[1:-1]
                    config[section] = {}
                elif '=' in line:
                    key, value = line.split('=', 1)
                    key, value = key.strip(), value.strip()
                    if section:
                        config[section][key] = value
        return config
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def save_to_json(data):
    with open('config_output.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

app = Flask(__name__)

@app.route('/get-config', methods=['GET'])
def get_config():
    try:
        with open('config_output.json', 'r') as json_file:
            data = json.load(json_file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Configuration data not found"}), 404

def main():
    config = parse_config_file(config_file_path)
    if config:
        print("Configuration File Parser Results:")
        for section, values in config.items():
            print(f"{section}:")
            for key, value in values.items():
                print(f"- {key}: {value}")
        
        # Save the output data as JSON
        save_to_json(config)
    
    # Start the Flask app
    app.run(debug=True)

if __name__ == '__main__':
    main()
