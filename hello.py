ice_cream_rating = 9
sleep_rating = 10
sum_happiness = ice_cream_rating + sleep_rating
happiness_rating = sum_happiness / 2

total_rating = 10
percentage = (happiness_rating / total_rating) * 100

first_name = "Артем"
last_name = "Аликин"
my_name = first_name + " " + last_name

print(happiness_rating)

print(type(ice_cream_rating))
print(type(first_name))
print(type(happiness_rating))

print(f"Меня зовут {first_name}, и я ставлю мороженому {ice_cream_rating} баллов из 10! Я {my_name}, и мой рейтинг удовольствия от сна — {sleep_rating} из 10! Исходя из вышеперечисленных факторов, мой рейтинг счастья составляет {happiness_rating} из 10, или {percentage}%!")

#комментарий