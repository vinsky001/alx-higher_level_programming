#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda x:if x == search else x, mylist))
    return (new_list)