# Back-End (API)

Documentação da API feita para ser usada como Back-End do sistema de controle para produção da empresa Volatex


### Como rodar:

- **Passo 1:** Crie um ambiente virtual para rodar o projeto.

        python3 -m venv apiFast && source apiFast/bin/activate

- **Passo 2:** Atualize o pip

        pip install --upgrade pip

- **Passo 3:** Baixe o repositório do projeto na sua máquina.

        git clone git@github.com:kanyesteves/fastapi-volatex.git

- **Passo 4:** Instale as dependências para rodar o projeto

        pip install -r requirements.txt

- **Passo 5:** Rode o comando para usar a API

        uvicorn controller:app --reload

### Endpoints:

Para acessar a documentação dos endpoints, acesse

        http://127.0.0.1:8000/docs

![ENDPOINTS](https://github.com/kanyesteves/fastapi-volatex/blob/master/ENDPOINTS.png)