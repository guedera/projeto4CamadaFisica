import datetime
import binascii

def log_message(action, message_type, message_size, packet_num=None, total_packets=None, crc=None):
    """
    Registra uma linha no arquivo de log
    action: 'envio' ou 'receb'
    message_type: tipo da mensagem (1-6)
    message_size: tamanho em bytes
    packet_num: número do pacote (opcional)
    total_packets: total de pacotes (opcional)
    crc: valor CRC em hexadecimal (opcional)
    """
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")[:-3]
    
    # Formata a linha do log de acordo com o tipo de mensagem
    if packet_num is not None and total_packets is not None and crc is not None:
        log_line = f"{timestamp} / {action} / {message_type} / {message_size} / {packet_num} / {total_packets} / {crc}"
    else:
        log_line = f"{timestamp} / {action} / {message_type} / {message_size}"
    
    # Caminho correto para o arquivo de log do servidor
    log_path = "/home/guedera/Documents/Aulas/Camadas/projeto4CamadaFisica/codes_server/server_log.txt"
    
    # Escreve no arquivo de log
    with open(log_path, "a") as log_file:
        log_file.write(log_line + "\n")
    
    return log_line

def initialize_log():
    """
    Inicializa ou limpa o arquivo de log do servidor
    """
    log_path = "/home/guedera/Documents/Aulas/Camadas/projeto4CamadaFisica/codes_server/server_log.txt"
    with open(log_path, "w") as log_file:
        log_file.write("Timestamp / Ação / Tipo / Tamanho / Pacote / Total / CRC\n")
