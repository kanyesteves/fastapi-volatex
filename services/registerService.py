import uuid
from firebase_admin import db


class RegisterService:

    def get_production(self):
        db_productions = db.reference("db-volatex/production/")
        productions = db_productions.get()
        return productions 

    def get_products_supplier(self):
        db_products_supplier = db.reference("db-volatex/products_supplier/")
        products_suppliers = db_products_supplier.get()
        return products_suppliers 

    def get_tear(self):
        db_teares = db.reference("db-volatex/teares/")
        teares = db_teares.get()
        return teares 

    def get_operator(self):
        db_operators = db.reference("db-volatex/operators/")
        operators = db_operators.get() 
        return operators
    
    def save_production(self, data: dict):
        db_productions = db.reference(f"db-volatex/production/{data['num_peça']}-{data['fornecedor']}-{data['produto']}")
        db_productions.set(data)
        return "Peça inserida com sucesso !!"

    def save_tear(self, data: dict):
        db_teares = db.reference(f"db-volatex/teares/{data['nome']}")
        db_teares.set(data)
        return "Tear inserida com sucesso !!"

    def save_operator(self, data: dict):
        db_operators = db.reference(f"db-volatex/operators/{data['nome']}")
        db_operators.set(data)
        return "Operador inserido com sucesso !!"

    def save_product_supplier(self, data: dict):
        db_products_supplier = db.reference(f"db-volatex/products_supplier/{data['fornecedor']}-{data['produto']}")
        db_products_supplier.set(data)
        return "Fornecedor inserido com sucesso !!"