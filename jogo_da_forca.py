import time
from random import choice
from time import sleep
import pygame
import os
def forca(chances):
    print("  _______     ")
    print(" |/      |    ")

    if chances == 5:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if chances == 4:
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |            ")

    if chances == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |       |    ")
        print(" |            ")

    if chances == 2:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if chances == 1:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if chances == 0:
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
# criar arquivos .txt para colocar as listas
with open('frutas.txt', encoding='utf-8') as lista:
    frutas = lista.read()
    frutas = frutas.split('\n')
with open('cores.txt', encoding='utf-8') as lista:
    cores = lista.read()
    cores = cores.split('\n')
with open('animais.txt', encoding='utf-8') as lista:
    animais = lista.read()
    animais = animais.split('\n')
with open('alfabeto.txt', encoding='utf-8') as lista:
    alfabeto = lista.read()
c = 1 #escolha de novo round
cat = 0 #escolha da categoria
corretas = []
erradas = []
digitadas = []
chances = 6
print('>' * 20, 'UNIESP'.center(10), '<' * 20)
print('#'.ljust(10), 'INTRODUÇÃO À PROGRAMAÇÃO'.center(30), '#'.rjust(10))
print('#'.ljust(10), ' '.center(30), '#'.rjust(10))
print('#'.ljust(3), 'Grupo:'.ljust(10), '#'.rjust(37))
print('#'.ljust(3), 'Anna Cordeiro - 2022210220021@iesp.edu.br', '#'.rjust(6))
print('#'.ljust(3), 'Ítalo Ricardo - 2022210220029@iesp.edu.br', '#'.rjust(6))
print('#'.ljust(3), 'Jânio Milanês - 2022211510089@iesp.edu.br', '#'.rjust(6))
print('#'.ljust(3), 'João Henrique - 2022210220015@iesp.edu.br', '#'.rjust(6))
print('#'.ljust(3), 'Roberto Maia - 2022210220022@iesp.edu.br', '#'.rjust(7))
print('#'.ljust(3), 'Ryan Urtiga - 2022210220017@iesp.edu.br', '#'.rjust(8))
print('#'.ljust(10), ' '.center(30), '#'.rjust(10))
print('#'.ljust(10), ' '.center(30), '#'.rjust(10))
while c != 0:
    print('#'.ljust(3), 'Escolha a categoria que você deseja jogar: ', '#'.rjust(4))
    print('#'.ljust(3), '[1] FRUTAS', '#'.rjust(37))
    print('#'.ljust(3), '[2] CORES', '#'.rjust(38))
    print('#'.ljust(3), '[3] ANIMAIS', '#'.rjust(36))
    print('#'.ljust(3), '[0] SAIR', '#'.rjust(39))
    print('#' * 52)
    print(' ')
    cat = int(input('Digite o número referente a categoria que você deseja: '))
    while cat != 1 and cat != 2 and cat != 3 and cat != 0:
        print('Por favor, digite um valor válido. \n '
              'Escolha a categoria que você deseja jogar: \n'
              '[1] FRUTAS \n'
              '[2] CORES \n'
              '[3] ANIMAIS \n'
              '[0] SAIR \n')
        cat = int(input('Qual categoria você escolheu? '))
    if cat == 0:
        print('PROGRAMA ENCERRADO')
        break
    elif cat == 1:
        categoria = 'FRUTAS'
        p = choice(frutas) #escolher palavra aleatória da lista
        p = list(p) #separar as letras
        print(p)
    elif cat == 2:
        categoria = 'CORES'
        p = choice(cores)
        p = list(p)
        print(p)
    elif cat == 3:
        categoria = 'ANIMAIS'
        p = choice(animais)
        p = list(p)
        print(p)
    print('INICIANDO...')
    sleep(1)
    print('A PALAVRA É: ')
    while chances > 0:
        forca(chances)
        for letra in p:
            if letra in corretas:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print(' ')
        print('\033[32m'+'Corretas: '+'\033[0;0m', ', '.join(corretas))
        print('\033[31m'+'Erradas: '+'\033[0;0m', ', '.join(erradas))
        sugestao = str(input('Que letra você acha que a palavra possui? \n PALPITE: ')).strip().upper()
        while sugestao == '':
            print('Você deixou o palpite em branco!')
            sugestao = str(input('Que letra você acha que a palavra possui? \n PALPITE: ')).strip().upper()
        while sugestao in digitadas:
            print('Você já digitou essa letra! Por favor, tente novamente.')
            sugestao = str(input('Que letra você acha que a palavra possui? \n PALPITE: ')).strip().upper()
        while sugestao not in alfabeto:
            print('Por favor, digite uma LETRA!')
            sugestao = str(input('Que letra você acha que a palavra possui? \n PALPITE: ')).strip().upper()
        while len(sugestao) > 1:
            print('Isso não é uma letra! Digite novamente')
            sugestao = str(input('Que letra você acha que a palavra possui? \n PALPITE: ')).strip().upper()
        for palavra in p:
            if sugestao in p:
                print('\033[32m'+'VOCÊ ACERTOU UMA LETRA!'+'\033[0;0m')
                pygame.init()
                pygame.mixer.music.load('acertou letra.mp3')
                pygame.mixer.music.play()
                corretas.append(sugestao)
                digitadas.append(sugestao)
                break
            else:
                chances = chances - 1
                if chances == 0:
                    forca(chances)
                    break
                print('\033[31m'+'VOCÊ ERROU UMA LETRA :(  TENTE NOVAMENTE'+'\033[0;0m')
                pygame.init()
                pygame.mixer.music.load('errou letra.mp3')
                pygame.mixer.music.play()
                digitadas.append(sugestao)
                erradas.append(sugestao)
                break
        time.sleep(1.2)
        os.system('cls')
        if chances == 0:
            pygame.init()
            pygame.mixer.music.load('perdeu rodada.mp3')
            pygame.mixer.music.play()
            print('\033[33m'+'VOCÊ PERDEU! A PALAVRA ERA {}'.format(''.join(p))+'\033[0;0m')
            print("    _______________         ")
            print("   /               \       ")
            print("  /                 \      ")
            print("//                   \/\  ")
            print("\|   XXXX     XXXX   | /   ")
            print(" |   XXXX     XXXX   |/     ")
            print(" |   XXX       XXX   |      ")
            print(" |                   |      ")
            print(" \__      XXX      __/     ")
            print("   |\     XXX     /|       ")
            print("   | |           | |        ")
            print("   | I I I I I I I |        ")
            print("   |  I I I I I I  |        ")
            print("   \_             _/       ")
            print("     \_         _/         ")
            print("       \_______/           ")
            break
        if set(p).issubset(set(digitadas)):
            pygame.init()
            pygame.mixer.music.load('ganhou rodada.mp3')
            pygame.mixer.music.play()
            print('\033[34m'+'PARABÉNS! VOCÊ GANHOU!')
            print("       ___________      ")
            print("      '._==_==_=_.'     ")
            print("      .-\\:      /-.    ")
            print("     | (|:.     |) |    ")
            print("      '-|:.     |-'     ")
            print("        \\::.    /      ")
            print("         '::. .'        ")
            print("           ) (          ")
            print("         _.' '._        ")
            print("        '-------'       " +'\033[0;0m')
            break
    c = int(input('Deseja iniciar uma nova rodada? Digite [1] SIM ou [0] NÃO \n'))
    while c != 1 and c != 0:
        print('Por favor, digite 1 [SIM] ou 0 [NÃO] \n')
        c = int(input('Deseja iniciar uma nova rodada? \n'))
    if c == 0:
        print('PROGRAMA ENCERRADO')
        break
    if c == 1:
        corretas = []
        erradas = []
        digitadas = []
        chances = 6
