# class Dog:
#     def __new__(cls, *args, **kwargs):
#         print(f'__new__ | {cls}')
#         #вызываеться для создания родительского объекта, super возвращаеться ссылку и по ссылке создаем новый обект
#         #просим создать нашего родителя объект по классу Dog
#         return super().__new__(cls)
#
#     def __init__(self):
#         print(f'__init__ | {self}')
#
#
# dog1 = Dog()
# # print(dog1)

# 2.Singleton
class DB:
    db_conector = None #создание db_conector по умолчанию

    def __new__(cls, *args, **kwargs): # будем возвращаться один и тот же один db_conector
        if DB.db_conector is None:  #если он None
            DB.db_conector = super().__new__(cls) # тогда создадим новый
        return DB.db_conector  # если db_conector  Есть, мы его вернем


    def __init__(self, login, password):
        self.login = login
        self.password = password

    def save_data(self):
        print('Данные Сохранены')

    def delete_data(self):
        print('Данные Удалены')

    def __str__(self):  #для чтения
        return f'{self.login} | {self.password} | {id(self)}' # один id у всех . Теперь можно создать много db_conector

# db_conector1 = DB('postgres1', 'postgres45')
# db_conector2 = DB('postgres2', 'postgres56')

for i in range(1, 10):
    db_coonnector1 = DB('postgres1', 'postgres45')
    print(db_coonnector1)
    db_coonnector1.save_data()
    db_coonnector2 = DB('postgres2', 'postgres56')
    print(db_coonnector2)
    db_coonnector2.save_data()

# print(db_conector1)
# print(db_conector2)