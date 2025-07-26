import sqlite3
import hashlib

# menu driven

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
is_loged_in = 0

while True :

    print("-------------- Welcome to User Management System ---------------")
    print("1.Register")
    print("2.Login")
    print("3.Logout")
    print("4.Change Password")
    print("5.exit")
    print("-----------------------------------------------------------------")
    choice = int(input("Enter your Choice:"))

    if choice == 1:
        user_name = input("create Username:").strip()
        user_pass = input("Create Password:").strip()

        if not user_name or not user_pass:
            print("username or password cannot be empty.")
            continue

        if len(user_pass) < 6:
            print("password length should be at least 6 character long.")
            continue

        else :
            hashed_pass = hash_password(user_pass)

            conn = sqlite3.connect("user_management_system.db")
            cursor = conn.cursor()

            data = cursor.execute("""CREATE TABLE IF NOT EXISTS registrationThree(
            username TEXT PRIMARY KEY,
            password TEXT,
            Login INT
            )""")

            try:
                cursor.execute("INSERT INTO registrationThree (username, password,Login) VALUES (?, ?, ?)", (user_name, hashed_pass,is_loged_in))
                print("Successfully Registered.")
                conn.commit()
            except sqlite3.IntegrityError:
                print("Username already exist, Try another user name.")

        conn.close()
    if choice == 2:

        print("-------- welcome to login page ---------")
        user_name = input("Enter username").strip()
        user_pass = input("Enter Password").strip()

        if not user_name or not user_pass:
            print("Username or Password cannot be empty.")
            continue

        if is_loged_in == 1:
            print("already logged in , first Logout and try again.")
            continue
        else:
            hashed_pass = hash_password(user_pass)
            conn = sqlite3.connect("user_management_system.db")
            cursor = conn.cursor()

            cursor.execute("select * from registrationThree WHERE username = ? AND password = ?",(user_name,hashed_pass))
            result = cursor.fetchone()

            if result:
                is_loged_in = 1
                cursor.execute("UPDATE registrationThree SET Login = 1 WHERE username =?",(user_name,))
                conn.commit()
                print("Login Successfully.")
            else:
                print("Credential not matched , Try again")

    if choice == 3:
        print("-------- Logout page ---------")
        user_name = input("Enter username to Logout:").strip()

        if not user_name:
            print("username cannot be empty.")
            continue
        else :
            conn = sqlite3.connect("user_management_system.db")
            cursor = conn.cursor()

            cursor.execute("select * from registrationThree WHERE username = ? AND Login = 1", (user_name,))
            result = cursor.fetchone()

            if result :
                cursor.execute("UPDATE registrationThree SET Login = 0 WHERE username =?",(user_name,))
                conn.commit()
                print("Logout Successfully")

            else:
                print("you are not able to Logout , first login")

    if choice == 4:
        print("-------- Change Password ---------")
        user_name = input("Enter username to change Password:").strip()

        if not user_name:
            print("Username cannot be empty.")
            continue


        conn = sqlite3.connect("user_management_system.db")
        cursor = conn.cursor()


  # check if user exist

        cursor.execute("select * from registrationThree WHERE username = ?", (user_name,))
        result = cursor.fetchone()

        if result :
            current_pass = input("Enter your current password: ").strip()
            hashed_current_pass = hash_password(current_pass)

            # Verify current password
            if hashed_current_pass != result[1]:
                print("Current password is incorrect. Try again.")
                conn.close()
                continue

            # Ask for new password
            new_pass = input("Enter new password (min 6 chars): ").strip()

            if not new_pass:
                print("New password cannot be empty.")
            elif len(new_pass) < 6:
                print("Password must be at least 6 characters long.")
            elif hash_password(new_pass) == hashed_current_pass:
                print("New password cannot be the same as the current password.")
            else:
                hashed_new_pass = hash_password(new_pass)
                cursor.execute("UPDATE registrationThree SET password = ? WHERE username = ?",
                               (hashed_new_pass, user_name))
                conn.commit()
                print("Password reset successfully.")
        else:
            print("Username not found. Please register first.")

        conn.close()



    if choice == 5:
        print("Exit from the System.5")
        break

