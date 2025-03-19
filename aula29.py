def exibir_menu():
    print("bem-vindo ao menu de cadastro")
    print("1 - novo cadastro")
    print("2 - ver cadastro")
    print("3 - sair")
    print("-----------------------------------------------------------")

def cadastrar_pessoa(cadastros):
    nome = input("nome:")
    idade = input("idade:")
    turma = input("turma:")
    curso = input("curso:")
    cadastros.append({"nome": nome, "idade": idade, "turma": turma, "curso": curso})
    print("Cadastro realizado com sucesso!")

def ver_cadastros (cadastros):
    if not cadastros:
        print("Nenhum cadastro no sistema. ")
    else:
        print("\n ------ LISTA DE CADASTROS ------")   

        for i, pessoa in enumerate (cadastros, 1):
            print(f"{i}. Nome: {pessoa ['nome']}", Idade:
{pessoa ['Idade']}, Turma: {pessoa ['Turma']}, Curso: {pessoa}']}")'
                
def main():
    cadastro = []
    while True:
        exibir_menu()
        opção = input("ecolha uma opção: ")
        if opção == "1":
            cadastrar_pessoa (cadastros)
        elif opção == "2":
            ver_cadastros (cadastros)
        elif opção == "3":
            print("obrigado por utilizar nosso sistema")
            break
            
        