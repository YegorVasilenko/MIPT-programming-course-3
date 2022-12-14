###### Чем классовая переменная отличается от поля? В какой ситуации можно через поле влиять на поля других экземпляров?
Поле класса распространяется на все его экземпляры, а вот классовые переменные каждый экземпляр "избирает себе сам".

###### Как называется типизация в питоне и какой идеей она руководствуется?
Динамическая типизация (во многих ЯП, например, C, типизация статическая). Программисту
не нужно явно задавать тип объекта или значения функции.

###### Каким образом мы реализуем полиморфизм для созданных нами объектов?
Хочется работать с экземплярами разных классов, но по-одинаковому. Например,
у меня есть класс Deutsch и класс English. Я хочу, чтобы экземпляры этих классов
поздоровались друг с другом по-своему. Удобно, если это описывается однообразно:
Deutsch.hello(), English.hello() (результат "Hallo!" и "Hello!"). Можно добавить
еще и классы Dutch и Russian: Dutch.hello() вернет "Hoi!", Russian.hello() — "Привет!" :)

###### Зачем переопределять метод _radd_() наравне с _add_()?
Для некоторых классов (x + y) не равно тождественно (y + x). Операции ведь бывают разными,
например, умножение четырехмерных чисел (кватернионов) не коммутативно, так что при 
реализации класса Quaternion приедтся переопределить и _add_(), и _radd()_.
