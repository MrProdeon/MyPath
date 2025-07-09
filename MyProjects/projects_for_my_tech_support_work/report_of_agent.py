print('''Для сверки отчета агента потребуется :
1) Просмотреть на какие юридическая лица у водителя имеются балансы. 
   Информация о юридических лицах интеграции находится в справочники - внешние интеграции
2) Собрать нужные нам отчёты :
   - Отчет по поездкам из старой версии ЛК для нужной интеграции. (Проставляем нужную дату. Желательно 1 число следующего месяца)
   - Отчеты - выплаты за нужный период, в самой выгрузке фильтруем по нужному водителю.
''')

print('Рассчитаем bonusSum: ')
bonusSum = float(input('В отчете поездок, в фильтре по столбцу "Адрес" выбираем все пустые, кроме компенсаций\n---> '))
print(f'bonusSum = {bonusSum} ')
print('Рассчитаем tripsSum : ')
card_trips = float(input('Рассчет безналичных поездок : общая сумма за поездку - комиссия агрегатора - "начислено"\n---> '))
cash_trips = float(input('Наличные поездки = сумма комиссии таксопарка только по наличным поездкам\n---> '))
park_commission_in_jump = float(input('Комиссия парка с успешных выводов : отчете по выплатам суммируем столбец "Комиссия водителей за вывод"\n---> '))
compensation = float(input('В отчете поездок, в фильтре по столбцу "Адрес" выбираем все пустые с комментарием "Компенсация"\n--->  '))
tripsSum =compensation + cash_trips + card_trips + park_commission_in_jump

print(f'tripsSum = {tripsSum}')

print('Рассчитаем agentsExpenses : ')
agentExpenses = float(input('В отчете по выплатам, отфильтрованному по водителю, сумма столбца "Комиссия банка"\n---> '))
print(f'agentExpenses = {agentExpenses}')

print('Рассчитаем commissionSum : ')
trips_commission = float(input('В отчете поездок сумма столбца с комиссией парка'))
commission_of_bank = float(input('В отчете выплат сумма комиссий банка'))
commissionSum = trips_commission + (park_commission_in_jump - commission_of_bank)
print(f'commissionSum = {commissionSum}')

print(f'''
Итого :
bonusSum = {bonusSum}
tripsSum = {tripsSum}
agentExpenses = {agentExpenses}
commissionSum = {commissionSum}

''')