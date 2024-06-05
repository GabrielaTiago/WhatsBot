import pyperclip
import pyautogui
import webbrowser

from pyautogui import ImageNotFoundException

from modules.temporizadores import aguarda_login, pausa_curta, pausa_entre_mensagens, carregamento_curto, carregamento_medio, carregamento_conversas

LINK = 'https://api.whatsapp.com/send?phone='
MENSAGEM = 'Oiie! Tudo bem? Estou fazendo um robô pra WhatsApp 🤖\nSe você está recebendo essa mensagem é porque funfou 😂😅'

def abre_whatsapp(telefone: str):
    print('Abrindo o WhatsApp Web para o número ' + telefone + '📱')
    webbrowser.open_new(LINK + telefone)
    carregamento_medio() # Espera carregar o WhatsApp Web

def permite_links_whatsapp_popup():
    print('Procurando popup de permissão de links no WhatsApp Web 🗃️')
    try:
        x, y = pyautogui.locateCenterOnScreen('src/assets/quadradinho.png')
        print('Caixa de seleção popup encontrada. Clicando na opção "Sempre permitir"')
        pyautogui.click(x, y, duration=1.5)
        if x and y:
            x, y = pyautogui.locateCenterOnScreen('src/assets/abrir_url.png')
            print('Botão "Abrir URL" encontrado. Clicando no botão "Abrir URL"\n')
            pyautogui.click(x, y, duration=1.2)
    except ImageNotFoundException:
        print('Popup não foi encontrado!\n')

def iniciar_conversa():
    pausa_curta()
    print('Iniciando conversa 📨')
    try:
        x, y = pyautogui.locateCenterOnScreen('src/assets/btn_iniciar_conversa.png')
        pyautogui.click(x, y, duration=1.5)
    except ImageNotFoundException:
        print('Botão de iniciar conversa não encontrado!\n')

def seleciona_whatsapp_web():
    pausa_curta()
    print('\nSelecionando WhatsApp Web 📱🌐')
    try:
        x, y = pyautogui.locateCenterOnScreen('src/assets/btn_whats_web.png')
        pyautogui.click(x, y, duration=1.5)
    except ImageNotFoundException:
        print('Botão para utliizar WhatsApp Web não encontrado!\n')

def verifica_login(esta_logado: bool, primeira_vez: bool):
    print('\nVerificando se o login foi efetuado 🪪')
    if esta_logado:
        print('Usuário já está logado! 🪪\n')
        return
    if primeira_vez:
        carregamento_medio() # Espera carregar o QR Code
    try:
        if pyautogui.locateCenterOnScreen('src/assets/ponta_qr_code.png'):
            print('QR Code encontrado. Por favor, faça o login no WhatsApp Web 📱')
            aguarda_login()
            verifica_login(esta_logado=False, primeira_vez=False)
    except ImageNotFoundException:
        print('Login efetuado com sucesso! 🚀\n')


def verifica_carregamento_conversas():
    print('Verificando se as conversas foram carregadas 📨')
    try:
        if pyautogui.locateCenterOnScreen('src/assets/carregando_conversas.png'):
            print('Conversas ainda não foram carregadas!')
            carregamento_conversas()
            verifica_carregamento_conversas()
    except ImageNotFoundException:
        print('Conversas carregadas com sucesso! 🗒️\n')

def verifica_modal_iniciando_conversa():
    carregamento_medio()
    print('Verificando se o modal de iniciar conversa está aberto 📨')
    try:
        iniciando_conversa = pyautogui.locateCenterOnScreen('src/assets/iniciando_conversa.png')
        btn_cancelar = pyautogui.locateCenterOnScreen('src/assets/btn_cancelar.png')
        if iniciando_conversa or btn_cancelar:
            verifica_modal_iniciando_conversa()
    except ImageNotFoundException:
        pass

def copia_mensagem(mensagem: str):
    pyperclip.copy(mensagem) # pyperclip utilizado para textos com acentuação
    pyautogui.hotkey('ctrl', 'v')
    pausa_curta()
    pyautogui.press('enter')

def envia_mensagem( mensagem: str):
    print('Enviando mensagem  📨')
    copia_mensagem(mensagem)
    print('Mensagem enviada com sucesso! 🚀')

def envia_mensagem_para_lista_de_tefones(telefones: list):
    if not telefones:
        print('Nenhum telefone encontrado na lista! 😢\n')
        return

    for telefone in telefones:
        abre_whatsapp(telefone)
        permite_links_whatsapp_popup()
        iniciar_conversa()
        seleciona_whatsapp_web()
        verifica_login(esta_logado=False, primeira_vez=True)
        verifica_carregamento_conversas()
        verifica_modal_iniciando_conversa()
        envia_mensagem(MENSAGEM)
        pausa_entre_mensagens()
    print('\nTodas as mensagens foram enviadas com sucesso! 🚀🚀🚀')