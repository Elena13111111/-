import os.path  # импортируем операционую систему


# создаем файл
def create_file(file_name):
    with open(file_name, "w") as file:
        for i in range(1, 10):
            file.write(f" Number : {i}\n")
          

# создаем папку
def create_folder(newpath):
      if not os.path.exists(newpath):   #если путь не сущ-ет
        os.makedirs(newpath)      # то сделай папку
#newpath = r'D:\pythonProject\venv\12.py'  # путь файла

# перенести файл из старого места в новое
def move_file(old_path, new_path):
    os.rename(old_path, new_path)


create_folder(r'test_folder')    #создание папки
create_file('text_text.txt')    #создание файла
move_file('text_text.txt', 'test_folder/text_text.txt')    # мы переместили наш файл в папку