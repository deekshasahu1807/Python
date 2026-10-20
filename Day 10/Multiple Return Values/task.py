def format_name(f_name, l_name):
    if (f_name == "") or (l_name == ""):
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(format_name(first_name, last_name))
