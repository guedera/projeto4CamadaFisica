import crcmod

# Criando a função CRC-16-CCITT (polinômio 0x1021)
crc16 = crcmod.predefined.Crc('crc-16')

# Dados a serem transmitidos
dados = b"Mensagem de teste"

# Calculando o checksum CRC-16
crc16.update(dados)
checksum_bytes = crc16.digest()  # Retorna os 2 bytes diretamente

print(f"Checksum CRC-16 (bytes): {checksum_bytes.hex().upper()}")  # Representação hexadecimal
print(f"Bytes individuais: {checksum_bytes[0]:02X} {checksum_bytes[1]:02X}")  # Bytes separados
