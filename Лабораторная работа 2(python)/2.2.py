salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital=0
for i in range(months):
    budget=abs(salary-spend)
    spend*=(1+increase)
    money_capital+=budget

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital,2))
