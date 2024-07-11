import psycopg2
import faker
import random

user_qty = 10
task_qty = 50

faker = faker.Faker()

status_script = "INSERT INTO status(name) VALUES ('new'), ('in progress'), ('completed')"


def create_user():
    return f"INSERT INTO users(fullname, email) VALUES ('{faker.name()}', '{faker.email()}')"


def create_task():
    return f"INSERT INTO tasks(title, desription, status_id, user_id) VALUES ('{faker.sentence(5)}', '{faker.text(100)}', '{random.choice(status_id_list)}', '{random.choice(user_id_list)}')"


with psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="mysecretpassword",
        port=5432,
        ) as conn:
    with conn.cursor() as cursor:

        cursor.execute(status_script)
        print('Статуси додано.')

        for _ in range(user_qty):
            cursor.execute(create_user())
        print(f'Фейкові юзери додані в кількості {user_qty} шт.')

        cursor.execute('select id from status')
        status_id_list = [i[0] for i in cursor.fetchall()]

        cursor.execute('select id from users')
        user_id_list = [i[0] for i in cursor.fetchall()]

        for _ in range(task_qty):
            cursor.execute(create_task())
        print(f'Фейкові таски додані в кількості {task_qty} шт.')
