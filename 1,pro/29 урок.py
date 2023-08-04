years_list = [1980, 1981, 1982, 1983, 1984, 1985]
print('Мой третий день рождения:', years_list[2])
print('Я самый старый:', years_list[-1])
things = ["mozzarella", "cinderella", "salmonella"]
print(things)
print(things[1].title())
print(things[1][0].upper() + things[1][1:])
print(things[0].upper())
print(things)
# things.pop(2)
things.remove('salmonella')
print(things)

surprise = ['Groucho', 'Chico', 'harpo']
print(surprise)
surprise.remove('harpo')
surprise.append('Harpo')
print(surprise)
print(surprise[2].title())

print('=' * 80)
e2f = {
    'do': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}
print(e2f['walrus'])
f2e = {}
for eng, france in e2f.items():
    f2e[france] = eng
print(e2f)
print(f2e)
print(f2e['chien'])
print(list(e2f.keys()))

print('=' * 80)

life = {
    'animals': {
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': {},
        'emus': {},
    },
    'plants': {},
    'other': {},
}
print(life)
print(list(life.keys()))
print(list(life['animals'].keys()))
print(life['animals']['cats'])