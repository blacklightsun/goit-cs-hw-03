import psycopg2

# open sql-script
with open('create_tables.sql', 'r') as f:
    sql_script = f.read()
    print('Скрипт відкрито')
    # print(sql_script)


with psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="mysecretpassword",
        port=5432,
    ) as conn:
    with conn.cursor() as cursor:
        cursor.execute(sql_script)
        print('Скрипт виконано')

