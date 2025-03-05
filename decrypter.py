import os
import pyaes

## abrir o arquivo criptografado
file_name = "teste.txt.ransomwaretroll"
try:
    file = open(file_name, "rb")
    file_data = file.read()
except:
    print("Arquivo não encontrado")
    exit(1)
finally:
    file.close()

## chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo descriptografado
new_file = "teste.txt"
try:
    file = open(new_file, "rb")
    new_file.write(decrypt_data)
except:
    print("Erro ao criar o arquivo descriptografado")
    exit(1)
finally:
    new_file.close()
