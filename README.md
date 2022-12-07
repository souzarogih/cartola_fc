<p align="center">
    Microserviço em Django desenvolvido na imersão full stack full cycle da Code Education.
</p>

### Comandos para execução do docker
`$ docker-compose up -d`
`$ docker-compose down`

### Execução da aplicação
`python manage.py runserver 0.0.0.0:8000`

### Acessar a URL de admin
http://localhost:8000/admin/login/?next=/admin/

### Django admin
Username: admin@user
Email: admin@user.com
Password: admin

### Instalação de bibliotecas
`$ pipenv install django`
`$ pip install django`
`$ pip install django-environ`
`$ pipenv install django-environ`
`$ pipenv install dj-database-url`


### Comandos básicos para linux

#### Atualizar repositórios
`$ sudo apt update`

#### Instalação do pip
`$ sudo apt install pipenv`
`$ sudo apt install python3-pip`
`$ sudo apt install python3-django`

#### Ativar o virtual env
pipenv shell

### Executar as migração do django
python manage.py migrate


### Criar um módulo django
django-admin startapp app

### Transcrever para banco de dados
`python manage.py makemigrations`

### Executar a migração
`python manage.py migrate`

### Alterando as permissões
chmod +x .docker/start.dev.sh

### Gerar um JSON com todos os dados do banco de dados
python manage.py dumpdata app

### Carregar os dados 
`python manage.py loaddata initial_data`