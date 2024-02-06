from firebase_admin import db

class ExportService:

    def get_production(self):
        db_productions = db.reference("db-volatex/production/")
        productions = db_productions.get()
        return productions 

    def get_products_supplier(self):
        db_products_supplier = db.reference("db-volatex/products_supplier/")
        products_suppliers = db_products_supplier.get()
        return products_suppliers 