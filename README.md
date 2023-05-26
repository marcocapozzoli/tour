# Tour Api

## 💻 Projeto

Essa é uma aplicação de controle de cadastro de funcionários onde é permitido cadastrar, visualizar, editar e inativar, funcionários, departamentos e empresas

## 🚀 Ferramentas

Essas foram as principais tecnologias utilizadas:
- Python 3.11
- Django 4.2.1
- Django Rest Framework 3.14.0
- Pydantic 1.10.8
- Poetry 1.4.2
- Docker 

O banco de dados dessa aplicação foi o `PostgreSQL`.

## Instalação


**1. Clone esse repositório**

```
git clone git@github.com:marcocapozzoli/tour.git
```

**2. Preparando o ambiente**

Obs: Tenha o Docker e o Docker-compose instalados e de preferencia o `make` também.

Utilizei o docker para simplificar a execução do código. Então se você tem as ferramenta `make` e o `docker` instalados em sua maquina, bastar está na raiz do projeto e rodar o seguinte comando

```
make all
```

Caso você não tenha o make mas tenha o `docker` e `docker-compose` basta rodar o comando abaixo:

```
docker-compose up -d
```

Isso vai criar todo o ambiente, instalar todas as dependencias, rodar as migrações no banco e levandar o servidor. Com isso a aplicação já estara pronta.


## Execução

Após rodar os comandos acima a aplicação estará disponível em [http://localhost:8000](http://localhost:8000).

**1. Gerando um token**

Após o servidor estiver rodando é necessário criar um superusuário para acessar os endpoints. Caso tenha o `make` execute

```
make create-superuser
```

Caso não tenha o `make` e esteja com o `docker` execute

```
docker exec -it tour python src/infra/manage.py createsuperuser
```

Para acessar qualquer endpoint é necessário está logado e para isso para fazer uma requisição para o endpoint abaixo passando as credenciais `username` e `password` e com isso utilizar o `access` para acessar os endpoints

### Requisição

POST /api/token/

```json
{
  "username": "consultant",
  "password": "password"
}
```
### Exemplo de resposta:

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NTE0Nzk4NiwiaWF0IjoxNjg1MDYxNTg2LCJqdGkiOiJhMmVhYjc1NGRlNTE0YmRkOThiMTVhNzYwNWRkMGRlNSIsInVzZXJfaWQiOjJ9.07nMfXU9twVvsc_rFnFxgucH7sFmU9fFvBhBZc9UIqQ",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1MDYxODg2LCJpYXQiOjE2ODUwNjE1ODYsImp0aSI6IjkxYWRkZWQxN2JhYTQxYTQ5NmIzZTdjMjM0NjYwNjEyIiwidXNlcl9pZCI6Mn0.lN6nDIvSXhNRlhz4iYXBrvmO8ZtugcW6z2DIG0wuIiA"
}
```

**2. Endpoints - Empresa**

1. Criar Empresa

### Requisição

POST /api/v1/company/create

```json
{
  "street": "Street",
  "city": "City",
  "country": "Brazil",
  "cnpj": "91352128000170"
}
```
### Exemplo de resposta:

```json
{
  "success": true,
  "error": null,
  "data": {
    "street": "Street",
    "city": "City",
    "country": "Brazil",
    "cnpj": "91352128000170",
    "is_active": true,
    "id": "617971c2-264e-4c9b-8b3b-e7abdca45f2e",
    "updated_at": "2023-05-26T00:28:10.289884Z",
    "created_at": "2023-05-26T00:28:10.289862Z"
  }
}
```

2. Detalhar Empresa

### Requisição

GET /api/v1/company/detail/:id

### Exemplo de resposta:

```json
{
  "success": true,
  "error": null,
  "data": {
    "street": "Street",
    "city": "City",
    "country": "Brazil",
    "cnpj": "91352128000170",
    "is_active": true,
    "id": "617971c2-264e-4c9b-8b3b-e7abdca45f2e",
    "updated_at": "2023-05-26T00:28:10.289884Z",
    "created_at": "2023-05-26T00:28:10.289862Z"
  }
}
```

3. Atualizar Empresa

É possível editar apenas um campo

### Requisição

PATCH /api/v1/company/detail/:id

```json
{
  "country": "Brazil Update",
}
```
### Exemplo de resposta:

```json
{
  "success": true,
  "error": null,
  "data": {
    "street": "Street",
    "city": "City",
    "country": "Brazil Update",
    "cnpj": "91352128000170",
    "is_active": true,
    "id": "617971c2-264e-4c9b-8b3b-e7abdca45f2e",
    "updated_at": "2023-05-26T00:56:51.252917Z",
    "created_at": "2023-05-26T00:28:10.289862Z"
  }
}
```

4. Inativar Empresa

### Requisição

PATCH /api/v1/company/detail/:id 

```json
{
  "is_active": false,
}
```
### Exemplo de resposta:

```json
{
  "success": true,
  "error": null,
  "data": {
    "street": "Street",
    "city": "City",
    "country": "Brazil Update",
    "cnpj": "91352128000170",
    "is_active": false,
    "id": "617971c2-264e-4c9b-8b3b-e7abdca45f2e",
    "updated_at": "2023-05-26T00:59:18.932195Z",
    "created_at": "2023-05-26T00:28:10.289862Z"
  }
}
```

5. Listar Empresas

Na listagem está permitidos filtar por pais e cidade com as keys `country` e `city`

## Requisição

GET /api/v1/company/list

## Exemplo de resposta

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "617971c2-264e-4c9b-8b3b-e7abdca45f2e",
      "is_active": false,
      "created_at": "2023-05-26T00:28:10.289862Z",
      "updated_at": "2023-05-26T00:59:18.932195Z",
      "cnpj": "91352128000170",
      "street": "Street",
      "city": "City",
      "country": "Brazil Update"
    },
    {
      "id": "2c2d5c48-3f88-4aeb-9d62-c22940ef7ee2",
      "is_active": true,
      "created_at": "2023-05-26T01:02:54.220146Z",
      "updated_at": "2023-05-26T01:02:54.220164Z",
      "cnpj": "08212804000166",
      "street": "Street 2",
      "city": "City 2",
      "country": "Brazil"
  }
  ]
}
```

