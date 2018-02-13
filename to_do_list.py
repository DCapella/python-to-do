def show_help():
    print("""
What are items on your to-do list?
Type 'END' to finish.
Type 'HELP' for this help.
Type 'SHOW' to see your current list.
""")

def show_list(to_do_list):
    print("\nHere's your list:")

    for number in range(len(to_do_list)):
        print(f"%s) %s" % (str(number + 1), to_do_list[number]))

def add_to_list(to_do_list, new_item):
    to_do_list.append(new_item)
    print(f"Added %s. List now has %s items." % (new_item, len(to_do_list)))



def main():
    to_do_list = []
    show_help()
    while True:
        new_item = input("> ")

        if new_item.lower() == 'end':
            break
        elif new_item.lower() == 'help':
            show_help()
            continue
        elif new_item.lower() == 'show':
            show_list(to_do_list)
            continue
        add_to_list(to_do_list, new_item)

    show_list(to_do_list)

main()
