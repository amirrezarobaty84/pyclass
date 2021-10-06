import sqlite3

print("HELLO DEAR :) \nDon't have GOOD DAY, Have a GREAT DAY \nI  can do the following: \
\n1-Add some body if you want\n2-delete some body if you want \n3-Search any body \n5-Show your list")

while True:
    REQUEST = input("what can i do for you ?!? \n( search - add - delete - show_list ) \n")
    if REQUEST  == 'add':
        first_name = input("what's her/his first_name ? \n")
        last_name = input("what's her/his last_name ? \n")
        phone_number = int(input("what's her/his phone_number ?\n"))
        connection = sqlite3.connect('contacts.db')
        query = "INSERT INTO person VALUES (?,?,?)"
        cursor = connection.cursor()
        cursor.execute(query, (first_name, last_name, phone_number))
        connection.commit()
        print("{} {} with this phone_number {} added :)".format(first_name, last_name, phone_number))

    elif REQUEST  == 'delete':
        first_name = input("what's her/his first_name ? \n")
        last_name = input("what's her/his last_name ? \n")
        conn = sqlite3.connect('contacts.db')
        query = "DELETE FROM person WHERE first_name = ? AND last_name = ?"
        cursor = conn.cursor()
        cursor.execute(query, (first_name, last_name))
        conn.commit()
        print("{} {} deleted :)".format(first_name, last_name, phone_number))


    elif REQUEST  == 'search':
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        first_name = input("what's her/his first_name ? \n")
        last_name = input("what's her/his last_name ? \n")
        c.execute(f'SELECT * from person where First_name=? and Last_name =? ',  (first_name, last_name))
        back = c.fetchall()
        for i in back:
                print(f'First_name: {i[0]} \t  Last_name: {i[1]} \t phone_number: {i[2]}')
                conn.commit()

    elif REQUEST  == 'show_list':
        connection = sqlite3.connect('contacts.db')
        cursor = connection.cursor()
        query = "select * from person"
        cursor.execute(query)
        rows = cursor.fetchall()
        row = cursor.fetchone()
        for i in rows:
            print(f'First_name: {i[0]} \t  Last_name: {i[1]}  \t phone_number: {i[2]} ')
        connection.commit()

    
    another_request = input("Do you have another_request ?\n")
    
    elif another_request == 'yes':
        pass
    elif another_request == 'no':
        print("Have a grreat Day :)")
        break
        

    
