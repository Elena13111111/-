class Cat: # пишем класс Cat, это шаблон Кота, не сущ-ий объект
    age = 2   # переменная
    name = 'муся'

cat1 ={  #создаем словарь
    'age': 2,
    'name': 'Василий'
}
# сущ-ий объект класса, это конструктор. Это метод, кот.вызываеться при создании объекта
cat2 = Cat()
cat3 = Cat()

print(cat1['name'])#выводим имя
print(cat2.name) #выводим имя
print(cat3.name) #выводим имя

# print(cat1)
# print(cat2.__dict__)