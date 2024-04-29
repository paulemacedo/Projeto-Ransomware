import os
import pyaes

file_name = 'flag.txt.paule'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

#chave
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

#remove arquivo
os.remove(file_name)

#decrypt
new_file = 'flag.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()