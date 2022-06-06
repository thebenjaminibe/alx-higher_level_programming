#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if 0 > idx > len(my_list):
        return my_list
    else:
        new_list = my_list[:]
        for i in range(len(new_list)):
            if i == idx:
                new_list[i] = element
    return new_list
