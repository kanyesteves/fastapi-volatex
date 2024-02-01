import mysql.connector


class GraphsService:
    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = mysql.cursor()

    def get_production(self):
        try:
            sql = "SELECT id, numero_peça, tear, peso, fornecedor, produto, revisao, operador, `date` FROM production"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            productions = [dict(zip(self.cursor.column_names, result)) for result in results]
            return productions 
        except mysql.connector.Error as err:
            print(f"[DB]:     Erro ao buscar peças: {err}")

    def get_products_supplier(self):
        try:
            sql = "SELECT id, fornecedor, produto, created_at FROM products_suppliers"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            products_suppliers = [dict(zip(self.cursor.column_names, result)) for result in results]
            return products_suppliers 
        except mysql.connector.Error as err:
            print(f"[DB]:     Erro ao buscar fornecedores: {err}")

    def get_tear(self):
        try:
            sql = "SELECT id, nome, modelo, created_at FROM teares"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            teares = [dict(zip(self.cursor.column_names, result)) for result in results]
            return teares 
        except mysql.connector.Error as err:
            print(f"[DB]:     Erro ao buscar teares: {err}")