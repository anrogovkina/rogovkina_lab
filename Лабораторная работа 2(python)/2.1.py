money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months=0
while True:
    budget = abs(salary - spend)
    money_capital -= budget
    spend *= (1 + increase)
    months += 1
    if money_capital<budget:
        break
print("Количество месяцев, которое можно протянуть без долгов:", months)
