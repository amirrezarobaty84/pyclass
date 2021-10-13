import sqlite3

print("-----------PHONE BOOK-----------")
print("0.QUIT")
print("1.ADD PHONE NUMBER TO THE PHONE BOOK")
print("2.SEARCH PHONE NUMBER TN THE PHONE BOOK")
print("3.DELETE PHONE NUMBER TO THE PHONE BOOK")
print("4.SHOW your PHONE BOOK")
while True:
    n=int(input("enter NUMBER{0/1/2/3/4}:-"))
    if n==1:
        first_name = input("enter your first name ? \n")
        last_name = input("enter your last name ? \n")
        phone_number = int(input("enter your number ?\n"))
        connection = sqlite3.connect('telephone.db')
        query = "INSERT INTO telephone VALUES (?,?,?)"
        cursor = connection.cursor()
        cursor.execute(query, (first_name, last_name, phone_number))
        connection.commit()
        print("DONE")

    elif n==2:
        connection = sqlite3.connect('telephone.db')
        cursor = connection.cursor()
        first_name = input("enter your first name ? \n")
        last_name = input("enter your last name ? \n")
        cursor.execute(f'SELECT * from telephone where First_name=? and Last_name =? ',  (first_name, last_name))
        back = cursor.fetchall()
        for b in back:
                print(f'First_name: {b[0]} \t  Last_name: {b[1]} \t phone_number: {b[2]}')
                connection.commit()

    elif n == 3 :
        first_name = input("enter your first name ? \n")
        last_name = input("enter your last name ? \n")
        connection = sqlite3.connect('telephone.db')
        query = "DELETE FROM telephone WHERE first_name = ? AND last_name = ?"
        cursor = connection.cursor()
        cursor.execute(query, (first_name, last_name))
        connection.commit()
        print("DONE")

    elif n == 4 :
        onnection = sqlite3.connect('telephone.db')
        cursor = connection.cursor()
        query = "select * from telephone"
        cursor.execute(query)
        rows = cursor.fetchall()
        row = cursor.fetchone()
        for i in rows:
            print(f'First_name: {i[0]} \t  Last_name: {i[1]}  \t phone_number: {i[2]} ')
        connection.commit()


    elif n==0:
        break
