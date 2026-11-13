import security_tools

password = input("Enter password: ")
ip_address = input("Enter IP address: ")

if security_tools.validate_password(password):
    print("Password is valid")

else:
    print("Password is weak")
    print("Suggested Password:",
          security_tools.generate_password())

if security_tools.validate_ip(ip_address):
    print("IP address is valid")

else:
    print("IP address is invalid")