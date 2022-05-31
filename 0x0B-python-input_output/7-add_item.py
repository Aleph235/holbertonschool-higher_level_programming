#!/usr/bin/python3
"""create a json file with given imput"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    op = my_file = load_from_json_file("add_item.json")
except Exception as e:
    op = []
for elem in sys.argv[1:]:
    op.append(elem)
save_to_json_file(op, "add_item.json")
