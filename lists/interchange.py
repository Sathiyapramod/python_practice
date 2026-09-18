data = {"name": "John", "tech": "python", "city": "New York"}
# { “John” : “name, “python”: “tech”, “New York” : “city }

result = {}

for key in data:
    new_key = data[key]
    new_val = key
    result[new_key] = new_val
# print(result)


# keys()
print(data.keys())

# values()
print(data.values())

# items()
print(data.items())

for k, v in data.items():
    print(k, "=", v)
