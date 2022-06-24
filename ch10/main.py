import csv
from pprint import pprint
import sqlite3

from Customer import Customer


def main():
    with sqlite3.connect('people.db') as con:
        cur = con.cursor()
        for row in cur.execute('SELECT * FROM customers'):
            c = Customer(*row)
            print(c)



def main_insert():
    with sqlite3.connect('people.db') as con:
        cur = con.cursor()

        with open('MOCK_DATA.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sql = f"""INSERT INTO customers(first_name,last_name,email,gender,ip_address,is_customer)
                VALUES('{row['first_name'].replace("'","''")}','{row['last_name'].replace("'","''")}','{row['email']}','{row['gender']}','{row['ip_address']}',{row['is_customer']})                
                """
                cur.execute(sql)
                print(sql)
        con.commit()

if __name__ == "__main__":
    main()