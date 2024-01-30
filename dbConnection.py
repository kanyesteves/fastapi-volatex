import mysql.connector

class DBConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("[DB]:     Conexão estabelecida com sucesso !!")
            return self.connection
        except mysql.connector.Error as er:
            print(f"[DB]:     Erro ao se conectar com o Mysql {er}")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("[DB]:     Conexão ao Mysql encerrada.")
