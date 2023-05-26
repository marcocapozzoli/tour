# Tour Api

## 💻 Projeto

Essa é uma aplicação de controle de cadastro de funcionários onde é permitido cadastrar, visualizar, editar e inativar, funcionários, departamentos e empresas

Below Screenshot from the browsable API:
![image](/readme_img/main_screen1.png?raw=true "Main_Screen")

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
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

**2. Preparando o ambiente**

Utilizei o docker para simplificar a execução do código. Então se você tem as ferramenta `make` e o `docker` instalados em sua maquina, bastar está na raiz do projeto e rodar o seguinte comando

```
make all
```

Caso você não tenha o make mas tenha o `docker` e `docker-compose` basta rodar o comando abaixo:

```
docker-compose up. 
```

Isso vai criar todo o ambiente, instalar todas as dependencias, rodar as migrações no banco e levandar o servidor. Com isso a aplicação já estara pronta.

## Execução

Após rodar os comandos acima a aplicação estará disponível em [http://localhost:8000](http://localhost:8000).

**1. Gerando um token**

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
  }"
}
```

2. Detalhar Empresa

### Requisição

GET /api/v1/company/detail/617971c2-264e-4c9b-8b3b-e7abdca45f2e 

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
  }"
}
```

3. Atualizar Empresa

É possível editar apenas um campo da empresa

### Requisição

PATCH /api/v1/company/detail/617971c2-264e-4c9b-8b3b-e7abdca45f2e 

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

PATCH /api/v1/company/detail/617971c2-264e-4c9b-8b3b-e7abdca45f2e 

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
  }"
}
```

2. Detalhar Departamento

### Requisição

GET /api/v1/deapartment/detail/617971c2-264e-4c9b-8b3b-e7abdca45f2e 

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
  }"
}
```

3. Atualizar Departamento

É possível editar apenas um campo da empresa

### Requisição

PATCH /api/v1/deapartment/detail/617971c2-264e-4c9b-8b3b-e7abdca45f2e 

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

4. Inativar Departamento

### Requisição

PATCH /api/v1/deapartment/detail/617971c2-264e-4c9b-8b3b-e7abdca45f2e 

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

5. Listar Departamentos

## Requisição

GET /api/v1/deapartment/list

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



## Endpoints and Features

- Autenticação de administrador
  - `(POST)/api/token`
- Criar Empresa
  - `(POST) /api/buy/`
- Detalhar empresa
  - `(GET) /api/buy/`
- Inativar empresa
  - `(PATCH) /api/buy/{id}/`
- Listar empresas
  - `(GET) /api/buy/{id}/`
- 
  - `(PATCH) /api/buy/{id}/`
- Delete an specific buy
  - `(DELETE) /api/buy/{id}/`

👀 For more information about endpoints, see the documentation on endpoint `(GET)/api/doc/`

## 📎 Versioning

1.0.0.0

## 🧔 Authors

* **Marco Capozzoli**: @marcocapozzoli (https://github.com/marcocapozzoli)

## 📚 Referências
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django](https://www.djangoproject.com/)
- [Swagger](https://drf-yasg.readthedocs.io/en/stable/)