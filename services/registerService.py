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