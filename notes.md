# Testing Environment
Using publicly available FTP for demonstration and testing.

Host: 'test.rebex.net'
Username: 'demo'
Password: 'password'

Avoid testing sensitive information, generate a sample ACH file.


# Generate a SSH key pair
- Open a terminal or command prompt on your local machine.
- Use the following command to generate an SSH key pair: ``` ssh-keygen -t rsa -b 2048```
- Press "Enter" to accept the default file location and passphrase (leave empty if you don't want to set a passphrase - not recommended).

# Upload the public key to the remote server (WF Bank)
- Provide the ```id_rsa``` (private key) and ```id_rsa.pub``` (public key).
- WF should assist in uploading the public key to the appropriate location on the remote server.

## Don't have access to the business application environments? Follow these steps!
- **Set up a local SSH server**: Install an SSH server software on your local machine to simulate the remote server. Some popular options are OpenSSH (available for various operating systems) or Bitvise SSH Server (for Windows).
  - Set up a local SSH server:
    - For Windows: You can use Bitvise SSH Server, which provides a simple installation and configuration process. You can download it from the Bitvise website (https://www.bitvise.com/ssh-server-download).
    - For macOS/Linux: OpenSSH is typically available by default on these operating systems. If it's not already installed, you can install it using the package manager for your distribution (e.g., `apt-get` for Ubuntu, `yum` for CentOS).
-**Generate SSH key pair**: Generate an SSH key pair (public and private key) using a tool like ssh-keygen. This will allow you to authenticate with the local SSH server.
  - Open a terminal or command prompt on your local machine.
  - Run the following command to generate an SSH key pair:
    - `ssh-keygen -t rsa`.
  - You will be prompted to enter a file path for saving the keys. Press Enter to accept the default location `(~/.ssh/id_rsa)` or provide a different path if desired.
  - You will also be prompted to enter a passphrase. You can choose to enter a passphrase for added security, or leave it blank for no passphrase. Press Enter to continue.
  - The key pair will be generated: `id_rsa` (private key) and `id_rsa.pub` (public key).
- **Configure the SSH server**: Configure the SSH server to allow key-based authentication using your generated public key. The configuration process may vary depending on the SSH server software you choose.
  - For Bitvise SSH Server (Windows):
  - Launch the Bitvise SSH Server Control Panel.
  - Click on the "Settings" button next to the profile labeled "Server".
  - In the "Host key management" section, click on the "Add" button.
  - Browse to the location where you saved the private key (id_rsa) and select it. Click "Open" to add the key.
  - In the "User accounts" section, click on the "Add" button.
  - Enter your desired username in the "Account name" field.
  - In the "Authentication" tab, select "Public key" from the "Allowed authentication methods" list.
  - Click on the "Import" button and browse to the location where you saved the public key (id_rsa.pub). Select it and click "Open" to import the key.
  - Click "OK" to save the configuration changes.
- For OpenSSH (macOS/Linux):
  - Open the SSH server configuration file using a text editor. The location of the file may vary, but it is typically found at /etc/ssh/sshd_config or /etc/sshd_config.
  - Find the line that starts with #PubkeyAuthentication and remove the leading # character to uncomment the line.
  - Find the line that starts with #AuthorizedKeysFile and remove the leading # character to uncomment the line.
  - Save the changes and exit the text editor.
  - Restart the SSH server to apply the configuration changes. The command to restart the SSH server varies depending on your operating system. For example, on Ubuntu, you can run: `sudo service ssh restart`.

- **Update the script with test environment details**: Modify the script to use the test environment details, including the hostname/IP address, SSH port, username, and path to your private key. Update the hostname, port, username, and private_key_path variables with the appropriate values for your test environment.
-** Create a test directory**: Create a directory on your local machine to simulate the remote directory where you want to transfer the ACH file. Update the remote_dir variable with the path to your test directory.
- **Run the script**: Run the script after making the necessary modifications. It will generate a sample ACH file (sample.ach) and transfer it to the specified remote directory on your local machine.
  - In the script you provided, update the hostname, port, username, and private_key_path variables with the appropriate values for your local SSH server configuration.
  - For example:
  ``` python
  hostname = "localhost"  # Use "localhost" if running the SSH server locally
  port = 22  # Default SSH port is 22
  username = "your_username"  # Set the username you configured on the SSH server
  private_key_path = "/path/to/your/private/key"  # Update with the path to your private key (e.g., "~/.ssh/id_rsa")


By setting up a local SSH server and configuring the script accordingly, you can test the ACH file transfer functionality without relying on the actual business application environments. You should have a local SSH server set up and configured for key-based authentication. You can proceed to run the script and test the ACH file transfer functionality.