from PIL import Image, ImageDraw
import math
"""
Локальные переменные функции draw_pythagoras_tree:
draw - рисование объектов
x - начальное значение x
y - начальное значение y
x_end - конечное значение x
y_end - конечное значение y
angle - угол наклона
size - размер
level - уровень рисования
"""
def draw_pythagoras_tree(draw, x, y, angle, size, level):
    if level == 0:
        return
    x_end = x + int(math.cos(angle) * size)
    y_end = y - int(math.sin(angle) * size)
    draw.line([x, y, x_end, y_end], fill='green', width=1)
    new_size = size * math.sqrt(2) / 2
    draw_pythagoras_tree(draw, x_end, y_end, angle - math.pi / 4, new_size, level - 1)
    draw_pythagoras_tree(draw, x_end, y_end, angle + math.pi / 4, new_size, level - 1)
# Создаем пустое пространство
width, height = 800, 600
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# выбираем параметры
initial_size = 150
initial_x = width // 2
initial_y = height - 50
initial_angle = math.pi / 2
max_level = 15
draw_pythagoras_tree(draw, initial_x, initial_y, initial_angle, initial_size, max_level)
image.show()