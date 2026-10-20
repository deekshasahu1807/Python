def format_name(f_name, l_name):
    """ Format first name and last name in title format"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    """ Return formatted title """
    return f"{formated_f_name} {formated_l_name}"

""" This function is used to convert the name in title format"""
formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)
print(length)