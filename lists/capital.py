"""
Write a Python program for the following
Question:
Input    	data ={"cat":"Meow","dog": "Bark","cow": "Maa"}
---------------
Expected Output : { "CAT":"Meow","DOG": "Bark","COW": "Maa"  }
Key - Turned as Uppercase  / Capital Letters
Val - retain the Same
"""

data = {"cat": "Meow", "dog": "Bark", "cow": "Maa"}

# Expected Output : {"CAT":"Meow","DOG": "Bark","COW": "Maa"}


# for key in data.copy():
#     new_key = key.upper()
#     old_val = data[key]
#     data[key.upper()] = old_val
#     del data[key]
# print(data)


result = {}

for key in data:
    # new key
    new_key = key.upper()

    # old value
    old_val = data[key]

    # print(new_key, old_val)
    result[new_key] = old_val
print(result)
