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
