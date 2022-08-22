data = {"a": 1, "b": 4, "c": 9, "d": 16, "h": 25, "g": 36, "f": 49, "e": 64, "r": 81, "y": 100}
new_data = {key: value for value, key in data.items()}
print(new_data)

