def interpreta_head(head:bytes) -> tuple :
    l =[]
    for b in head:
        l.append(b)
    return tuple(l)

def verifica_erro(h0,h3,h4,h5,h6,h7,pl,n):         
    erro = ''
    verifica = 'Verificado'

    if h3 != len(pl):
        erro += f'erro no tamanho do payload enviado!! esperado: {len(pl)} Recebido: {h3} \n'
    
    if h4 != n:
        erro += f'erro na sequencia. Esperado: {n}. Recebido: {h4} \n'

    #caso dê algum erro, entra nessa função
    if erro:
        erro += f'O pacote que deve ser solicitado é o pacote de número {h6} \n'
        erro += f'O ultimo pacote recebido foi o {h7} \n'

    #h1 quantidade de pacotes.

    return erro if erro else verifica


def verifica_dadosEoP(EoP:bytes):
    # \xAA\xBB\xCC
    aviso = True
    a = EoP[0]
    b = EoP[1]
    c =EoP[2]

    if a == '\xAA' and b == '\xBB' and c =='\xCC':
        return aviso
    
    return not aviso 

def verifica_tipo(h0,h1):
    if h0 == 1 : 
        # significa que a mensagem é do tipo 1 
        # ou seja terei os dados da qtd de pkcts enviados no total
        total_pkcts = h1
        return 'Tipo1',total_pkcts
    

def altera_byte(head:bytes, tipo, numero_pckt_recebido:int=None):
    head[0] = tipo
    if tipo == 4:
        head[1] = numero_pckt_recebido.to_bytes('big')

    return head


def verifica_pacote(pl,npckt,contador):
    return npckt == contador #and pl == ????
