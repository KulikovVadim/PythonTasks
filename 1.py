name = "Куликов"
surname = "Вадим"
year = 2003
print(name + "_" + surname + "_" + str(year))
name, surname = surname, name
year += 60
print(name + "_" + surname + "_" + str(year))