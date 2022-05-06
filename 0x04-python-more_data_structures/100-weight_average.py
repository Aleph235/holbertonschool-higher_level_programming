#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        simple_list = list(sum(my_list, ()))
        score_list = simple_list[::2]
        weight_list = simple_list[1::2]
        total = sum([score_list[i]*weight_list[i] for i in
                     range(len(score_list))])
        average = total/sum(weight_list)
        return average
    else:
        return 0
