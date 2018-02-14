import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_help():
    clear_screen()
    print("""
What are items on your to-do list?
Type 'EXIT' or 'Q' to quit.
Type 'HELP' for this help.
Type 'SHOW' to see your current list.
Type 'REMOVE' to delete an item from your list.
""")

def show_list(to_do_list):
    clear_screen()

    print("\nHere's your list:")
    print("-"*10)

    for number in range(len(to_do_list)):
        print(f"%s. %s" % (str(number + 1), to_do_list[number]))

    print("-"*10)

def remove_from_list(to_do_list):
    show_list(to_do_list)
    temp_remove = input("What would you like to remove?\n> ")
    try:
        to_do_list.remove(temp_remove)
    except ValueError:
        print("'{}' was not in your list.".format(temp_remove))
        input("ENTER/RETURN to continue")
        remove_from_list(to_do_list)
    show_list(to_do_list)

def add_to_list(to_do_list, new_item):
    show_list(to_do_list)
    if len(to_do_list):
        position = input("Where should I add {}?\n"
                         "Press ENTER/RETURN to add to the end of the list\n"
                         "> ".format(new_item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        to_do_list.insert(position-1, new_item)
    else:
        to_do_list.append(new_item)

    show_list(to_do_list)


def main():
    to_do_list = []
    show_help()
    while True:
        new_item = input("What will you add to your list?\n> ")

        if new_item.lower() == 'exit' or new_item.lower() == 'q':
            break
        elif new_item.lower() == 'help':
            show_help()
            continue
        elif new_item.lower() == 'show':
            show_list(to_do_list)
            continue
        elif new_item.lower() == 'remove':
            remove_from_list(to_do_list)
        else:
            add_to_list(to_do_list, new_item)

    show_list(to_do_list)

main()
