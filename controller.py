import uvicorn
import firebase_admin
from fastapi import FastAPI
from firebase_admin import credentials
from services.userService import UserService
from services.graphsService import GraphsService
from services.registerService import RegisterService
from services.exportService import ExportService
from services.configService import ConfigService

if not firebase_admin._apps:
    cred = credentials.Certificate("db-volatex-realtime-firebase-adminsdk.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://db-volatex-realtime-default-rtdb.firebaseio.com/'
})


app = FastAPI()
userService = UserService()
graphsService = GraphsService()
registerService = RegisterService()
exportService = ExportService()
configService = ConfigService()

##### USERS
page_users = "users"
@app.get(f'/{page_users}/get_users/')
def get_users():
    return userService.get_users()

@app.post(f'/{page_users}/save_user/')
def save_user(data: dict):
    return userService.save_user(data)


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


# ##### REGISTER
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

@app.get(f'/{page_register}/get_operators/')
def get_operator():
    return registerService.get_operator()

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


# ##### CONFIG
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