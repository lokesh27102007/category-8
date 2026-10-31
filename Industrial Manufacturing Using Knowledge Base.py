machine_status = input("Enter machine status (normal/fault): ").lower()
temperature = int(input("Enter machine temperature: "))

if machine_status == "fault":
    print("Action: Stop the machine")
elif temperature > 80:
    print("Action: Cool down the machine")
else:
    print("Action: Continue production")
