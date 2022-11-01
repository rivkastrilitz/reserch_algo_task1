import re
from doctest import testmod
from typing import Any

import function


################### Q1 ###########################

def safe_call(f: function, **kwargs):
    '''
       This function make a safe call to another function
       by validating argument types
       returns the f call on arguments or an error.
       Define input and expected output:
        >>> safe_call(f=fun, x=3, y=2.0, z=1)
        5.0
        >>> safe_call(f=fun_add, x=4, y=2.0, z=1 )
        7.0
   '''

    # go over all argument and check their type
    for key, arg in kwargs.items():
        # if arg name appear in annotation
        if key in f.__annotations__:
            arg_type = f.__annotations__[key]
            # if type of argument don't mach type of annotation
            if not isinstance(arg, arg_type):
                raise Exception('args type dose not fit the annotation ')
    return f(**kwargs)


def fun(x: int, y: float, z):
    return (x + y) * z


def fun_add(x: int, y: float, z):
    return x + y + z


######################### Q2 ######################

def bfs(src: Any, dest: Any, find_neighbor: function) -> list:

    '''
          This function find a path between
          src and dest
          returns the path that was found .
          Define input and expected output:
           >>> bfs((0, 0), (2, 2), nei_func)
           [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

      '''

    path_list = [[src]]
    path_index = 0
    # save previously visited nodes
    previous_nodes = {src}
    if src == dest:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]

        # if dest in neighbors finish
        if dest in find_neighbor(last_node):
            current_path.append(dest)
            return current_path
        # Add new paths
        for next_node in find_neighbor(last_node):
            if not next_node in previous_nodes:
                # copy current path
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path was found
    return []

def nei_func(node):
    (x,y) = node
    return [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]




################## Q3 #######################

def num_sort(test_string):
    return list(map(float, re.findall(r'\d+', test_string)))[0]


def sort_rec(container):
    if isinstance(container, list):
        str_container = []
    elif isinstance(container, tuple):
        str_container = []
    elif isinstance(container, dict):
        str_container = {}
    elif isinstance(container, set):
        str_container = set()
    for element in container:
        if isinstance(element, list) or isinstance(element, dict) or isinstance(element, tuple) or isinstance(element,
                                                                                                              set):
            sorted_element = sort_rec(element)
            my_string = ''
            if isinstance(element, list):
                my_string += "["
                for x in sorted_element:
                    my_string += str(x) + ","
                my_string = my_string[:-1] + ']'
            elif isinstance(element, dict):
                my_string += "{"
                for x in sorted_element:
                    my_string += str(x) + ":" + str(sorted_element[x]) + ","
                my_string = my_string[:-1] + '}'
            elif isinstance(element, tuple):
                my_string += "("
                for x in sorted_element:
                    my_string += str(x) + ","
                my_string = my_string[:-1] + ')'
            elif isinstance(element, set):
                my_string += "{"
                for x in sorted_element:
                    my_string += str(x) + ","
                my_string = my_string[:-1] + '}'

            if isinstance(container, list):
                str_container.append(my_string)
            elif isinstance(container, tuple):
                str_container.append(my_string)
            elif isinstance(container, dict):
                str_container[element] = my_string
            elif isinstance(container, set):
                str_container.add(my_string)
        else:
            if isinstance(container, list):
                str_container.append(str(element))
            elif isinstance(container, tuple):
                str_container.append(str(element))
            elif isinstance(container, dict):
                str_container[element] = str(container[element])
            elif isinstance(container, set):
                str_container.add(str(element))

    if isinstance(str_container, list):
        str_container = list(sorted(str_container, key=num_sort))
    elif isinstance(str_container, tuple):
        str_container.sort(key=num_sort)
    elif isinstance(str_container, dict):
        dict(sorted(str_container.items(key=num_sort)))
    elif isinstance(str_container, set):
        str_container = sorted(str_container,key=num_sort)
    return str_container


def printSorted(container):
    '''
           This function sorts a deep data
           returns the sorted data set .
           Define input and expected output:
            >>> printSorted([4, 3, (100, 67), 23, 0.4, 2, {23, 4}])
            [0.4,2,3,4,{4,23},23,(67,100)]

   '''

    str_cont = sort_rec(container)
    my_str = ""
    if isinstance(str_cont, list):
        my_str += "["
        for x in str_cont:
            my_str += str(x) + ","
        my_str = my_str[:-1] + ']'
    elif isinstance(str_cont, dict):
        my_str += "{"
        for x in str_cont:
            my_str += str(x) + ":" + str(str_cont[x]) + ","
        my_str = my_str[:-1] + '}'
    elif isinstance(str_cont, tuple):
        my_str += "("
        for x in str_cont:
            my_str += str(x) + ","
        my_str = my_str[:-1] + ')'
    elif isinstance(str_cont, set):
        my_str += "{"
        for x in str_cont:
            my_str += str(x) + ","
        my_str = my_str[:-1] + '}'
    print(my_str)





# examples
if __name__ == '__main__':

    # q2
    print(bfs((0, 0), (2, 2), nei_func))
    print(bfs((0, 1), (2, 2), nei_func))
    print(bfs((2, 2), (2, 0), nei_func))
    testmod(name='bfs', verbose=True)

    # q1
    print(safe_call(fun_add, x=5, y=0.0, z=7))
    print(safe_call(fun, x=5, z=6, y=7.3))
    testmod(name='safe_call', verbose=True)


    # q3
    printSorted([4, 3, (100, 67), 23, 0.4, 2, {23, 4}])
    testmod(name='printSorted', verbose=True)

