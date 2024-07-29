-- Запити для виконання:

-- Отримати всі завдання певного користувача. Використайте SELECT для отримання завдань конкретного користувача за його user_id.
select * from tasks where user_id = 3;

-- Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
select tasks.id, tasks.title, tasks.description, users.fullname, status.name as status from tasks left join status on tasks.status_id=status.id left join users on tasks.user_id=users.id where status.name='new'
--or
select tasks.id, tasks.title, tasks.description, users.fullname from tasks left join users on tasks.user_id=users.id where status_id = (select id from status where name = 'new');

-- Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.
update tasks set status_id=(select id from status where name='in progress') where id=32;

-- Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.
select users.* from users left join tasks on users.id=tasks.user_id where tasks.user_id is null;
-- or
select * from users where id not in (select user_id from tasks);

-- Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.
insert into tasks (title, description, status_id, user_id) values ('vvre fev re', 'fdfdv lf vfdvfdv c cv  c', (select id from status where name='new'), 6);

-- Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.
select * from tasks where status_id=(select id from status where name='new');

-- Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.
delete from tasks where id=51;

-- Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.
select * from users where email like '%john%@%.%';

-- Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.
update users set fullname='Hulio Lopez' where id=20;

-- Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
select status.name as statuses, count(tasks.id) as task_qty from tasks left join status on tasks.status_id=status.id group by status.name;

-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').
select tasks.*, users.email from tasks left join users on tasks.user_id=users.id where email like '%@example.com';

-- Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.
select * from tasks where description is null;

-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.
select users.fullname, tasks.title, tasks.description from tasks left join users on tasks.user_id = users.id inner join status on tasks.status_id=status.id where status.name='in progress';

-- Отримати користувачів та кількість їхніх завдань. Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.
select users.fullname, count(tasks.id) as task_qty from tasks left join users on tasks.user_id=users.id group by users.fullname order by users.fullname;
