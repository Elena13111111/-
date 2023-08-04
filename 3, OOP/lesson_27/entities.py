# entities -сущность для хранения данных /dataclass/ Для хранения баззовых данных

from  dataclasses import dataclass, field

ADMIN_ACCESS = 'ADMIN_ACCESS'
STUDENT_ACCESS = 'STUDENT_ACCESS'


@dataclass(frozen=True)
class Student:
    name: str  #имя строковое
    password: str  #пароль строковое
    role: str = STUDENT_ACCESS  #допуск строковое / по умолчанию Студента
    marks: list = field(default_factory=list)  #оценки числа для каждого свои, по умолчанию без оценок


    #field(default_factory=list) -задает данные для каждого объекта



