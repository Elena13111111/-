#управляющие методы/ преобразуем def run_study_program()

from utils import Utils    #ссылка на файл utils.ру импортируя class Utils
from repository import StudentsRepoXlsx #ссылка на файл repository на class StudentsRepoXlsx(StudentsRepo)
from test_service import TestService

class TestProgramRunner:
    repo = StudentsRepoXlsx() # инициализируем параеметры
    test_service = TestService(repo) # ссылка на логическое ядро (test_service )

    def run(self):
        students = self.repo.load_students() # ссылка на def load_students(self) /загрузка студентов
        login, password = Utils.input_login_pass()  #сверка логин и пароль введееного  class Utils
        student =Utils.check_is_registered(students, login, password) #регистрация одного студента
        config = self.repo.get_config()   # выполнение работы
        self.test_service.try_to_show_menu(students, student, config['menu']) # если неправильный логин или пароль

# запуск программы
runner = TestProgramRunner()
runner.run()

# Debug  login, password = Utils.input_login_pass()  --> пишем в строке students и мы видим всех наших студентов
# и админа со всей информацией