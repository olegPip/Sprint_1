class Tester:

    def __init__(self, name):  # Добавили аргумент "self"
        self.name = name       # Переменная сохранена  как атрибут обьекта через "self.name" 
                               # Удалена строка "deadline = True" так как статус дедлайна передается напрямую в метод "work_hard"

    def work_hard(self, deadline=True):
        if deadline:                         # Условие "if self.deadline:" измено на "if deadline" 
            print(self.name, 'Что ж, часок ещё поработаю!') # Теперь метод использует значение аргумента deadline, который передается при вызове (False для tester_1 и True для tester_2), а не ищет несуществующий атрибут внутри класса.
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester(name='tester_1')
tester_1.work_hard(deadline=False) # 'tester_1 Можно отдыхать'
tester_2 = Tester(name='tester_2')
tester_2.work_hard(deadline=True) # 'tester_2 Что ж, часок поработаю!'                    