#  Games Education - Poker, Chess, Checkers, Backgammon, Dominoes and others!

## Общая информация:
Данный сервис ещё в стадии разработки, но в нём уже можно делать многие вещи:
* Регистрировать новых пользователей  
* Авторизоваться под своей учёткой  
* Создавать страницы курсов (доступно после авторизации)  
* Просматривать список всех курсов  
* Просматривать список курсов по категориям (с помощью бокового меню)  
* Искать курсы по названию (с помощью формы поиска в шапке)  
* Использовать пагинацию для подгрузки новой порции курсов
* Просматривать детальное описание курса со списком уроков и расписанием занятий  
* Редактировать и удалять свои курсы (доступно после авторизации)  

## Что нужно реализовать:
* Создание, редактирование и удаление стриниц уроков
* Создание страницы расписания начала курсов
* Заглушку для урока, если он объявлен в расписании, но ещё не создан

## Для запуска требуется:
* Python >=3.8
* django >= 3
* mysqlclient = latest (for connecting Django to MySQL)
* MySQL >= 5.7
* mixer >= 6.1.3

## Настройки подключения к базе данных:
Для подключения базы MySQL создайте файл my.cnf в папке /education на основе шаблона my.cnf.example

## Чтобы создать тестовые данные:
```bash
$ cd "Path to manage.py"
$ python manage.py mix_data
```

Это создаст следующие тестовые данные:
* Группы
* Пользователей
* Курсы
* Уроки для курсов
* Расписание некоторых уроков
 
## Создание и применение миграций:
```bash
$ cd "Path to manage.py"
$ python manage.py makemigrations
$ python manage.py makemigrations education
$ python manage.py migrate
```

## Запуск:
```bash
$ cd "Path to manage.py"
$ python manage.py runserver
```

## Создание первого пользователя:
```bash
$ cd "Path to manage.py"
$ python manage.py createsuperuser
``` 

## Дополнительная информация
Код создан в учебных целях в рамках учебного курса по веб-разработке - [otus.ru](https://otus.ru)
