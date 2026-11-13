incident = {
    "username": "admin",
    "ip_address": "192.168.1.50",
    "event_type": "Failed Login",
    "risk_level": "Medium"
}

print("Username:", incident["username"])
print("IP Address:", incident["ip_address"])

incident["status"] = "Open"

incident["risk_level"] = "High"

incident.pop("event_type")

print("\nRemaining Data")

for key, value in incident.items():
    print(key, ":", value)

print("\nTotal key-value pairs:", len(incident))