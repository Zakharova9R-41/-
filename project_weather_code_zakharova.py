def get_weather_input():
    """
    данные от пользователя
    """
    try:
        temperature = float(input("Введите температуру в градусах: "))
        is_rainy = input("Есть осадки? (да/нет): ").lower().strip() in ['да']

        if is_rainy:
            is_raining_heavily = input("Осадки сильные? (да/нет): ").lower().strip() in ['да']
        else:
            is_raining_heavily = False

        return temperature, is_rainy, is_raining_heavily
    except ValueError:
        print("Ошибка: Введите температуру (число)")
        return get_weather_input()


def clothing_advisor(temperature, is_rainy, is_raining_heavily):
    """
    Советует что надеть
    """

    if is_rainy:
        print(f"- Сильные осадки: {'Да' if is_raining_heavily else 'Нет'}")

    print("\nРекомендуется надеть:")

    # Выбор одежды
    if temperature > 20 and temperature < 30:
        if is_rainy:
            print("🔸 Футболку")
            print("🔸 Шорты")
            print("🔸 Дождевик")
        else:
            print("🔸 Футболку")
            print("🔸 Шорты")

    elif temperature > 0:
        if is_rainy:
            if is_raining_heavily:
                print("🔸 Пальто")
                print("🔸 Резиновые сапоги")
                print("🔸 Зонт")
            else:
                print("🔸 Пальто")
                print("🔸 Дождевик")
        else:
            print("🔸 Пальто")

    else:
        print("🔸 Пуховик")


# Основная программа
def main():
    print("                                              ")
    print("Здравствуйте, я помогу что надеть по погоде!\n")

    temperature, is_rainy, is_raining_heavily = get_weather_input()
    clothing_advisor(temperature, is_rainy, is_raining_heavily)


if __name__ == "__main__":
    main()