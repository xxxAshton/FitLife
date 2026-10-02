# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
CONSTANT_ML = 1000

# Приветствие
print('Вас приветствует цифровой фитнес-трекер FitLife!')
print('Моя задача-рассчитать индекс массы тела и рекомендованную норму воды в день')
print('Давайте знакомиться!')

# 1. Знакомство
user_name = input('Как вас зовут?').title()
user_age = int(input('Сколько вам лет?'))

# 2. Сбор данных
user_weight = float(input('Введите ваш вес (кг):'))
user_height = float(input('Введите ваш рост (м):'))

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# Подсчет воды: вес * 30 мл
water_ml = user_weight * WATER_PER_KG
water_needed = water_ml / CONSTANT_ML
water_needed = round(water_needed, 1)

# 4. Вывод красивого результата
print(f'Отчет для пользователя: {user_name}, {user_age} лет')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_needed} л. в день')
print('')
print("Расчет окончен. Будьте здоровы!")