**3. Endpoints - Departamento**

1. Criar Departamento

### Requisição

POST /api/v1/department/create

```json
{
  "name": "Name",
  "cost_center": "0001",
  "integration_code": "12A",
  "company": "2c2d5c48-3f88-4aeb-9d62-c22940ef7ee2"
}
```
### Exemplo de resposta:

```json
{
  "success": true,
  "error": null,
  "data": {
    "name": "Name",
    "cost_center": "0001",
    "integration_code": "12A",
    "company": "2c2d5c48-3f88-4aeb-9d62-c22940ef7ee2",
    "is_active": true,
    "id": "d997065c-f453-41c7-8e63-bbc8a8033402",
    "updated_at": "2023-05-26T01:13:49.797518Z",
    "created_at": "2023-05-26T01:13:49.797505Z"
  }
}
```

2. Detalhar Departamento

### Requisição

GET /api/v1/department/detail/:id 

### Exemplo de resposta:

```json
{
  "success": true,
  "error": null,
  "data": {
    "name": "Name",
    "cost_center": "0001",
    "integration_code": "12A",
    "company": "2c2d5c48-3f88-4aeb-9d62-c22940ef7ee2",
    "is_active": true,
    "id": "d997065c-f453-41c7-8e63-bbc8a8033402",
    "updated_at": "2023-05-26T01:13:49.797518Z",
    "created_at": "2023-05-26T01:13:49.797505Z"
  }
}
```

3. Atualizar Departamento

É possível editar apenas um campo

### Requisição

PATCH /api/v1/department/update/:id 

```json
{
  "cost_center": "1254"
}
```
### Exemplo de resposta:

```json
{
  "success": true,
  "error": null,
  "data": {
    "name": "Name",
    "cost_center": "1254",
    "integration_code": "12A",
    "company": "2c2d5c48-3f88-4aeb-9d62-c22940ef7ee2",
    "is_active": true,
    "id": "d997065c-f453-41c7-8e63-bbc8a8033402",
    "updated_at": "2023-05-26T01:15:55.979908Z",
    "created_at": "2023-05-26T01:13:49.797505Z"
  }
}
```

4. Inativar Departamento

### Requisição

PATCH /api/v1/department/update/:id 

```json
{
  "is_active": false,
}
```
### Exemplo de resposta:

```json
{
  "success": true,
  "error": null,
  "data": {
    "name": "Name",
    "cost_center": "1254",
    "integration_code": "12A",
    "company": "2c2d5c48-3f88-4aeb-9d62-c22940ef7ee2",
    "is_active": false,
    "id": "d997065c-f453-41c7-8e63-bbc8a8033402",
    "updated_at": "2023-05-26T01:17:01.698239Z",
    "created_at": "2023-05-26T01:13:49.797505Z"
  }
}
```

5. Listar Departamentos

Na listagem está permitidos filtar por empresa com a key `company`

## Requisição

GET /api/v1/department/list

