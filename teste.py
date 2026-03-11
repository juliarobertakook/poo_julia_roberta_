from abc import ABC, abstractmethod

class Livro:
    def __init__(self, isbn, titulo, autor, disponivel=True):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def emprestar(self):
        if not self.disponivel:
            raise Exception("Livro já está emprestado.")
        self.disponivel = False

    def devolver(self):
        self.disponivel = True


class Usuario(ABC):
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.lista_livros_emprestados = []

    @abstractmethod
    def pegar_emprestado(self, livro):
        pass

    @abstractmethod
    def devolver_livro(self, livro):
        pass


class Aluno(Usuario):
    limite = 3

    def pegar_emprestado(self, livro):
        if len(self.lista_livros_emprestados) >= Aluno.limite:
            raise Exception("Aluno atingiu o limite de livros.")
        
        livro.emprestar()
        self.lista_livros_emprestados.append(livro)

    def devolver_livro(self, livro):
        if livro in self.lista_livros_emprestados:
            livro.devolver()
            self.lista_livros_emprestados.remove(livro)


class Professor(Usuario):
    limite = 5

    def pegar_emprestado(self, livro):
        if len(self.lista_livros_emprestados) >= Professor.limite:
            raise Exception("Professor atingiu o limite de livros.")
        
        livro.emprestar()
        self.lista_livros_emprestados.append(livro)

    def devolver_livro(self, livro):
        if livro in self.lista_livros_emprestados:
            livro.devolver()
            self.lista_livros_emprestados.remove(livro)


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def consultar_livros_emprestados(self):
        for usuario in self.usuarios:
            print("Usuário:", usuario.nome)
            for livro in usuario.lista_livros_emprestados:
                print(" -", livro.titulo)

livro1 = Livro("LIV001", "Titulo 1", "Autor 1")
livro2 = Livro("LIV002", "Titulo 2", "Autor 2")
livro3 = Livro("LIV003", "Titulo 3", "Autor 3")

aluno1 = Aluno("ALUNOXX1", "Nome 1")
prof1 = Professor("PROFXX1", "Professor 1")

biblioteca = Biblioteca()

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.adicionar_usuario(aluno1)
biblioteca.adicionar_usuario(prof1)

aluno1.pegar_emprestado(livro1)
prof1.pegar_emprestado(livro2)

biblioteca.consultar_livros_emprestados()