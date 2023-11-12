from ftplib import FTP

# FTP server details
FTP_HOST = "xxx"
FTP_USER = "xxx"
FTP_PASS = "xxx"
directory_name = "ruby"
# Connect to the FTP server
ftp = FTP(FTP_HOST, FTP_USER, FTP_PASS)

# List the files in the current directory

ftp.dir()

# Create a new directory
# try:
#     ftp.mkd(directory_name)
#     print(f"Directory '{directory_name}' created successfully.")
# except Exception as e:
#     print(f"An error occurred: {e}")


#
# Define the filename to be downloaded and the local filename where it will be saved
# remote_filename = '/Users/rubenchik/GDrive2/Languages/Python/Kivork/Improve skills/Basic/df.py'
# local_filename = 'downloaded_file.txt'

#
# # Download a file
# with open(local_filename, 'wb') as local_file:
#     ftp.retrbinary(f'RETR {remote_filename}', local_file.write)
#
# print(f'{remote_filename} has been downloaded and saved as {local_filename} in the local directory.')
#
# # Define the filename to be uploaded and the path to the local file
local_file_to_upload = '/Users/rubenchik/GDrive2/Languages/Python/Kivork/Improve skills/Basic/df.py'
remote_filename = 'df.py'
#
#
# Upload a file
with open(local_file_to_upload, 'rb') as file_to_upload:
    ftp.storbinary(f'STOR {remote_filename}', file_to_upload)

print(f'{local_file_to_upload} has been uploaded as {remote_filename} to the FTP server.')
print(ftp.dir())

# The name of the file you want to create
# filename = "example.txt"
# # The content you want to write in the file
# file_content = "Hello, this is a test file."

# # Create a file and write content to it
# try:
#     # Open a file in write mode in binary
#     with open(filename, 'wb') as file:
#         # Write the content to the file
#         file.write(file_content.encode())
#
#     # Open the file in read mode in binary and upload it to FTP
#     with open(filename, 'rb') as file:
#         ftp.storbinary(f'STOR {filename}', file)
#
#     print(f"File '{filename}' created and uploaded successfully.")
#
# except Exception as e:
#     print(f"An error occurred: {e}")


# Close the FTP connection
ftp.quit()
