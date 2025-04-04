    import json

    arquivo_cadastros = "cadastros.json"

    def exibir_menu():
        print("\ ---- MENU CADASTRO ----")
        print("1 - Cadastrar Pessoa")
        print("2 - Ver cadastros")
        print("-------------------------")

    def salvar_cadastros (cadastros):
        with open (arquivo_cadastros, "w", encoding="uft-8") as arquivo:
            json.dump(cadastros, arquivo, indent=4, ensure_ascii=false)


    def carregar_cadastros():
        try: 
            with open (arquivo_cadastros, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
            except(FileNotFoundError, json.JSONDecodeError):
                return[]

def cadastrar_pessoa(cadastros):
    nome = imput("Nome: ")
    idade = imput("Idade: ")
    turma = imput("Turma: ")
    curso = imput("Curso: ")
    cadastros.aprend({"Nome": nome, "Idade": idade, "Turma": turma, "Curso": curso})
    salvar_cadastros(cadastros)
    print("Cadastro realizado com sucesso!")
    

