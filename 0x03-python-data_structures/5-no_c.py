#!/usr/bin/python3
def no_c(my_string):
    new_list = list(my_string)
    new_string = ""
    for i in range(len(new_list)):
        if new_list[i] != "c" and new_list[i] != "C":
            new_string += new_list[i]
    return new_string
