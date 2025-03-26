# Projeto 4 - Camada Física

Este projeto implementa uma comunicação entre cliente e servidor utilizando a camada física da computação. Ele simula a transmissão de dados, como imagens, dividindo-os em pacotes, enviando-os através de uma interface serial e garantindo a integridade dos dados com o uso de CRC16.

## Estrutura do Projeto

- **Cliente**: Responsável por enviar os dados para o servidor.
- **Servidor**: Recebe os dados enviados pelo cliente e valida sua integridade.
- **Camada de Enlace**: Implementa a lógica de envio e recepção de pacotes.
- **CRC16**: Garante a integridade dos dados transmitidos.

## Requisitos

- Python 3.6+
- Dependências listadas no arquivo `requirements.txt`.

## Como Executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o servidor:
   ```bash
   python codes_server/server.py
   ```

3. Execute o cliente:
   ```bash
   python codes_client/client.py
   ```

## Funcionalidades

- Divisão de dados em pacotes.
- Verificação de integridade com CRC16.
- Logs detalhados de envio e recepção.
- Tratamento de erros e retransmissão de pacotes.

## Estrutura de Arquivos

- `codes_client/`: Código do cliente.
- `codes_server/`: Código do servidor.
- `requirements.txt`: Dependências do projeto.