### 1. Ответьте на вопрос: как бы вы тестировали/проверяли корректность, полноту и неизбыточность ваших тестов? Как бы вы осуществляли эти проверки в автоматическом режиме? Ответ приложите в текстовом виде в любом удобном формате.

Корректность и неизбыточность проверял бы по теории тестирования, применяя техники тест дизайна. 
Классы эквивалентности, граничные значения, таблица принятия решений и т.д.

Полноту проверял бы по метрике code coverage.

```
plugins: cov-4.1.0
collected 28 items                                                                                                                                                                                                                                                                                                 

tests\test_delivery_cost_dimensions.py ....                                                                                                                                                                                                                                                                  [ 14%] 
tests\test_delivery_cost_distance.py .............                                                                                                                                                                                                                                                           [ 60%]
tests\test_delivery_cost_fragile.py .....                                                                                                                                                                                                                                                                    [ 78%]
tests\test_delivery_cost_serviceworkload.py ......                                                                                                                                                                                                                                                           [100%] 

---------- coverage: platform win32, python 3.9.13-final-0 -----------
Name                        Stmts   Miss  Cover
-----------------------------------------------
app\delivery.py                32      0   100%
app\delivery_constants.py       2      0   100%
app\delivery_enums.py           9      0   100%
-----------------------------------------------
TOTAL                          43      0   100%
```


### 2. Также, просим ответить вас на эти вопросы:

- Почему вы хотите стать Наставником в Яндекс Практикуме?

Мне нравится учить других и закреплять уже то, что знаю, возвращаясь к основам.

- Какими компетенциями по вашему мнению должен обладать хороший наставник в вашей профессии? Почему? 
Обоснуйте ваш выбор с примерами из собственного опыта

Терпеливостью -- потому что необходимо дотошно и спокойно объяснять непонимающему студенту, 
что именно он делает не так и почему это неправильно, а также донести до него почему по другому лучше.

Умение учить -- чтобы знания усваивались их нужно правильно передавать и доносить. 
Иначе не найти общего языка и будет только негатив.

Эмпатией -- нужно сопереживать студенту, все люди разные, 
поэтому и подход к наставничеству должен быть отчасти индивидуальным.

- Как вы учились тестированию и попали в эту профессию?

Моя первая работа была тестировщиком-автоматизатором, и нравится проверять ошибки, исследовать как и что работает.
Теорию учил из классиков Куликова и Савина. Автоматизацию постигал сам на работе в рамках своих задач, а также с помощью своих pet проектов.

- Попробуй объяснить, что такое Локатор максимально простыми словами, для человека, не погруженного в ИТ

Локатор -- это некий указатель как можно понять из названия, который указывает нам на какой-то 
конкретный элемент на веб странице с необходимыми нам условиями. 
Как название города или деревни в такой большой стране как Россия.