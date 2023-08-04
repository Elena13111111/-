#управляющие методы/ преобразуем def run_study_program()

from utils import Utils    #ссылка на файл utils.ру импортируя class Utils
from repository import StudentsRepoXlsx #ссылка на файл repository на class StudentsRepoXlsx(StudentsRepo)


class TestProgramRunner:
    repo = StudentsRepoXlsx() # инициализируем параеметры

    def run(self):
        students = self.repo.load_students() # ссылка на def load_students(self)
        login, password = Utils.input_login_pass()  #логин и пароль введееного  class Utils
        Utils.check_is_registered(students, login, password) #регистрация

# запуск программы
runner = TestProgramRunner()
runner.run()

# Debug  login, password = Utils.input_login_pass()  --> пишем в строке students и мы видим всех наших студентов
# и админа со всей информацией