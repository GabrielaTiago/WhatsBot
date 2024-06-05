from datetime import datetime
from time import sleep

def hora_atual():
    return datetime.now().strftime('%H:%M')

def msg_carregando():
    print('Carregando... ⏲️')

def pausa_entre_mensagens():
    print(f'Nova mensagem em 5 minutos - {hora_atual()} ⏲️\n')
    sleep(300)

def aguarda_login():
    print(f'Aguardando 3 minutos para efetuar o login - {hora_atual()} ⏲️')
    sleep(180)

def pausa_curta():
    sleep(1.25)

def carregamento_curto():
    msg_carregando()
    sleep(3)

def carregamento_medio():
    msg_carregando()
    sleep(10)

def carregamento_conversas():
    print('Aguardando 1 minuto para completar o carregamento das conversas e mensagens ⏲️')
    sleep(60)