# Описание проекта:
Реализация популярной игры "Змейка" при помощи языка программирования Python и основ ООП.

## Классы, методы и функции:

- Класс GameObject:
Атрибуты:
• position — позиция объекта на игровом поле. В данном случае она инициализируется как центральная точка экрана.
• body_color — цвет объекта. Он не задаётся конкретно в классе GameObject, но предполагается, что будет определён в дочерних классах.
Методы:
• draw — абстрактный метод. Этот метод должен определять, как объект будет отрисовываться на экране. По умолчанию — pass.
- Класс Apple, наследуется от GameObject:
Атрибуты:
• body_color — цвет яблока. В данном случае задаётся RGB-значением (красный цвет — (255, 0, 0)).
• position — позиция яблока на игровом поле. Яблоко появляется в случайном месте на игровом поле.
Методы:
• randomize_position — устанавливает случайное положение яблока на игровом поле — задаёт атрибуту position новое значение. Координаты выбираются так, чтобы яблоко оказалось в пределах игрового поля.
draw — отрисовывает яблоко на игровой поверхности.
- Класс Snake, наследуется от GameObject:
Атрибуты:
• length — длина змейки. Изначально змейка имеет длину 1.
• positions — список, содержащий позиции всех сегментов тела змейки. Начальная позиция — центр экрана.
• direction — направление движения змейки. По умолчанию змейка движется вправо.
• next_direction — следующее направление движения, которое будет применено после обработки нажатия клавиши. По умолчанию задать None.
• body_color — цвет змейки. Задаётся RGB-значением (по умолчанию — зелёный: (0, 255, 0)).
Методы:
• update_direction — обновляет направление движения змейки.
• move — обновляет позицию змейки (координаты каждой секции), добавляя новую голову в начало списка positions и удаляя последний элемент, если длина змейки не увеличилась.
• draw — отрисовывает змейку на экране, затирая след.
• get_head_position — возвращает позицию головы змейки (первый элемент в списке positions).
• reset — сбрасывает змейку в начальное состояние.
- handle_keys — обрабатывает нажатия клавиш, чтобы изменить направление движения змейки.

# Автор: [Аринов Данияр](https://github.com/vegitobluefan)