per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("money:")
deposit = [i * float(money) * 0.01 for i in per_cent.values()]
depositint= list(map(int, deposit))
print("deposit =", depositint)
print("Максимальная сумма, которую вы можете заработать —", max(depositint))