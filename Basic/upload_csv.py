print('Yes')
import paramiko

# create ssh client
ssh_client = paramiko.SSHClient()

# remote server credentials
host = "eu-central-1.sftpcloud.io"
username = "fc973e0102244f768b0235b6e89f5c13"
password = "3ZUBX71RfV0mmXmenI52OjcWVxoJd2jZ"
port = 22

#######
### test connections
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,port=port,username=username,password=password)

print('connection established successfully')

ssh_client.close()
##########
##### Test 2. Info about files

sh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,port=port,username=username,password=password)

ftp = ssh_client.open_sftp()
files = ftp.listdir()

print("Listing all the files and Directory: ", files)

# close the connection
ftp.close()
ssh_client.close()

##### Test 3. Upload


# create ssh client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,port=port,username=username,password=password)

# create an SFTP client object
ftp = ssh_client.open_sftp()

# download a file from the remote server
files = ftp.put("/Users/rubenchik/GDrive/Languages/Python/Kivork/Improve skills/Basic/dict.py", "dict.py")

# close the connection
ftp.close()
ssh_client.close()