## Exemplo de resposta

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "d997065c-f453-41c7-8e63-bbc8a8033402",
      "is_active": false,
      "created_at": "2023-05-26T01:13:49.797505Z",
      "updated_at": "2023-05-26T01:17:01.698239Z",
      "name": "Name",
      "cost_center": "1254",
      "integration_code": "12A",
      "company": "2c2d5c48-3f88-4aeb-9d62-c22940ef7ee2"
    },
    {
      "id": "f9da0b15-f62f-4b27-b2f5-fc81bf3bf388",
      "is_active": true,
      "created_at": "2023-05-26T01:17:58.558319Z",
      "updated_at": "2023-05-26T01:17:58.558332Z",
      "name": "Name 2",
      "cost_center": "123",
      "integration_code": "12A",
      "company": "2c2d5c48-3f88-4aeb-9d62-c22940ef7ee2"
    }
  ]
}
```


**3. Endpoints - Funcionários**

1. Criar Funcionário

### Requisição

POST /api/v1/employee/create

```json
{
  "full_name": "Full name",
  "email": "teste@mail.com",
  "phone": "81999999999",
  "birthday": "24/06/1990",
  "entry_date": "10/10/2016",
  "departure_date": "01/01/2010",
  "city": "City",
  "department": "d997065c-f453-41c7-8e63-bbc8a8033402"
}
```

### Exemplo de resposta:

```json
{
  "success": true,
  "error": null,
  "data": {
    "full_name": "Full name",
    "email": "teste@mail.com",
    "phone": "81998956167",
    "birthday": "1990-06-24",
    "entry_date": "2016-10-10",
    "departure_date": "2010-01-01",
    "city": "City",
    "department": "d997065c-f453-41c7-8e63-bbc8a8033402",
    "is_active": true,
    "id": "1a189469-8066-4fbb-974c-66aba53cc4d2",
    "updated_at": "2023-05-26T01:20:36.270397Z",
    "created_at": "2023-05-26T01:20:36.270373Z"
  }
}
```

2. Detalhar Funcionário

### Requisição

GET /api/v1/employee/detail/:id 

### Exemplo de resposta:

```json
{
  "success": true,
  "error": null,
  "data": {
    "full_name": "Full name",
    "email": "teste@mail.com",
    "phone": "81998956167",
    "birthday": "1990-06-24",
    "entry_date": "2016-10-10",
    "departure_date": "2010-01-01",
    "city": "City",
    "department": "d997065c-f453-41c7-8e63-bbc8a8033402",
    "is_active": true,
    "id": "1a189469-8066-4fbb-974c-66aba53cc4d2",
    "updated_at": "2023-05-26T01:20:36.270397Z",
    "created_at": "2023-05-26T01:20:36.270373Z"
  }
}
```

3. Atualizar Funcionário

É possível editar apenas um campo

### Requisição

PATCH /api/v1/employee/update/:id

```json
{
  "phone": "11999885544"
}
```
### Exemplo de resposta:

```json
{
  "success": true,
  "error": null,
  "data": {
    "full_name": "Full name",
    "email": "teste@mail.com",
    "phone": "11999885544",
    "birthday": "1990-06-24",
    "entry_date": "2016-10-10",
    "departure_date": "2010-01-01",
    "city": "City",
    "department": "d997065c-f453-41c7-8e63-bbc8a8033402",
    "is_active": true,
    "id": "1a189469-8066-4fbb-974c-66aba53cc4d2",
    "updated_at": "2023-05-26T01:25:00.970614Z",
    "created_at": "2023-05-26T01:20:36.270373Z"
  }
}
```

4. Inativar Funcionário

### Requisição

PATCH /api/v1/employee/update/:id 

```json
{
  "is_active": false,
}
```
### Exemplo de resposta:

```json
{
  "success": true,
  "error": null,
  "data": {
    "full_name": "Full name",
    "email": "teste@mail.com",
    "phone": "11999885544",
    "birthday": "1990-06-24",
    "entry_date": "2016-10-10",
    "departure_date": "2010-01-01",
    "city": "City",
    "department": "d997065c-f453-41c7-8e63-bbc8a8033402",
    "is_active": false,
    "id": "1a189469-8066-4fbb-974c-66aba53cc4d2",
    "updated_at": "2023-05-26T01:26:14.797503Z",
    "created_at": "2023-05-26T01:20:36.270373Z"
  }
}
```

5. Listar Funcionários

Na listagem está permitidos filtar por cidade, empresa e departamento, com as keys `city` `company` `department__company`

## Requisição

GET /api/v1/employee/list?department=:id&department__company=:id&city=City

## Exemplo de resposta

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "b6175d45-f5c0-41cb-a774-4ae2503acd26",
      "is_active": true,
      "created_at": "2023-05-26T01:27:26.894417Z",
      "updated_at": "2023-05-26T01:27:26.894439Z",
      "full_name": "Full name 3",
      "email": "teste3@mail.com",
      "phone": "11999885544",
      "birthday": "1990-06-24",
      "entry_date": "2016-10-10",
      "departure_date": "2010-01-01",
      "city": "City",
      "department": "f9da0b15-f62f-4b27-b2f5-fc81bf3bf388"
    }
  ]
}
```

## Testes

Você pode rodar os teste e vê a cobertura rodando com o comando

```
make test-cov
```

Caso não tenha o make pode rodar o comando


```
docker exec -it tour coverage run src/infra/manage.py test -v 2 && docker exec -it tour coverage report
```
