#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        result = [0]*list_length
        for i in range(list_length):
            try:
                result[i]=my_list_1[i]/my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
                continue
            except (TypeError, ValueError):
                print("wrong type")
                continue
    except IndexError:
        print("out of range")
    finally:
        return result
