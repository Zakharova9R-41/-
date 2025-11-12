def get_weather_input()
try:
temperature = float(input("Введите температуру в градусах: "))
is_rainy = input("Есть осадки? (да/нет): ").lower().strip() in ['да', 'yes', 'y', 'д']
if is_rainy:
is_raining_heavily = input("Осадки сильные? (да/нет): ").lower().strip() in ['да', 'yes', 'y', 'д']
else:
is_raining_heavily = False
return temperature, is_rainy, is_raining_heavily
except ValueError:
print("Ошибка: Введите корректную температуру (число)")
return get_weather_input()
def recommend_clothing(temperature, is_rainy, is_raining_heavily):
print("\nРекомендации по одежде:")
print("Что надеть:")
if temperature > 20:
if is_rainy:
print("Футболку, шорты и дождевик")
else:
print("Футболку и шорты")
elif temperature > 0:
if is_rainy:
if is_raining_heavily:
print("Пальто, резиновые сапоги и зонт")
else:
print("Пальто и дождевик")
else:
print("Пальто")
else:
print("Пуховик")
def main():
print("=" * 50)
print("Помощник по выбору одежды по погоде")
print("=" * 50)
temperature, is_rainy, is_raining_heavily = get_weather_input()
print(f"\nТемпература: {temperature}°C")
print(f"Осадки: {'Да' if is_rainy else 'Нет'}")
if is_rainy:
print(f"Сильные осадки: {'Да' if is_raining_heavily else 'Нет'}")
recommend_clothing(temperature, is_rainy, is_raining_heavily)
if __name__ == "__main__":
main()

