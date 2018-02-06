[![Travis](https://img.shields.io/travis/codesponsor/codesponsor.svg)]()
[![Waffle.io - Columns and their card count](https://badge.waffle.io/codesponsor/codesponsor.svg?columns=all)](https://waffle.io/codesponsor/codesponsor)


# Code Sponsor

Code Sponsor provides funding for open source projects through ethical advertising.

## Partnership

Code Sponsor is a proud partner of [Gitcoin](https://codesponsor.io/t/c/e60d8217823be14100be63adb5d31a79/).
Gitcoin pushes Open Source Forward. Learn more at [https://gitcoin.co](https://codesponsor.io/t/c/e60d8217823be14100be63adb5d31a79/)

<img src='https://codesponsor.io/t/l/e60d8217823be14100be63adb5d31a79/pixel.png' style='width:1px; height:1px;' >

## Running Locally

### With Docker

```
git clone https://github.com/codesponsor/codesponsor.git
cd codesponsor
cp code_sponsor/.env-sample code_sponsor/.env
docker-compose up -d
```
Navigate to `http://0.0.0.0:8000/`.

### Without Docker

```
git clone https://github.com/codesponsor/codesponsor.git
cd codesponsor
cp code_sponsor/.env-sample code_sponsor/.env

```

You will need to edit the `code_sponsor/.env` file with your local environment settings.

### Setup Database

PostgreSQL is the database used by this application. Here are some instructions for installing PostgreSQL on various operating systems.

[OSX](https://www.moncefbelyamani.com/how-to-install-postgresql-on-a-mac-with-homebrew-and-lunchy/)

[Windows](http://www.postgresqltutorial.com/install-postgresql/)

[Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04)

Once you have Postgres installed and running on your system, enter into a Postgres session.
```
psql
```
Create the database and a new privileged user.
```sql
CREATE DATABASE codesponsor_development;
CREATE USER codesponsor_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE codesponsor_development TO codesponsor_user;
```
Exit Postgres session
```
\q
```
Update the code_sponsor/.env file with the DATABASE ENV:

```bash
DATABASE_URL=psql://codesponsor_user:password@127.0.0.1:5432/codesponsor_development
```


### Startup server


```
pipenv install
pipenv run python manage.py migrate
pipenv run python manage.py createcachetable
pipenv run python manage.py runserver 0.0.0.0:8000
```

Navigate to [http://localhost:8000/](http://localhost:8000/)


### Deploying to Heroku

Ensure you add the buildpacks:

    $ heroku buildpacks:add --index 1 heroku/nodejs
    $ heroku buildpacks:add --index 2 heroku/python

Deploy to Heroku

    $ heroku create
    $ git push heroku master
    $ heroku run python manage.py migrate
    $ heroku open

## Legal

```
Copyright (C) 2018 Code Sponsor

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
```

## License
[GNU AFFERO GENERAL PUBLIC LICENSE](./LICENSE)

<!-- Google Analytics -->
<img src='https://ga-beacon.appspot.com/UA-102162972-4/codesponsor/codesponsor' style='width:1px; height:1px;' >
