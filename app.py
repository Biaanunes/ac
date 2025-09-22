import os
import time

salvar_usuarios = []
salvar_senha = []

def opcao_invalida():
    print("\nAcho que você digitou algo errado :( ")
    input('Digite alguma tecla para voltar ao menu principal: ')
    main()

def opcoes():
    print("\nBem-vindo")
    print("1 - Cadastrar")
    print("2 - Log in")

def escolher_opcao():
    try:
        opcao_escolhida = int(input("\nDigite a opção desejada: ")) 
        if opcao_escolhida == 1:
            cadastrar()
        elif opcao_escolhida == 2:
            log_in()
        else:
            opcao_invalida()
    except ValueError:
        print("\nPor favor, insira um número válido.")
        escolher_opcao()

def cadastrar():
    usuario_cadastro = input("Crie um nome de usuário: ")
    senha_cadastro = input("Crie uma senha: ")

    if usuario_cadastro in salvar_usuarios:
        print("O usuário já existe")
    else: 
        salvar_usuarios.append(usuario_cadastro)
        salvar_senha.append(senha_cadastro)
        print("Usuário cadastrado com sucesso!")

    voltar_ao_menu()

def log_in():
    tentativas = 0
    limite_tentativas = 3

    while tentativas < limite_tentativas:
        usuario_entrar = input("\nDigite seu nome de usuário: ")
        senha_entrar = input("Digite sua senha: ")

        if usuario_entrar in salvar_usuarios:
            indice = salvar_usuarios.index(usuario_entrar)
            if salvar_senha[indice] == senha_entrar:
                print("Login realizado com sucesso!\n")
                depois_de_logar(usuario_entrar)
                return  
            else:
                tentativas += 1
                print(f"\nSenha incorreta! Tentativa {tentativas} de {limite_tentativas}.")
        else:
            print("\nUsuário não encontrado :(")
        
        if tentativas == limite_tentativas:
            print("Número máximo de tentativas excedido. Acesso bloqueado.")
            time.sleep(2)  
            voltar_ao_menu()

def depois_de_logar(usuario_entrar):
    while True:
        print("\n1 - Ver perfil")
        print("2 - Sair")
        opcao_logIn = input("Selecione uma das opções: ")

        if opcao_logIn == '1':
            print(f"\nO seu nome de usuário é {usuario_entrar}\n")
        elif opcao_logIn == '2':
            print("\nEncerrando...")
            time.sleep(1) 
            os.system('cls') 
            voltar_ao_menu() 
            break
        else:
            print("Opção Inválida")

def voltar_ao_menu():
    input('Pressione Enter para voltar ao menu principal:')
    os.system('cls') 
    main()

def main():
    os.system('cls') 
    opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
