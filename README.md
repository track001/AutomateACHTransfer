# ACH File Transfer Automation

This project automates the transfer of ACH (Automated Clearing House) files to a remote server using Python and the Paramiko library for SSH and SFTP functionality.

## Features

- Establishes an SSH connection to the remote server using key-based authentication.
- Transfers the ACH file to the remote server securely using SFTP.
- Customizable SSH connection details such as hostname, port, username, and private key path.
- Provides clear console output for file generation and transfer status.

## Prerequisites

- ```Python 3.x```.
- Paramiko library (`pip install paramiko`).

## Usage

1. Configure the SSH connection details and remote directory in the code.
2. Run the script: `python main.py`.
3. The script will generate a sample ACH file and transfer it to the specified remote server.
4. Monitor the console output for the status of the ACH file transfer.

## Configuration

In the `main.py` file, update the following variables with your specific details:



```python
hostname = "example.com"  # Replace with the actual hostname or IP address
port = 22  # SSH port (default is 22)
username = "your_username"  # Replace with your username on the remote server
private_key_path = "/path/to/your/private/key"  # Replace with the path to your private key file
remote_dir = "/path/to/remote/directory"  # Replace with the desired remote directory
