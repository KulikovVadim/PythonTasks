years = float(input("Введите количество лет: "))
quantity = int(input("Введите количество экспонатовж: "))
kolvodney = years * 365
c = kolvodney * 12 * 8
minutes = 5 * quantity
dney = minutes // 460
let = dney // 365
print ("Вы посмотрите: " + str(c) + " экспонатов за " + str(years) + " лет")
print ("вы потратите: " + str(let) + " лет или " + str(dney) + " дней или " + str(minutes) + " минут" )
