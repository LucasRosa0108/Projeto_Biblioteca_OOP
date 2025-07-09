from livro import Livro
from biblioteca import Biblioteca

biblioteca = Biblioteca()

def menu():
    print("\n🔧 Menu Biblioteca")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Buscar livro por título")
    print("4. Remover livro por ISBN")
    print("5. Atualizar livro por ISBN")
    print("6. Sair")

def criar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano: "))
    isbn = input("ISBN: ")
    livro = Livro(titulo, autor, ano, isbn)
    biblioteca.adicionar_livro(livro)
    print("✅ Livro adicionado!")

def atualizar_livro():
    isbn = input("ISBN do livro a atualizar: ")
    encontrado = False
    for livro in biblioteca.livros:
        if livro.isbn == isbn:
            print(f"Livro encontrado: {livro}")
            novo_titulo = input("Novo título: ")
            novo_autor = input("Novo autor: ")
            novo_ano = int(input("Novo ano: "))
            livro.titulo = novo_titulo
            livro.autor = novo_autor
            livro.ano = novo_ano
            print("✅ Livro atualizado!")
            encontrado = True
            break
    if not encontrado:
        print("❌ Livro com ISBN não encontrado.")

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        criar_livro()
    elif escolha == "2":
        print("\n📚 Lista de Livros:")
        biblioteca.listar_livros()
    elif escolha == "3":
        termo = input("Digite parte do título: ")
        biblioteca.buscar_por_titulo(termo)
    elif escolha == "4":
        isbn = input("ISBN do livro a remover: ")
        biblioteca.remover_livro_por_isbn(isbn)
        print("✅ Livro removido (se encontrado).")
    elif escolha == "5":
        atualizar_livro()
    elif escolha == "6":
        print("📕 Encerrando programa. Até mais!")
        break
    else:
        print("❌ Opção inválida. Tente novamente.")
