def validate_ip(ip):

    ip = ip.strip()

    if ip.count(".") != 3:
        return False

    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for part in parts:

        if not part.isdigit():
            return False

        if int(part) < 0 or int(part) > 255:
            return False

    return True


ip_address = input("Enter an IP address: ")

if validate_ip(ip_address):
    print("Valid IP address")
else:
    print("Invalid IP address")