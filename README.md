# Back-End (API)

Documentação da API feita para ser usada como Back-End do sistema de controle para produção da empresa Volatex

### FrameWork Python usada:
- [FastAPI](https://fastapi.tiangolo.com/)

### Endpoints:
1. **GET**
    - /get_users/
    - /graphs/get_production/
    - /graphs/get_tear/
    - /graphs/get_products_supplier/
    - /register/get_production/
    - /register/get_tear/
    - /register/get_products_supplier/
    - /export/get_production/
    - /export/get_products_supplier/
    - /config/get_production/
    - /config/get_tear/
    - /config/get_products_supplier/
    - /config/get_operators/
2. **POST**
    - /register/save_production/
    - /config/save_tear/
    - /config/save_operator/
    - /config/save_products_supplier/
3. **PUT**
    - /config/update_production/
    - /config/update_tear/
    - /config/update_operator/
    - /config/update_products_supplier/
4. **DELETE**
    - /config/delete_production/
    - /config/delete_tear/
    - /config/delete_operator/
    - /config/delete_products_supplier/