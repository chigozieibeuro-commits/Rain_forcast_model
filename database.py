import  psycopg2

def connectio():
    con=psycopg2.connect(
        host="db",
        user="postgres",
        database="weather",
        password="password",
        port="5432"

    )

    return con