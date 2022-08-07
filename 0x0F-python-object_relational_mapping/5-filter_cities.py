#!/usr/bin/python3
"""list all cities of given argument"""
from sys import argv
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    args = argv[4].split(';')
    state_name = args[0].strip('"\'')

    cur = db.cursor()
    cur.execute("SELECT cities.name\
                FROM cities JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name = '{}'\
                ORDER BY cities.id ASC".format(state_name))
    query_rows = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))
    cur.close()
    db.close()
