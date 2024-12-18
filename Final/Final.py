class Planet: #Creates the Planet Objext
    def __init__(self, name, moons, type): #Called when making class
        self.name = name
        self.moons = moons
        self.type = type

    def get_moons(self): #Moon function
        return self.moons

    def get_type(self): #Type function
        return self.type

def display_planets(planets):
    print("\nSelect a planet to find out how many moons it has and its type:")
    for i, planet in enumerate(planets):
        print(f"{i + 1}. {planet.name}")

def main():
    # List of planets, their moons, and Type
    planets = [
        Planet("Mercury", 0, "Rocky"),
        Planet("Venus", 0, "Rocky"),
        Planet("Earth", 1, "Rocky"),
        Planet("Mars", 2, "Rocky"),
        Planet("Jupiter", 92, "Gassy"),
        Planet("Saturn", 145, "Gassy"),
        Planet("Uranus", 27, "Gassy"),
        Planet("Neptune", 14, "Gassy"),
        Planet("Pluto", 5, "Rocky")
    ]


    while True: #Makes a while loop that will stop when the user says to stop
        display_planets(planets)
        try:
            # Ask user for input
            choice = int(input("\nEnter the number corresponding to the planet or 0 to quit: "))
            
            if choice == 0:
                print("Goodbye!")
                break

            if 1 <= choice <= len(planets): #If statement to see what the user chose
                selected_planet = planets[choice - 1]
                print(f"\n{selected_planet.name} has {selected_planet.get_moons()} moon(s) and is a {selected_planet.get_type()} planet.\n")
                
                # Ask if the user wants to go again
                again = input("Do you want to select another planet? (yes/no): ").strip().lower()
                if again != "yes":
                    print("Goodbye!")
                    break
                
            else:
                print("Invalid choice. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()