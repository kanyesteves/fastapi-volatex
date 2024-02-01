import mysql.connector


class ConfigService:
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

    def get_operator(self):
        try:
            sql = "SELECT id, nome, cargo, created_at FROM operators"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            operators = [dict(zip(self.cursor.column_names, result)) for result in results]
            return operators 
        except mysql.connector.Error as err:
            print(f"[DB]:     Erro ao buscar teares: {err}")

    def save_tear(self, data: dict):
        try:
            sql = "INSERT INTO teares (nome, modelo, created_at) VALUES(%s, %s, %s)"
            self.cursor.execute(sql, (data['nome'], data['modelo'], data['created_at']))
            self.mysql.commit()
            message = f"Tear inserida com sucesso !!"
            return message
        except mysql.connector.Error as err:
            print(f"[DB]:     Erro ao salvar tear: {err}")

    def save_operator(self, data: dict):
        try:
            sql = "INSERT INTO operators (nome, cargo, created_at) VALUES(%s, %s, %s)"
            self.cursor.execute(sql, (data['nome'], data['cargo'], data['created_at']))
            self.mysql.commit()
            message = f"Operador inserido com sucesso !!"
            return message
        except mysql.connector.Error as err:
            print(f"[DB]:     Erro ao salvar operador: {err}")

    def save_product_supplier(self, data: dict):
        try:
            sql = "INSERT INTO products_suppliers (fornecedor, produto, created_at) VALUES(%s, %s, %s)"
            self.cursor.execute(sql, (data['fornecedor'], data['produto'], data['created_at']))
            self.mysql.commit()
            message = f"Fornecedor inserido com sucesso !!"
            return message
        except mysql.connector.Error as err:
            print(f"[DB]:     Erro ao salvar fornecedor: {err}")

    def update_production(self, data: dict):
        try:
            sql = f"UPDATE production SET {data['column_name']} = %s WHERE id = %s"
            self.cursor.execute(sql, (data['data']['value'], data['data']['id_peça']))
            self.mysql.commit()
            message = f"Valor atualizado com sucesso !!"
            return message
        except mysql.connector.Error as err:
            print(f"[DB]:     Erro ao atualizar a tabela: {err}")

    def update_tear(self, data: dict):
        try:
            sql = f"UPDATE teares SET {data['column_name']} = %s WHERE id = %s"
            self.cursor.execute(sql, (data['data']['value'], data['data']['id_tear']))
            self.mysql.commit()
            message = f"Valor atualizado com sucesso !!"
            return message
        except mysql.connector.Error as err:
            print(f"[DB]:     Erro ao atualizar a tabela: {err}")

    def update_operator(self, data: dict):
        try:
            sql = f"UPDATE operators SET {data['column_name']} = %s WHERE id = %s"
            self.cursor.execute(sql, (data['data']['value'], data['data']['id_tear']))
            self.mysql.commit()
            message = f"Valor atualizado com sucesso !!"
            return message
        except mysql.connector.Error as err:
            print(f"[DB]:     Erro ao atualizar a tabela: {err}")

    def update_products_supplier(self, data: dict):
        try:
            sql = f"UPDATE products_suppliers SET {data['column_name']} = %s WHERE id = %s"
            self.cursor.execute(sql, (data['data']['value'], data['data']['id_tear']))
            self.mysql.commit()
            message = f"Valor atualizado com sucesso !!"
            return message
        except mysql.connector.Error as err:
            print(f"[DB]:     Erro ao atualizar a tabela: {err}")

    def delete_production(self, data: dict):
        try:
            sql = f"DELETE FROM production WHERE numero_peça = %s"
            self.cursor.execute(sql, (data["numero_peça"],))
            self.mysql.commit()
            message = f"Valor removido com sucesso !!"
            return message
        except mysql.connector.Error as err:
            print(f"[DB]:     Erro ao removido valor da tabela: {err}")

    def delete_tear(self, data: dict):
        try:
            sql = f"DELETE FROM teares WHERE id = %s"
            self.cursor.execute(sql, (data["id_tear"],))
            self.mysql.commit()
            message = f"Valor removido com sucesso !!"
            return message
        except mysql.connector.Error as err:
            print(f"[DB]:     Erro ao removido valor da tabela: {err}")

    def delete_operator(self, data: dict):
        try:
            sql = f"DELETE FROM operators WHERE id = %s"
            self.cursor.execute(sql, (data["id_operator"],))
            self.mysql.commit()
            message = f"Valor removido com sucesso !!"
            return message
        except mysql.connector.Error as err:
            print(f"[DB]:     Erro ao removido valor da tabela: {err}")

    def delete_products_supplier(self, data: dict):
        try:
            sql = f"DELETE FROM products_suppliers WHERE id = %s"
            self.cursor.execute(sql, (data["id_products_supplier"],))
            self.mysql.commit()
            message = f"Valor removido com sucesso !!"
            return message
        except mysql.connector.Error as err:
            print(f"[DB]:     Erro ao removido valor da tabela: {err}")