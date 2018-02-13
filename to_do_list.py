to_do_list = []

print("What are items on your to-do list?")
print("Type 'END' when finished with adding items.")

while True:
    new_item = input("> ")

    if new_item.lower() == 'end':
        break

    to_do_list.append(new_item)

print("\nHere's your list:")

for number in range(len(to_do_list)):
    print(str(number + 1) + ') ' + to_do_list[number])

print("\n")
