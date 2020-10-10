import Alfredo
import inspect

def inicio():
    '''Apresenta programa'''

    Alfredo.linguinha()
    print('Olá esse aqui é o Alfredo. \n ')



def menu():

    resposta = input('Escolha entre, feliz, assustado, triste, linguinha, dormindo, sexy, dinheiro ou apaixonado. \n Escreva "sair" para terminar \n')
    return resposta.lower()

if __name__ == '__main__':
    inicio()
    opcao = menu()

    while (opcao != "sair"):

        if(opcao == 'feliz'):
            Alfredo.feliz()
        elif(opcao == 'assustado'):
            Alfredo.assustado()
        elif(opcao == 'triste'):
            Alfredo.triste()
        elif(opcao == 'linguinha'):
            print('VC ESCOLHEU O MAIS BRABO')
            Alfredo.linguinha()
        elif(opcao == 'dormindo'):
            Alfredo.dormindo()
        elif(opcao == 'sexy'):
            Alfredo.sexy()
        elif(opcao == 'dinheiro'):
            Alfredo.dinheiro()
        elif(opcao == 'apaixonado'):
            Alfredo.apaixonado()

        opcao = menu()




