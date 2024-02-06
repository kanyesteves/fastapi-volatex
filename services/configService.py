import uuid
from firebase_admin import db


class ConfigService:

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

    def update_production(self, data: dict):
        db_productions = db.reference(f"db-volatex/production/{data['num_peça']}-{data['fornecedor']}-{data['produto']}")
        db_productions.set(data)
        return "Valor atualizado com sucesso"

    def update_tear(self, data: dict):
        db_teares = db.reference(f"db-volatex/teares/{data['nome']}")
        db_teares.set(data)
        return "Valor atualizado com sucesso"

    def update_operator(self, data: dict):
        db_operators = db.reference(f"db-volatex/operators/{data['nome']}")
        db_operators.set(data)
        return "Valor atualizado com sucesso"

    def update_products_supplier(self, data: dict):
        db_products_supplier = db.reference(f"db-volatex/products_supplier/{data['fornecedor']}-{data['produto']}")
        db_products_supplier.set(data)
        return "Valor atualizado com sucesso"

    def delete_production(self, data: dict):
        data['remove'] = True
        db_products_supplier = db.reference(f"db-volatex/production/{data['num_peça']}-{data['fornecedor']}-{data['produto']}")
        db_products_supplier.set(data)
        return "Peça removida com sucesso"

    def delete_tear(self, data: dict):
        data['remove'] = True
        db_teares = db.reference(f"db-volatex/teares/{data['nome']}")
        db_teares.set(data)
        return "Tear removido com sucesso"

    def delete_operator(self, data: dict):
        data['remove'] = True
        db_operators = db.reference(f"db-volatex/operators/{data['nome']}")
        db_operators.set(data)
        return "Operador removido com sucesso"

    def delete_products_supplier(self, data: dict):
        data['remove'] = True
        db_products_supplier = db.reference(f"db-volatex/products_supplier/{data['fornecedor']}-{data['produto']}")
        db_products_supplier.set(data)
        return "Fornecedor removido com sucesso"