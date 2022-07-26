# Installation Process

- clone project

  - `git clone https://github.com/MacAlistair1/flask-restful-api.git`

- Command after clone success

  - `python3 -m venv env` **virtual env**
  - `source env/bin/activate` **activate virtual env if required**
  - `pip install -r requirements.txt` **install requirements dependency modules**
  - `flask run` **serve the project**

- Api EndPoint
  - `{BASE_URI}/api/buses` `GET` **get bus list**
  - `{BASE_URI}/api/buses` `POST` **store new bus**
  - `{BASE_URI}/api/buses/<id>` `GET` **get single bus object**
  - **There are other api EndPoints for put and delete the bus object**
