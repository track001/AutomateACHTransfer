import paramiko  # Importing the Paramiko library for SSH and SFTP functionality
# import os  # Importing the os module for file operations and path manipulation


def transfer_ach_file():
    # SSH connection details for the remote server (bank)
    hostname = "example.com"  # Replace with the actual hostname or IP address
    port = 22  # SSH port (default is 22)
    username = "your_username"  # Replace with your username on the remote server
    private_key_path = "/path/to/your/private/key"  # Replace with the path to your private key file

    # Remote directory on the server
    remote_dir = "/path/to/remote/directory"  # Replace with the desired remote directory

    # Create SSH client and load the private key
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

    try:
        # Connect to the remote server using SSH key-based authentication
        ssh.connect(hostname, port=port, username=username, pkey=private_key)
        sftp = ssh.open_sftp()

        # Transfer the ACH file to the remote server
        sftp.put("sample.ach", f"{remote_dir}/sample.ach")
        sftp.close()

        print("ACH file transferred successfully via SFTP.")
    finally:
        # Close the SSH connection
        ssh.close()

def generate_ach_file():
    # Generate the ACH file content (example)
    ach_content = "I'm an example ACH file :D"

    # Save the ACH file
    file_path = "sample.ach"
    with open(file_path, "w") as file:
        file.write(ach_content)

    print("ACH file generated.")

def automate_ach_file_transfer():
    generate_ach_file()
    transfer_ach_file()

# Entry point of the script
if __name__ == "__main__":
    automate_ach_file_transfer()
