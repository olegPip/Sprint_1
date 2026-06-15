class TestCase:

    def __init__(self):
        self.steps = {}        # Инициализируем пустой словарь для шагов и переменной для ожидаемого результата
        self.result = None

    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text       # Добавляем в словарь шаг тест-кейса. Принимает 2 параметра ключ-значение (step_number-step_text)

    
    def delete_step(self, step_number):          # Удаляем шаг из step по ключу step_number
        if step_number in self.steps:
            del self.steps[step_number]

    def set_result(self, result):                 # Устанавливаем ожидаемый результат
        self.result = result

    def get_test_case(self):


        info = {                                  # Выводи информацию о составе тест-кейса
 
            'Шаги': {
                1: 'Перейти на сайт',
                2: 'Перейти в раздел Товары',
                3: 'Нажать кнопку «В корзину» у первого товара'
            },
        'Нажать кнопку': '«В корзину» у первого товара'
        }
        print(info)


test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case() 