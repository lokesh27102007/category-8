traffic_light = input("Enter traffic light (red/green/yellow): ").lower()
obstacle = input("Is there an obstacle? (yes/no): ").lower()

if obstacle == "yes":
    print("Action: Stop the vehicle")
elif traffic_light == "red":
    print("Action: Stop the vehicle")
elif traffic_light == "yellow":
    print("Action: Slow down")
elif traffic_light == "green":
    print("Action: Move forward")
else:
    print("Invalid input")
