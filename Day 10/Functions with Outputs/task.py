def format_name(f_name, l_name):
    return f_name.title() + ' ' + l_name.title()

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = format_name(first_name, last_name)
print(full_name)