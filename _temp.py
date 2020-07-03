from psycopg2 import connect
from models import User

USER = "postgres"
HOST = "127.0.0.1"
PASSWORD = "coderslab"

try:
    cnx = connect(user=USER, password=PASSWORD, host=HOST, database="workshop2");
except Exception as e:
    print("Error", e.pgcode, ":", e)
cnx.autocommit = True
cur = cnx.cursor()

u1 = User("John", "dupa123")

u1.safe_to_db(cur)