from livro import Livro
from biblioteca import Biblioteca

biblioteca = Biblioteca()

# Criando e adicionando livros
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899, "123456789")
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "987654321")
livro3 = Livro("A Arte da Guerra", "Sun Tzu", -500, "456789123")  # ano negativo para obras antigas

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Listando livros
print("📚 Lista de Livros:")
biblioteca.listar_livros()

# Buscando livro
print("\n🔍 Buscando por 'senhor':")
biblioteca.buscar_por_titulo("senhor")

# Removendo livro
print("\n❌ Removendo livro com ISBN 987654321")
biblioteca.remover_livro_por_isbn("987654321")

# Lista atualizada
print("\n📚 Lista atualizada:")
biblioteca.listar_livros()
