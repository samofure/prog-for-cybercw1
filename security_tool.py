correct_username = "admin"
correct_password = "Cyber123!"


def security_event_counter():
    correct = 0
    incorrect = 0

    for i in range(10):
        password = input("Enter password: ")

        if password == correct_password:
            correct += 1
        else:
            incorrect += 1

    percentage = (incorrect / 10) * 100

    print("Correct passwords:", correct)
    print("Incorrect passwords:", incorrect)
    print("Incorrect percentage:", percentage)

    if percentage > 50:
        print("Security Alert Raised!")


def brute_force_simulation():

    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:

        guess = input("Guess password: ")
        attempts += 1

        if guess == correct_password:
            print("Password found")
            break
    else:
        print("Maximum attempts reached")


def login_authentication():

    failed_attempts = 0

    while failed_attempts < 3:

        username = input("Username: ")
        password = input("Password: ")

        if username == correct_username and password == correct_password:
            print("Authentication successful")
            return

        else:
            failed_attempts += 1
            print("Authentication failed")

    print("Account frozen for 24 hours")


while True:

    print("\nSECURITY MENU")
    print("1. Security Event Counter")
    print("2. Brute Force Simulation")
    print("3. Login Authentication")
    print("4. Exit")

    choice = input("Select option: ")

    if choice == "1":
        security_event_counter()

    elif choice == "2":
        brute_force_simulation()

    elif choice == "3":
        login_authentication()

    elif choice == "4":
        print("Thank you for using the security tool")
        break

    else:
        print("Invalid choice")