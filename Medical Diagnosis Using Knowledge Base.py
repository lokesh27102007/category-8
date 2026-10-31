symptoms = input("Do you have fever? (yes/no): ").lower()
cough = input("Do you have cough? (yes/no): ").lower()

if symptoms == "yes" and cough == "yes":
    print("Possible diagnosis: Flu")
elif symptoms == "yes":
    print("Possible diagnosis: Fever")
elif cough == "yes":
    print("Possible diagnosis: Common Cold")
else:
    print("No common symptoms detected")
