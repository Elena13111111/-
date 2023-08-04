# ексель файл/ Интерфейс для работы с нашими данными

from abc import ABC, abstractmethod  # для абстрактного класса
import os    # для файла екселя
import pandas  # для файла екселя
import datetime  # для работы с датами
import json      # для файла json
from entities import Student  # из файла entities берем данные class Student

# абстрактный класс
class StudentsRepo(ABC):
    @abstractmethod
    def load_students(self):
        pass

   # реализация на базе Екселя
class StudentsRepoXlsx(StudentsRepo):
    STUDENTS_FILE_NAME = 'marks.xlsx'
    CONFIG_FILE_NAME = 'initial_config.json'

# зарегестрированные студенты
    def update_wit_initial_students(self, students):  # для добавления новых студентов
        new_students = {}

#читаем/подгружаем наш файл 'initial_config.json'
#encoding = 'utf-8'- это набом символов/кодировка, кот. позволяет читать любые языки
        with open(self.CONFIG_FILE_NAME, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            initial_students = data['users'] # initial_students -> все данные студентов по каждому

        for login, data in initial_students.items(): # есть ли имя у наших студентов кот.пришли изначально
            if login in students:   #если наш логин находиться в students
                marks = students[login]   #берем оценку студента по логину
                student = Student(  #создаем студента
                    name=login, # имя берем из логина
                    password=data['password'],  #пароль из словаря
                    role=data['role'], # дата из словаря
                    marks=marks  #оценки просто пишем
                )
            else:  #если у нас нету этого студента пишем , но без оценки
                student = Student(
                    name=login,
                    password=data['password'],
                    role=data['role']
                ) # далее этого студента добавляем в словарик
            new_students[login] = student

        return new_students

    # подгружаем имя студента и его страница/  дата и оценка
    def load_students(self):
        students = {} # для загрузки наших студентов
        # находим наш файл через self
        if os.path.exists(self.STUDENTS_FILE_NAME):  # мы проверяем, если такой файл есть мы его читаем
            xlsx_data = pandas.ExcelFile(self.STUDENTS_FILE_NAME)
            for sheet in xlsx_data.sheet_names:
                df1 = pandas.read_excel(xlsx_data, sheet)
                marks = df1.values.tolist()  # получаем оценки
                students[sheet] = list(    # читаем страницу
                    map(
                        lambda el:
                        (
                            datetime.datetime(
                                year=int(el[0][:4]),
                                month=int(el[0][5:7]),
                                day=int(el[0][8:10]),
                                hour=int(el[0][11:13]),
                                minute=int(el[0][14:16]),
                                second=0
                            ),
                            el[1]),
                        marks
                    )
                )

        return self.update_wit_initial_students(students)
