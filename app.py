import os
import time
salvar_usuarios = []
salvar_senha = []

def opcao_invalida():
    print("\nAcho que você digitou algo errado :( ")
    input('Digite alguma tecla para voltar ao menu principal: ')
    main()


def opcoes():
    print("\nBem-vindo\n")
    print("1-Cadastrar")
    print("2-Log in")

def escolher_opcao():

    opcao_escolhida = int(input("\nDigite a opção desejada: ")) 

    if opcao_escolhida == 1:
        cadastrar()
    elif opcao_escolhida == 2:
        log_in()
    else:
       opcao_invalida()

def cadastrar():
    usuario_cadastro = input("Crie um nome de usuário: ")
    senha_cadastro = input("Crie uma senha: ")

    if usuario_cadastro in salvar_usuarios:
        print("O usuário já existe")
    else: 
        salvar_usuarios.append(usuario_cadastro)
        salvar_senha.append(senha_cadastro)

    print("Usuário Cadastrado com sucesso!")
    main()

def log_in():

    tentativas = 0
    limite_tentativas = 3
    timeout = 3

    def depois_de_logar():
                print("\n1-Ver perfil")
                print("2-sair\n")
                opcao_logIn = int(input("Selecione uma das opções: "))
                if opcao_logIn == 1:
                    print(f"\nO seu nome de usúario é {usuario_entrar}\n")
                elif opcao_logIn == 2:
                    os.system('cls')
                    print("\n Encerrando... \n")
                else:
                    print("Ops, acho que você digitou algo errado")


    while True:
        usuario_entrar = input("\nDigite seu nome de usario: ")
        senha_entrar = input("Digite seu senha: ")

        if usuario_entrar in salvar_usuarios:
            indice = salvar_usuarios.index(usuario_entrar)
            if salvar_senha[indice] == senha_entrar:
                print("Login realizado com sucesso!\n\n")
                depois_de_logar()
                input("Digite alguma tecla para voltar: ")
                depois_de_logar()
                break

            else:
                tentativas += 1
                print("\nAcho que vocé digitou a senha errada :( ")
                print(f"Essa foi a {tentativas} tentativa de 3\n")
        else:
            print("\nUsuário não encontrado :(")
        
        if tentativas == limite_tentativas:
            print("Número máximo de tentativas excedido. Acesso bloqueado.")
            time.sleep(timeout)
            os.system('cls')
            main()



def main():
    opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()



