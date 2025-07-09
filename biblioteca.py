from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro_por_isbn(self, isbn):
        self.livros = [livro for livro in self.livros if livro.isbn != isbn]

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
        for livro in self.livros:
            print(livro)

    def buscar_por_titulo(self, termo):
        encontrados = [livro for livro in self.livros if termo.lower() in livro.titulo.lower()]
        if not encontrados:
            print(f"Nenhum livro encontrado com o termo '{termo}'")
        for livro in encontrados:
            print(livro)
