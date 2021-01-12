def search(data, value):
    index = 0
    found = False
    while index < len(data) and not found:
        if data[index] == value:
            found = True
        else:
            index += 1
    return found

my_data = [123, 32, 234, 43, 324, 65]
print(f"value 43 found: {search(my_data, 43)}")