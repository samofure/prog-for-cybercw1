import random
from datetime import datetime

correct_username = "admin"
correct_password = "Cyber123!"

while True:

    username = input("Enter username: ")
    password = input("Enter password: ")

    event_id = random.randint(1000, 9999)

    if username == correct_username and password == correct_password:

        print("\nEvent ID:", event_id)
        print("Username:", username)
        print("Event: Successful Login")
        print("Timestamp:", datetime.now())

        print("Access Granted")
        break

    else:

        print("\nEvent ID:", event_id)
        print("Username:", username)
        print("Event: Failed Login")
        print("Timestamp:", datetime.now())

        print("Access Denied")