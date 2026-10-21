from rich import print

print("[bold red]Welcome to Protect the Pizza!")
print("Your delivery car has broken down!\nMake the right choices so the pizza arrives hot and on time.")

print("\n[bold yellow]Smoke is pouring from the hood.[/bold yellow] What do you do?")
print("1) Pull over and check the engine")
print("2) Keep driving and hope for the best")
first_choice = input("(1,2)")

if first_choice == "1":
    print("\nYour car is low on coolant. A gas station is 10 minutes away on foot.")
    print("1) Walk to the gas station and buy coolant")
    print("2) Pour your giant soda into the radiator")
    second_choice = input("(1,2) ")

    if second_choice == "1":
        print("You walk to the station, but the pizza gets cold while you're gone.")
    elif second_choice == "2":
        print("The soda sizzles and the engine hisses, z Somehow... it works!")
    else:
        print("Invalid choice. The pizza gets colder.")

elif first_choice == "2":
    print("\nYour car drives for a few mins and then explodes!")
    print("[bold red]GAME OVER!!!!!![/bold red]")

else:
    print("Invalid choice. The pizza gets colder.")