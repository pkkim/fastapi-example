from typing import Union

import psycopg2
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    conn = psycopg2.connect(host="database-1.cytow4gkazsz.us-west-1.rds.amazonaws.com", port=5432, database="postgres", user="postgres", password="mypassword")
    cur = conn.cursor()
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    return {"item_id": item_id, "q": q, "db_version": db_version}
