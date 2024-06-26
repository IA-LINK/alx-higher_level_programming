#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
script should take 3 arguments: mysql username, mysql password
and database name (no argument validation needed)
must use the module MySQLdb (import MySQLdb)
script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""
import MySQLdb as mysql
from sys import argv


def connection(connect, username, password, database, prt):
    """
        lists all row in states table
        connect:port,
        username: username of the user,
        password: password of the database,
        database: the database to use,
        prt: port to connect.
    """
    mydb = mysql.connect(
        host=connect,
        user=username,
        passwd=password,
        db=database,
        port=prt
    )

    # create cursor
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # close connections
    cursor.close()
    return mydb


if __name__ == '__main__':
    mydbase = connection('localhost', argv[1], argv[2], argv[3], 3306)
    mydbase.close()