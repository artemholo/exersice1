print('Введите индекс месяца от 0 до 11: ')
selected_mounth_index = input()
selected_mounth_index = selected_mounth_index + 1

months = ['Январе', 'Феврале', 'Марте', 'Апреле', 'Майе', 'Июне', 'Июле', 'Августе', 'Сентябре', 'Октябре', 'Ноябре', 'Декабре']
average_temp = [-4.8, -5.0, -1.0, 5.2, 11.5, 16.1, 19.1, 17.4, 12.4, 6.2, 0.9, -2.5]

print_statement = f"Средняя температура в Санкт-Петебурге в {months[int(selected_mounth_index)]} составляет {average_temp[int(selected_mounth_index)]}"
print(print_statement)