--Produçao
CREATE TABLE volatex_dev.production (
	numero_peça varchar(100) NOT NULL,
	tear varchar(100) NOT NULL,
	peso FLOAT NOT NULL,
	fornecedor varchar(100) NOT NULL,
	produto varchar(100) NOT NULL,
	revisao varchar(100) NOT NULL,
	operador varchar(100) NOT NULL,
	`date` DATETIME NULL,
	id INT auto_increment NOT NULL,
	CONSTRAINT production_pk PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

-- Teares
CREATE TABLE volatex_dev.teares (
	id INT auto_increment NOT NULL,
	nome varchar(100) NOT NULL,
	modelo varchar(100) NOT NULL,
	created_at DATETIME NOT NULL,
	CONSTRAINT teares_pk PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

-- Fornecedores
CREATE TABLE volatex_dev.products_suppliers (
	id INT auto_increment NOT NULL,
	fornecedor varchar(100) NOT NULL,
	produto varchar(100) NOT NULL,
	created_at DATETIME NOT NULL,
	CONSTRAINT products_suppliers_pk PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

-- Operadores
CREATE TABLE volatex_dev.operators (
	id INT auto_increment NOT NULL,
	nome varchar(100) NOT NULL,
	cargo varchar(100) NOT NULL,
	created_at DATETIME NOT NULL,
	CONSTRAINT operators_pk PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;



