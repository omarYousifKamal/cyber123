import os
import shutil
import logging
import random
import string
import requests
import urllib3
from flask import Flask, request, redirect
from flask import Flask, request, render_template_string

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
app = Flask(__name__)



def copy_file(source, destination):
    if os.path.exists(source):
        shutil.copy2(source, destination)
        logging.info(f"File '{source}' copied to '{destination}' successfully.")
    else:
        logging.warning(f"File '{source}' does not exist.")

def list_files(directory):
    if os.path.exists(directory):
        files = os.listdir(directory)
        logging.info(f"Listing files in directory '{directory}': {', '.join(files)}")
        return files
    else:
        logging.warning(f"Directory '{directory}' does not exist.")
        return []

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
        logging.info(f"Directory '{directory}' created successfully.")
    else:
        logging.warning(f"Directory '{directory}' already exists.")


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))



def execute_command(command):
    os.system(command)
    logging.info(f"Command '{command}' executed successfully.")

def main():
    file_to_delete = input("Enter the name of the file to delete: ")
    delete_file(file_to_delete)
    print("File deleted successfully.")
    
    file_to_move = input("Enter the name of the file to move: ")
    destination = input("Enter the destination folder: ")
    move_file(file_to_move, destination)
    print("File moved successfully.")

    file_to_copy = input("Enter the name of the file to copy: ")
    destination_copy = input("Enter the destination folder to copy to: ")
    copy_file(file_to_copy, destination_copy)
    print("File copied successfully.")

    directory_to_list = input("Enter the directory to list files from: ")
    listed_files = list_files(directory_to_list)
    print("Files listed successfully:", listed_files)

    directory_to_create = input("Enter the name of the directory to create: ")
    create_directory(directory_to_create)
    print("Directory created successfully.")

    directory_to_delete = input("Enter the name of the directory to delete: ")
    delete_directory(directory_to_delete)
    print("Directory deleted successfully.")

    random_string_length = int(input("Enter the length of the random string to generate: "))
    random_string = generate_random_string(random_string_length)
    print("Random string generated successfully:", random_string)

    filename_to_write = input("Enter the name of the file to write random string to: ")
    write_to_file(filename_to_write, random_string)
    print("Random string written to file successfully.")

    filename_to_read = input("Enter the name of the file to read from: ")
    file_content = read_from_file(filename_to_read)
    print("File content read successfully:", file_content)

    filename_to_checksum = input("Enter the name of the file to calculate checksum for: ")
    file_checksum = calculate_checksum(filename_to_checksum)
    print("File checksum calculated successfully:", file_checksum)

    command_to_execute = input("Enter the command to execute: ")
    execute_command(command_to_execute)
    print("Command executed successfully.")

if __name__ == "__main__":
    main()


def fetch_data_from_server(url):
    try:
        response = requests.get(url, verify=False)  # Disables SSL certificate verification
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

url = input("Enter the URL of the server to fetch data from: ")
data = fetch_data_from_server(url)
if data:
    print("Data fetched successfully:", data)
else:
    print("Failed to fetch data from the server.")

@app.route('/redirect')
def redirect_to_url():
    target = request.args.get('url')
    return redirect(target)

if __name__ == '__main__':
    app.run(debug=True)

    