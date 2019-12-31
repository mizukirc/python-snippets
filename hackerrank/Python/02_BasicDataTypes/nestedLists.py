#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/nested-list/

 if __name__ == '__main__':
        nested_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        nested_list.append([name, score])
        student_dict = dict(nested_list)

    student_dict = dict(nested_list)

    vals_set = sorted(set(student_dict.values()))
    second_val = list(vals_set)[1]

    listOfKeys = [key for (key, val) in student_dict.items() if val == second_val]
    listOfKeys = sorted(listOfKeys)

    for i in range(len(listOfKeys)):
        print(listOfKeys[i])    
 

    

