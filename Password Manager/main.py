import time
import os
import sqlite3
connection = sqlite3.connect('container.db')
cursor = connection.cursor()


print("┌─────────────────────────────────┐")
print("│ Welcome to the Password Manager │")
print("└─────────────────────────────────┘")


def display_options():
    print("┌───────────────────────────────┐")
    print("│      1.New User sign Up       │")
    print("│      2.user login             │")
    print("│      3.Delete user login      │")
    print("│      4.Exit                   │")
    print("└───────────────────────────────┘")
    print()


def clean():
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')


while True:
    display_options()
    choice = input("Enter your choice: ")
    if choice == "1":
        login_username = input("Enter your username: ")
        login_password = input("Enter your password: ")

        print()
        old_user = list(cursor.execute(f"""SELECT username FROM login_credentials  
                                           WHERE username = ('{login_username}');"""))
        try:
            if login_username == old_user[0][0]:
                print("Username already exists..Please try again with a different username.")
        except Exception:
            command = f"""CREATE TABLE IF NOT EXISTS {login_username} (website_name VARCHAR(255), 
                                                                 website_url VARCHAR(256), 
                                                                 username VARCHAR(255), 
                                                                 password VARCHAR(255));"""
            cursor.execute(command)
            connection.commit()
            cursor.execute(f"""INSERT INTO login_credentials (username, password) 
                               VALUES ('{login_username}','{login_password}');""")
            connection.commit()
            print(f"You have successfully signed in as {login_username}!")

    elif choice == "2":
        login_username = input("Enter your username: ")
        login_password = input("Enter your password: ")

        print()
        user = list(cursor.execute(f"""SELECT username FROM login_credentials 
                                       WHERE username = ('{login_username}');"""))
        pa_ss = list(cursor.execute(f"""SELECT password FROM login_credentials 
                                        WHERE password = ('{login_password}');"""))
        connection.commit()
        try:
            if login_username == user[0][0] and login_password == pa_ss[0][0]:
                clean()
                print()
                print("You have successfully Logged in!")
                print()

            while True:
                print("┌─────────────────────────────┐")
                print("│●Options:                    │ ")
                print("│     1.Add a Password        │ ")
                print("│     2.Remove a password     │ ")
                print("│     3.update a Password     │ ")
                print("│     4.Fetch a Password      │")
                print("│     5.Exit                  │")
                print("└─────────────────────────────┘")
                print()

                option = int(input("Enter your option: "))
                if option == 1:
                    website_name = input("Enter the website name: ").capitalize().strip()
                    website_url = input("Enter the website url: ")
                    username = input("Enter the username: ")
                    password = input("Enter the password: ")
                    old_web = list(cursor.execute(f"""SELECT website_name FROM {login_username}  
                                                      WHERE website_name = ('{website_name}');"""))
                    print()
                    try:
                        if website_name == old_web[0][0]:
                            print("The website already exists in the database!")
                            print("Please try again")
                            print("_" * 33)
                    except Exception:
                        cursor.execute(f"""INSERT INTO {login_username} (website_name,website_url,username,password) 
                                           VALUES ("{website_name}","{website_url}","{username}","{password}"); """)
                        print("Your Password has been added!")
                        print("_" * 33)
                        time.sleep(3)
                        connection.commit()

                elif option == 2:
                    website_name = input("Enter the website name to remove from database: ").capitalize().strip()
                    website = list(cursor.execute(f"""SELECT website_name FROM {login_username} 
                                                  WHERE website_name = ('{website_name}');"""))
                    try:
                        if website_name == website[0][0]:
                            cursor.execute(f"""DELETE FROM {login_username} WHERE website_name = ("{website_name}");""")
                            connection.commit()
                            print("The website has been removed from the database.")
                            print("_" * 33)
                    except IndexError:
                        print("There is no such website in the database.")
                        print("_" * 33)
                    time.sleep(3)

                elif option == 3:
                    website_name = input("Enter the website name: ").capitalize().strip()
                    password = input("Enter the new password: ")
                    website = list(cursor.execute(f"""SELECT website_name FROM {login_username} 
                                                  WHERE website_name = ('{website_name}');"""))
                    try:
                        if website_name == website[0][0]:
                            cursor.execute(f"""UPDATE {login_username} SET password = '{password}' 
                                               WHERE website_name = ("{website_name}");""")
                            print("You have successfully updated the password")
                            print("_" * 33)
                            print()
                            connection.commit()
                    except IndexError:
                        print("There is no such website in the database to update the password.")
                        print("_" * 33)
                    time.sleep(3)

                elif option == 4:
                    website_name = input("Enter the website name to fetch your password: ").capitalize().strip()
                    website = list(cursor.execute(f"""SELECT website_name FROM {login_username} 
                                                      WHERE website_name = ('{website_name}');"""))
                    try:
                        if website_name == website[0][0]:
                            password = list(cursor.execute(f""" SELECT password FROM {login_username} 
                                                                WHERE website_name = ("{website_name}");"""))
                            print("──────────────────────────────")
                            print(" Website Name   │   Password")
                            print(f" {website_name}         │   {password[0][0]}")
                            print("───────────────────────────────")
                            print()
                            connection.commit()
                    except IndexError:
                        print("There is no such website in the database to fetch your password!.")
                        print("_" * 33)
                        print()
                    time.sleep(3)

                elif option == 5:
                    print("Exiting...")
                    print()
                    break

                else:
                    print("Invalid")

        except IndexError:
            print("Invalid username or password!")
            print()
            print("Please try again.")
            print()

    elif choice == "3":
        login_username = input("Enter the username to delete login details: ")
        password = input("Please type your password for confirmation: ")
        user = list(cursor.execute(f"""SELECT username FROM login_credentials 
                                       WHERE username = ("{login_username}");"""))
        connection.commit()
        pass_word = list(cursor.execute(f"""SELECT password FROM login_credentials 
                                            WHERE password = ("{password}");"""))
        connection.commit()
        try:
            if login_username == user[0][0] and password == pass_word[0][0]:
                cursor.execute(f"""DELETE FROM login_credentials WHERE username = ("{login_username}");""")
                connection.commit()
                cursor.execute(f"""DROP TABLE {login_username};""")
                connection.commit()
                clean()
                print()
                print("You have successfully deleted the Login details!")
                print("_" * 33)
        except IndexError:
            print("Invalid username or password!")
            print("_" * 33)

    elif choice == "4":
        print("Exited!")
        exit()
    else:
        print("──────────────────────────────")
        print(" Please enter a valid choice!")
        print("──────────────────────────────")
        print()
