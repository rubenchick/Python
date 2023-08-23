print('Yes')
import paramiko

# Параметры для подключения
sftp_host = "ansftp.infra.travel-dev.com"
sftp_port = 22
sftp_user = "anthony.ruby"
private_key_path = "/Users/rubenchik/GDrive/Languages/Python/Kivork/Improve skills/Basic/Key/sftp.txt"

# Подключаемся к серверу SFTP
private_key = paramiko.RSAKey(filename=private_key_path)
transport = paramiko.Transport((sftp_host, sftp_port))
transport.connect(username=sftp_user, pkey=private_key)

sftp = paramiko.SFTPClient.from_transport(transport)
#
# # Передаем файл
local_path = "/Users/rubenchik/GDrive/Languages/Python/Kivork/Improve skills/Basic/df.py"
remote_path = "df.py"
sftp.put(local_path, remote_path)

# Проверяем наличие файла на сервере

files_on_server = sftp.listdir("")
print(files_on_server)


# files_on_server = sftp.listdir("/path/on/server/")
# if "yourfile.csv" in files_on_server:
#     print("Файл успешно загружен на сервер!")
# else:
#     print("Ошибка! Файл не найден на сервере.")

# Закрываем соединение
sftp.close()
transport.close()