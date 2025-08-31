# djflow_saas

Projeto do Curso de Django, implementação de multitenant / multitenancy com subdominio e schemas postgresql.

# Requisitos e Atualização:

Esse projeto foi usado como exemplo de uma implementação de django-tenant-schemas que não é mais atualizado, a biblioteca django-tenant-schemas somente foi compativel até o Django 5.1.8 e deve ser instalado nessa mesma versão caso queira testar sem maiores bug.

Eu realizei uma melhoria no codigo original do projeto para conseguir dar continuidade no curso, pois estava muito desatualizado em versão do python e django.

Abaixo a lista de versões que devem ser levado em consideração para rodar o projeto.

- Python 3.13.5
- Django==5.1.8
- django-tenant-schemas==1.12.0
- pillow==11.3.0
- psycopg2==2.9.10

# Instalação

Ao baixar o projeto, encontraremos um arquivo chamado "requirements.txt" que contém todas as dependências do Python para executar o projeto.

Executamos o seguinte:

    [kiubtech]$ pip install -r requirements.txt


# Configuração.

Crie uma cópia do arquivo "settings.example.json" com o nome "settings.json".

Feito isso, você precisará configurar as informações de credenciais do seu banco de dados.

    "DB": {
        "default": {
          "ENGINE": "django.db.backends.postgresql_psycopg2",
          "HOST": "localhost",
          "NAME": "djflow",
          "USER": "admin",
          "PASSWORD": "admin",
          "PORT": 5432
        }
      }


E também suas credenciais de envio de e-mail.

    "EMAIL": {
        "EMAIL_USE_TLS": true,
        "EMAIL_HOST": "smtp.gmail.com",
        "EMAIL_PORT": 587,
        "EMAIL_BACKEND": "django.core.mail.backends.smtp.EmailBackend",
        "EMAIL_HOST_USER": "my-mail@gmail.com",
        "EMAIL_HOST_PASSWORD": "**************",
        "DEFAULT_FROM_EMAIL": "my-mail@gmail.com",
        "CONTACT_EMAIL": "my-mail@gmail.com"
      }

# Iniciando banco de dados e projeto.

Executamos as migrações para criar o banco de dados:

    [kiubtech]$ python manage.py migrate


e então geramos nosso superusuário.

    [kiubtech]$ python manage.py createsuperuser


Pronto! Isso deve ser tudo o que você precisa para executar o projeto nos seus computadores locais:

    [kiubtech]$ python manage.py runserver


O comando migrate_schemas --shared faz com que os aplicativos seja compartilhados schema public. Observação: seu banco de dados deve estar vazio se esta for a primeira vez que você executa este comando EXECUTAR APENAS 1X.  

    [kiubtech]$ python manage.py migrate_schemas --shared


O comando migrate_schemas ira fazer atualizações em todas schemas.  

    [kiubtech]$ python manage.py migrate_schemas

# Powered by Open Source Projects. 

Agradecemos imensamente os esforços das comunidades que apoiam o desenvolvimento dos seguintes projetos.

- [Django Project](https://www.djangoproject.com)
- [Django Solo](https://github.com/lazybird/django-solo)
- [Pillow](https://github.com/python-pillow/Pillow)
- [PostGreSQL](https://www.postgresql.org/)
- [Psycopg2](https://github.com/psycopg/psycopg2)
- [Bootstrap v4](http://getbootstrap.com/)


# Licença do projeto.

MIT License

    Copyright (c) 2017 Kiub Technologies
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.



Make with love by [@kiubtech](https://twitter.com/kiubtech) and [@pythonizame](https://twitter.com/pythonizame).


