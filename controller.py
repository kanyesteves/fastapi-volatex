import uvicorn
import mysql.connector
from fastapi import FastAPI
from dbConnection import DBConnection
from services.graphsService import GraphsService
from services.registerService import RegisterService
from services.exportService import ExportService
from services.configService import ConfigService

db = DBConnection(host='localhost', user='root', password='132567', database='volatex_dev')
mysql = db.connect()
cursor = mysql.cursor()

app = FastAPI()
graphsService = GraphsService(mysql)
registerService = RegisterService(mysql)
exportService = ExportService(mysql)
configService = ConfigService(mysql)



page_login = "login"
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


##### GRAPHS
page_graphs = "graphs"
@app.get(f'/{page_graphs}/get_production/')
def get_production():
    return graphsService.get_production()

@app.get(f'/{page_graphs}/get_tear/')
def get_tear():
    return registerService.get_tear()

@app.get(f'/{page_graphs}/get_products_suppliers/')
def get_products_supplier():
    return registerService.get_products_supplier()


##### REGISTER
page_register = "register"
@app.get(f'/{page_register}/get_production/')
def get_production():
    return registerService.get_production()

@app.get(f'/{page_register}/get_tear/')
def get_tear():
    return registerService.get_tear()

@app.get(f'/{page_register}/get_products_suppliers/')
def get_products_supplier():
    return registerService.get_products_supplier()

@app.post(f'/{page_register}/save_production/')
def save_production(data: dict):
    return registerService.save_production(data)


##### EXPORT
page_eport = "export"
@app.get(f'/{page_eport}/get_production/')
def get_production():
    return exportService.get_production()

@app.get(f'/{page_eport}/get_products_suppliers/')
def get_products_supplier():
    return exportService.get_products_supplier()


##### CONFIG
page_config = "config"
@app.get(f'/{page_config}/get_production/')
def get_production():
    return configService.get_production()

@app.get(f'/{page_config}/get_tear/')
def get_tear():
    return configService.get_tear()

@app.get(f'/{page_config}/get_products_suppliers/')
def get_products_supplier():
    return configService.get_products_supplier()

@app.get(f'/{page_config}/get_operators/')
def get_operator():
    return configService.get_operator()

@app.post(f'/{page_config}/save_tear/')
def save_tear(data: dict):
    return configService.save_tear(data)

@app.post(f'/{page_config}/save_operator/')
def save_operator(data: dict):
    return configService.save_operator(data)

@app.post(f'/{page_config}/save_products_supplier/')
def save_products_supplier(data: dict):
    return configService.save_product_supplier(data)

@app.put(f'/{page_config}/update_production/')
def update_production(data: dict):
    return configService.update_production(data)

@app.put(f'/{page_config}/update_tear/')
def update_tear(data: dict):
    return configService.update_tear(data)

@app.put(f'/{page_config}/update_operator/')
def update_operator(data: dict):
    return configService.update_operator(data)

@app.put(f'/{page_config}/update_products_supplier/')
def update_products_supplier(data: dict):
    return configService.update_products_supplier(data)

@app.delete(f'/{page_config}/delete_production/')
def delete_production(data: dict):
    return configService.delete_production(data)

@app.delete(f'/{page_config}/delete_tear/')
def delete_tear(data: dict):
    return configService.delete_tear(data)

@app.delete(f'/{page_config}/delete_operator/')
def delete_operator(data: dict):
    return configService.delete_operator(data)

@app.delete(f'/{page_config}/delete_products_supplier/')
def delete_products_supplier(data: dict):
    return configService.delete_products_supplier(data)


if __name__ == "__main__":
    uvicorn.run(app, port=8000)