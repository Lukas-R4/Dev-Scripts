print ("******Sistema de cadastro******\n")

dicio = {}

def cabecalho():
    print("***O que você deseja fazer? ***")
    print("1- Cadastrar Pessoa \n2- Consultar Pessoa \n3- Sair")
   
def operacoes():
    while True:
        cabecalho()
        op = int(input("\nOpção: "))
        if op == 1:

            pessoa = {}
            ent = input("Nome: ")

            pessoa["Idade"] = int(input("Idade: "))
            pessoa["Cidade"] = input("Cidade: ")

            dicio[ent] = pessoa

            
        elif op == 2:
            consulta = input("Informe o Nome da pessoa: ")
            print(dicio[consulta])
            
        elif (op > 3) or (op == 0):
            print("Opção inválida!")
            operacoes()
            return

        if op == 3:
            print("\nEncerrando...")
            break

operacoes()
