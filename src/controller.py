import uvicorn
import mysql.connector
from fastapi import FastAPI
from dbConnection import DBConnection

db = DBConnection(host='localhost', user='root', password='132567', database='volatex_dev')
mysql = db.connect()
cursor = mysql.cursor()
app = FastAPI()

# USERS
@app.get('/get_users/')
def get_users():
    try:
        sql = "SELECT name, password FROM user"
        cursor.execute(sql)
        results = cursor.fetchall()
        users = [dict(zip(cursor.column_names, result)) for result in results]
        return users 
    except mysql.connector.Error as err:
        print(f"[DB]:     Erro ao buscar usuários: {err}")


@app.post('/save_user/')
def save_user(user: dict) -> str:
    try:
        sql = "INSERT INTO user (name, password) VALUES (%s, %s)"
        cursor.execute(sql, (user['name'], user['password']))
        mysql.commit()
        message = f"Usuário {user['name']} inserido com sucesso !!"
        return message
    except mysql.connector.Error as err:
        print(f"[DB]:     Erro ao salvar usuário: {err}")

# PRODUCTION
@app.get('/get_prod/')
def get_prod():
    try:
        sql = "SELECT numero_peca, tear, peso, fornecedor, produto, revisao, operador, `date` FROM production"
        cursor.execute(sql)
        results = cursor.fetchall()
        users = [dict(zip(cursor.column_names, result)) for result in results]
        return users 
    except mysql.connector.Error as err:
        print(f"[DB]:     Erro ao buscar peças: {err}")


@app.post('/save_prod/')
def save_prod(prod: dict) -> str:
    try:
        sql = "INSERT INTO production (numero_peça, tear, peso, fornecedor, produto, revisao, operador, `date`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (prod['numero_peça'], prod['tear'], prod['peso'], prod['fornecedor'], prod['produto'], prod['revisao'], prod['operador'], prod['date']))
        mysql.commit()
        message = f"Peça inserida com sucesso !!"
        return message
    except mysql.connector.Error as err:
        print(f"[DB]:     Erro ao salvar peça: {err}")


if __name__ == "__main__":
    uvicorn.run(app, port=8000)