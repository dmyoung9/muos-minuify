import re
import requests
import os
from collections import defaultdict

# URL to the raw theme.c file in the GitHub repo
BANCH_MAP = {"Banana": "e81f65f9b883412ccaf9651a96dd921cbfd7df4b",
             "Current": "main"}

REPO_OWNER = "MustardOS"
REPO_NAME = "frontend"
BRANCH = BANCH_MAP["Current"]

GITHUB_URL = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/common/theme.c"

def download_theme_file(url, local_filename):
    """Download the theme.c file from GitHub."""
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_filename, 'w') as file:
            file.write(response.text)
        print(f"Downloaded {local_filename} from {url}")
    else:
        raise Exception(f"Failed to download file: {response.status_code}")

def extract_configurations(file_path):
    """Extract configurations from the theme.c file."""
    # Regular expression to match get_ini_hex, get_ini_int, and get_ini_string patterns
    ini_pattern = re.compile(r'get_ini_(hex|int|string)\(\s*(\w+),\s*"(\w+)",\s*"(\w+)"(?:,\s*(.+?))?\s*\)')
    
    # Dictionary to store sections and their keys/values
    config = defaultdict(dict)

    with open(file_path, 'r') as file:
        # Read the entire content of the file
        content = file.read()

    # Remove all whitespace (spaces, newlines, tabs) from the content
    content_no_whitespace = re.sub(r'\s+', '', content)

    # Now apply the regex pattern to the whitespace-free content
    matches = ini_pattern.findall(content_no_whitespace)

    for match in matches:
        value_type, muos_theme, section, key, default_value = match

        # Adjust the default value based on the type
        if muos_theme != "muos_theme":
            print(f"Weird {muos_theme} != muos_theme")
        if muos_theme != "muos_theme_overrides":
            if value_type == "hex":
                config[section][key] = "UNKNOWN_HEX"
            elif value_type == "int":
                if default_value and default_value.isdigit():
                    config[section][key] = default_value.strip()
                else:
                    config[section][key] = "UNKNOWN_INT"
            elif value_type == "string":
                config[section][key] = f'{default_value.strip()}' if default_value else 'UNKNOWN_STRING'

    return config

def generate_template(config, output_file):
    """Generate the output template file from the extracted configuration."""
    with open(output_file, 'w') as file:
        for section, values in config.items():
            file.write(f'[{section}]\n')
            for key, default_value in values.items():
                file.write(f'{key}={default_value}\n')
            file.write('\n')  # Add a blank line between sections

def cleanup(file_path):
    """Remove the downloaded theme.c file after processing."""
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Cleaned up: {file_path}")

def main():
    # Local filename for the downloaded theme.c
    local_file = 'theme.c'
    
    # Download the latest theme.c file from the GitHub repo
    download_theme_file(GITHUB_URL, local_file)

    # Extract configurations from the C file
    config = extract_configurations(local_file)
    
    # Generate the template file
    output_file = os.path.join('Helper Scripts','Generate Scheme File From Source','Default Scheme File.txt')
    generate_template(config, output_file)
    print(f"Template generated: {output_file}")
    
    # Clean up the downloaded theme.c file
    cleanup(local_file)

if __name__ == "__main__":
    main()
