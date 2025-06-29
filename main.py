def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_detailed_bmi_analysis(bmi):
    if bmi < 16:
        return "Выраженный дефицит массы тела"
    elif 16 <= bmi < 18.5:
        return "Недостаточная масса тела"
    elif 18.5 <= bmi < 25:
        return "Норма"
    elif 25 <= bmi < 30:
        return "Избыточная масса тела (предожирение)"
    elif 30 <= bmi < 35:
        return "Ожирение 1 степени"
    elif 35 <= bmi < 40:
        return "Ожирение 2 степени"
    else:
        return "Ожирение 3 степени (морбидное)"


def get_bmi_recommendation(bmi):
    if bmi < 18.5:
        return "Рекомендуется консультация диетолога для набора веса"
    elif 18.5 <= bmi < 25:
        return "Ваш вес в норме! Поддерживайте текущий режим"
    else:
        return "Рекомендуется увеличить физическую активность и скорректировать питание"


def calculate_ideal-weight(height, gender='unisex'):
    """По формуле Devine (1974)"""
def calculate_ideal_weight(height, gender='unisex'):
    """По формуле Devine (1974)"""
    if gender.lower() == 'male':
        return 50 + 2.3 * ((height * 100) - 152.4) / 2.54
    elif gender.lower() == 'female':
        return 45.5 + 2.3 * ((height * 100) - 152.4) / 2.54
    else:
        return (50 + 45.5) / 2 + 2.3 * ((height * 100) - 152.4) / 2.54

def calculate_daily_calories(weight, height, age, gender, activity_level=1.2):
    """Формула Миффлина-Сан Жеора"""
    if gender.lower() == 'male':
        return 50 + 2.3 * ((height * 100) - 152.4) / 2.54
    elif gender.lower() == 'female':
        return 45.5 + 2.3 * ((height * 100) - 152.4) / 2.54
    else:
        return (50 + 45.5) / 2 + 2.3 * ((height * 100) - 152.4) / 2.54


def validate_input(value, min_val, max_val):
    try:
        num = float(value)
        if min_val <= num <= max_val:
            return True
        return False
    except ValueError:
        return False
def calculate_body-fat(bmi, age, gender):
    """Расчет процента жира в организме по формуле YMCA"""
    if gender == 'male':
        return (1.20 * bmi) + (0.23 * age) - 16.2
    else:
        return (1.20 * bmi) + (0.23 * age) - 5.4

def get_body-fat_analysis(body-fat, gender):
    """Анализ процента жира в организме"""
    if gender == 'male':
        if body-fat < 6:
            return "Опасный уровень (необходима медицинская консультация)"
        elif 6 <= body-fat < 14:
            return "Атлетическое телосложение"
        elif 14 <= body-fat < 18:
            return "Спортивное телосложение"
        elif 18 <= body-fat < 25:
            return "Средний уровень"
        else:
            return "Высокий процент жира (рекомендуется снижение)"
    else:
        if body-fat < 14:
            return "Опасный уровень (необходима медицинская консультация)"
        elif 14 <= body-fat < 21:
            return "Атлетическое телосложение"
        elif 21 <= body-fat < 25:
            return "Спортивное телосложение"
        elif 25 <= body-fat < 32:
            return "Средний уровень"
        else:
            return "Высокий процент жира (рекомендуется снижение)"

def main():
    print("=== BMI Калькулятор ===")

    # Ввод данных с валидацией
    while True:
        try:
            weight = float(input("Введите ваш вес (кг): "))
            if not validate_input(weight, 30, 300):  # Реалистичные пределы веса
                print("Ошибка: вес должен быть между 30 и 300 кг")
                continue

            height = float(input("Введите ваш рост (м): "))
            if not validate_input(height, 1.0, 2.5):  # Реалистичные пределы роста
                print("Ошибка: рост должен быть между 1.0 и 2.5 м")
                continue

            age = int(input("Введите ваш возраст: "))
            if not validate_input(age, 2, 120):  # Реалистичные пределы возраста
                print("Ошибка: возраст должен быть между 2 и 120 годами")
                continue

            gender = input("Введите ваш пол (male/female): ").lower()
            if gender not in ['male', 'female']:
                print("Ошибка: пол должен быть 'male' или 'female'")
                continue

            break
        except ValueError:
            print("Ошибка: введите числовое значение")

    # Расчеты
    bmi = calculate_bmi(weight, height)
    ideal-weight = calculate_ideal-weight(height, gender)
    body-fat = calculate_body-fat(bmi, age, gender)

    ideal-weight = calculate_ideal-weight(height, gender)
    calories = calculate_daily_calories(weight, height, age, gender)

    # Вывод результатов
    print("\n=== Результаты ===")
    print(f"Ваш BMI: {bmi:.1f}")
    print(f"Категория: {get_detailed_bmi_analysis(bmi)}")
    print(f"Рекомендации: {get_bmi_recommendation(bmi)}")
    print(f"Идеальный вес: {ideal-weight:.1f} кг")
    print(f"\nПроцент жира в организме: {body-fat:.1f}%")
    print(f"Анализ: {get_body-fat_analysis(body-fat, gender)}")
    print(f"Суточная норма калорий: {calories:.0f} ккал")

if __name__ == "__main__":
    main()

VERSION = "3.0"
