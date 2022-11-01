import os
import sys


def jogar_novamente():
    
    print("Quer jogar novamente?\n1- Sim\n2- Não")
    novamente = int(input().strip())
    if(novamente == 1):
        print("Jogando Forca")
        jogar()
    elif(novamente == 2):
        print("Fim de Jogo")
        sys.exit(0)
       
def jogar():
    desafiante = input("Insira o nome do desafiante: ")
    competidor = input("Insira o nome do competidor: ")
    os.system("cls")

    palavra = str(input("Insira a palavra que será usada: "))
    dica1 = str(input("Insira a primeira dica da palavra escolhida: "))
    dica2 = str(input("Insira a segunda dica da palvra escolhida: "))
    dica3 = str(input("Insira a ultima dica da palavra escolhida: "))
    os.system("cls")

    arquivo = open('historico.txt', 'w')

    lista_palavra = []

    print(len(palavra),("Letras"))
    palavraSelecionada = len(palavra)

    for i in range(palavraSelecionada):
        lista_palavra.append('_')
    
    arquivo.close()

    digitadas = []
    acertos = []
    dica = 0
    erros = 0

    while True:
        senha = ''
        for letra in palavra:
            senha += letra if letra in acertos else '*'
        print(senha)
   
        if senha == palavra:
            print("<3")
            break
    
        print("1- Chutar letra")
        print("2- Pedir dica")
        op = input()
        if op == "1":
            print()
        elif op == "2":
            if dica == 0:
                print("dica 1: " + dica1)
                dica += 1
            
            elif dica == 1:
                print("dica 2: " + dica2)
                dica += 1
          
            elif dica == 2:
                print("dica 3: " + dica3)
                dica += 1 
            
            else:
                print("Você já solicitou todas as dicas do jogo!")
                dica += 1

        tentativa = input("Digite uma letra: ").lower().strip()       
    
        if tentativa in digitadas:
            print("você já tentou esta letra!")
            continue
        else:
            digitadas += tentativa
            if tentativa in palavra:
                    acertos += tentativa
            else:
                erros += 1
                print("você errou")
            print("X==:==\nX  :  ")
            print("X  O  " if erros >= 1 else "X")
            linha2 = ''
            if erros == 2:
                linha2 =  " | "
            elif erros == 3:
                linha2 = " /|  "
            elif erros >= 4:
                linha2 = " /|\ "
            print(f'X{linha2}')
            linha3 = ''
            if erros == 5:
                linha3 += " /   "
            elif erros >= 6:
                linha3 += " / \ "
            print(f"X{linha3}")
            print("X\n==========")
            if erros == 6:
                print("Enforcado!")
                print(f"a palavra secreta era: {palavra}")
                break
                  
    if erros == 6:
        vencedor = desafiante
    elif senha == palavra:
        vencedor = competidor
                    
    
    try:
        arquivo = open("historico.txt","r")
        conteudo = arquivo.readlines()
        arquivo.close()

    except:
        arquivo = open("historico.txt","w")
        arquivo.close()
    conteudo.append(palavra+"-")
    conteudo.append(vencedor+"\n")
    arquivo = open("historico.txt","w")
    arquivo.write(''.join(conteudo))
    arquivo.close()
    jogar_novamente()
jogar()     