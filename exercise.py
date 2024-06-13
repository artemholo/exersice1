station_names = ["Чаунская бухта", "Туймазы", "Конги", "Тырка", "Алакуртти"]
station_indexes = [25150, 28712, 32059, 30526, 22301]

assert len(station_names) == 5
assert len(station_indexes) == 5  

assert station_names[0] == "Чаунская бухта"
assert station_indexes[0] == 25150

new_stations_names = 'Тадебяяха', 'Териберка', 'Краснодар Пашковская'
new_station_indexes = 20964, 22028, 34929
station_names.extend(new_stations_names)
station_indexes.extend(new_station_indexes)

assert len(station_names) == 8
assert len(station_indexes) == 8
assert station_names[-1] == 'Краснодар Пашковская'
assert station_indexes[-1] == 34929

station_names.sort()
station_indexes.reverse()

assert station_names[0] == 'Алакуртти'
assert station_indexes[0] == 34929

zipp_station_names_indexes = zip(station_names, station_indexes)
zipp_list = list(zipp_station_names_indexes)

print(station_names)
print(station_indexes)
print(zipp_list)