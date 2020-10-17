import psycopg2





#cur.execute("CREATE TABLE person (id serial PRIMARY KEY, name text, age integer);")
#cur.execute("INSERT INTO person (name, age) VALUES (%s, %s)",("O'Relly", 60))
#cur.execute("INSERT INTO person (name, age) VALUES (%s, %s)",('Regis', 35))
#conn.commit()

def inserir_plan(planilhaWishLocal):
    conn = psycopg2.connect("dbname=mydatabase user=postgres password=gerson@123")
    cur = conn.cursor()
    #cur.execute("INSERT INTO person (name, age) VALUES (%s, %s)",(str(name), int(age)))
    cur.execute("INSERT INTO person (name, age) VALUES (%s, %s)",(str(planilhaWishLocal), 11))
    conn.commit()
    conn.close()


def mostrar_plan():
    conn = psycopg2.connect("dbname=mydatabase user=postgres password=gerson@123")
    cur = conn.cursor()
    cur.execute("SELECT * FROM person;")
    a = cur.fetchall()
    cur.close()
    conn.close()
    return a