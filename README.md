# Keyboard Simulator
# Клавиатурный Тренажер
версия 1.0

Aвторы:

Ильичев Матвей(matvey.ilichev@gmail.com)

Карпова Юля(yul_karpova@mail.ru)

Ревью выполнили: Анкудинов Александр

# Описание
Данное приложение является реализацией клавиатурного тренажёра.

# Требования

Python версии не ниже 3.6

PyQt версии 5

Sqlite версии 3

Matplotlib 3.4

# Состав

Графическая версия: KeyboardTrainer.py

Модули: modules/

Изображения: pictures/

Тесты: tests/

Пример запуска: ./KeyboardTrainer.py

# Подробности реализации

Модули, отвечающие за логику игры, расположены в папке modules и файле form.py. Большая часть проекта реализована с помощью PyQt5 - пользовательский интерфейс, подчеркивание синтаксиса, проигрывание музыки, выбор режимов и словарей. Сохранение статистики выполнено с помощью баз данных(Sqlite), её вывод реализован с помощью библиотеки matplotlib.pyplot. 

На модули сreate_user_dict, statistic, stopwatch написаны тесты, их можно найти в tests/.

# Возможности приложения можно увидеть, нажав на кнопку "Помощь" в меню.
