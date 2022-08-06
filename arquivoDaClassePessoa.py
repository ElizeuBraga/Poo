import sqlite3
connection = sqlite3.connect('bancodedados.db')
cursor = connection.cursor();

class classePessoa():
    def __init__(self, nome, sexualidade):
        self.__nome = nome
        self.__sexualidade = sexualidade

    def criarTabela(self):
        sql = """
            CREATE TABLE IF NOT EXISTS pessoas(
                nome TEXT,
                sexualidade TEXT
            );
        """

        cursor.execute(sql)

        print("Tabela criada com sucesso!")

    def salvarNoBanco(self):
        sql = "INSERT INTO pessoas(nome, sexualidade)VALUES(?, ?)"
        cursor.execute(sql, [self.__nome, self.__sexualidade])
        connection.commit()

        print("Pessoa inserida com sucesso!")

    def buscarTodasAsPessoas(self):
        sql = "SELECT * FROM pessoas"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print(resultado)