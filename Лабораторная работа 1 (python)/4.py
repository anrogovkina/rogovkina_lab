users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
all=0
unique=0
dict_users={"Общее количество":all,
            "Уникальные посещения":unique}
unique_users={'user1', 'user2', 'user3', 'user1', 'user4', 'user2'}
dict_users["Общее количество"]=len(users)
dict_users["Уникальные посещения"]=len(unique_users)
print(dict_users)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
