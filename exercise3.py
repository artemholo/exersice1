basename = "Station"
print(basename)

filenames = []
print(filenames)

for i in range(0, 21):
    station = f"{basename}{i}.txt"
    filenames.append(station)
    #print(station)

print(filenames)
print("".join(filenames))