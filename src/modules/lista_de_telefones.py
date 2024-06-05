import os

CAMINHO_ARQUIVO = 'src/telefones.txt'

def lista_de_telefones():
    lista_de_telefones = []
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, 'r') as arquivo:
            for linha in arquivo:
                lista_de_telefones.append(linha.strip('\n'))
        print('Lista de telefones criada com sucesso!\n')
    else:
        print('Arquivo de telefones não encontrado!\n')
    return lista_de_telefones
