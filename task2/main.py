
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def reading_all() -> str:
    '''
    функція для виведення всіх записів із колекції
    '''
    cursor = db.pets.find({}, {'_id': 0})
    return_string = ''
    for el in cursor:
        return_string += str(el)+'\n'
    return return_string


def reading_data_by_name(name: str) -> str:
    '''
    функціяяка дозволяє користувачеві ввести ім'я кота та виводить інформацію про цього кота
    '''
    return db.pets.find_one({"name": name}, {'_id': 0})


def update_age_by_name(name, age) -> bool:
    '''
    функція, яка дозволяє користувачеві оновити вік кота за ім'ям
    '''
    if isinstance(age, int):
        res = db.pets.update_one({"name": name}, {"$set": {"age": age}}, upsert=False)
        if res.modified_count == 1:
            return True
        else:
            return False
    else:
        print('Age data type is not integer')
        return False


def update_f_by_name(name, ficha) -> bool:
    '''
    функція, яка дозволяє додати нову характеристику до списку features кота за ім'ям
    '''
    res = db.pets.update_one({"name": name}, {"$addToSet": {"features": str(ficha)}}, upsert=False)
    if res.modified_count == 1:
        return True
    else:
        return False


def delete_by_name(name) -> bool:
    '''
    функція для видалення запису з колекції за ім'ям тварини
    '''
    res = db.pets.delete_one({"name": name})
    if res.deleted_count == 1:
        return True
    else:
        return False


def delete_all() -> int:
    '''
    функція для видалення всіх записів із колекції
    '''
    return db.pets.delete_many({}).deleted_count


uri = "mongodb+srv://blacklightsun:my11password@testcluster.iakfoko.mongodb.net/?retryWrites=true&w=majority&appName=testcluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!\n")
except Exception as e:
    print(e)

# create a connection to the pets database
db = client.pets

# операції з базою даних згідно ДЗ
print('\nAll database records:')
res1 = reading_all()
if res1 is not None:
    print(res1)
else:
    print('No records')


print('\nPet data by name:')
query_names = ['Murzik', 'Doris', 'Cat']
for name in query_names:
    res2 = reading_data_by_name(name)
    if res2 is not None:
        print(f'Query name: {name}. Found record(s): {res2}')
    else:
        print(f'Query name: {name}. Found record(s): No records')


print('\nUpdate age by name:')
query_names = ['Murzik', 'Boris', 'Cat', 'Doris']
query_new_ages = [2, 4, 9, 9.5]

for name, age in zip(query_names, query_new_ages):
    res3 = update_age_by_name(name, age)
    if res3 is True:
        print(f'Updating the age {age} of {name} is successfully!')
    else:
        print(f'Updating {name} is NOT successfully!')


print('\nUpdate the feature by name:')
query_names = ['Murzik', 'Boris', 'Cat', 'Doris']
query_new_features = ['long ears', 'cutted tail', 'short tail', 'grey moustache']

for name, ficha in zip(query_names, query_new_features):
    res4 = update_f_by_name(name, ficha)
    if res4 is True:
        print(f'Updating the feature {ficha} of {name} is successfully!')
    else:
        print(f'Updating {name} is NOT successfully!')

print('\nDelete pet by name:')
query_names = ['Dariy', 'Liza', 'Cat', 'Doris']
for name in query_names:
    res5 = delete_by_name(name)
    if res5 is True:
        print(f'Deleting {name} is successfully!')
    else:
        print(f'Deleting {name} is NOT successfully!')


print('\nDelete all pets from database:')
res6 = delete_all()
print(f'{res6} record(s) is deleted successfully!')

