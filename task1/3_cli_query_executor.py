import psycopg2
import tabulate

host = "localhost"
database = "postgres"
user = "postgres"
password = "mysecretpassword"
port = 5432

print("\nConnecting to PostgreSQL database...")
print(f'host={host}\ndatabase={database}\nuser={user}\npassword=**********\nport={port}')
print('\nEnter the sql-command you want to execute or e for exit\n')

with psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port,
        ) as conn:
    with conn.cursor() as cursor:

        while True:

            # введення SQL-запиту
            command = input('sql-command->').strip()
            if command == 'e':
                break

            try:
                cursor.execute(command)
                conn.commit()
                print('Command executing result:')

                if command.split()[0].lower() == 'select':  # CRUD-команди (не SELECT) не повертають нічого в курсор
                    res = cursor.fetchall()                 # тому потрібне це розгалудження
                    columns = [i.name for i in cursor.description]
                    table = tabulate.tabulate(res, headers=columns, tablefmt="grid")
                    print(table)
                    print('\n')
                else:
                    print(cursor.rowcount, 'record(s) processed.\n')  # виводимо кількість рядків, оброблених CRUD-командою

            except Exception as e:
                print('Command don\'t recognized.\nError message is: ', e, '\n')
