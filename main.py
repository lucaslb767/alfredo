import Alfredo
import inspect

def inicio():
    '''Apresenta programa'''

    Alfredo.linguinha()
    print('Olá esse aqui é o Alfredo. \n ')



def menu():

    resposta = input('Escolha entre, feliz, assustado, triste, linguinha. \n Escreva "sair" para terminar')
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

        opcao = menu()




