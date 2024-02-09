import uvicorn
import firebase_admin
from fastapi import FastAPI
from firebase_admin import credentials
from services.registerService import RegisterService

if not firebase_admin._apps:
    cred = credentials.Certificate("db-volatex-realtime-firebase-adminsdk.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://db-volatex-realtime-default-rtdb.firebaseio.com/'
})


app = FastAPI()
registerService = RegisterService()


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

@app.post(f'/{page_register}/save_tear/')
def save_tear(data: dict):
    return registerService.save_tear(data)

@app.post(f'/{page_register}/save_operator/')
def save_operator(data: dict):
    return registerService.save_operator(data)

@app.post(f'/{page_register}/save_products_supplier/')
def save_products_supplier(data: dict):
    return registerService.save_product_supplier(data)


if __name__ == "__main__":
    uvicorn.run(app, port=8000)