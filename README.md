### Installing necessary packages:  
* `pip install fastapi`
* `pip install "uvicorn[standard]"`  
* `pip install sqlalchemy`  
* `pip install pymysql`
* `pip install pytest`
* `pip install pytest-mock`
* `pip install httpx`
* `pip install cryptography`
### Run the server:
`uvicorn api.main:app --reload`
### Test API by built-in docs:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

CONFIG.PY Example
class conf:
    db_host = "localhost"
    db_name = "sandwich_maker_api"
    db_port = 3306
    db_user = "root"
    db_password = "" #replace with your db password
    app_host = "localhost"
    app_port = 8000
