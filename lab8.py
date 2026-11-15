# PART 1

class RoyalMember:
    def __init__(self, name, age, kingdom):
        self.name = name
        self.age = age
        self.kingdom = kingdom

    def introduce(self):
        print(f"I am {self.name} of {self.kingdom}.")


# PART 2

class Knight(RoyalMember):
    def __init__(self, name, age, kingdom, weapon, battles_won):
        super().__init__(name, age, kingdom)
        self.weapon = weapon
        self.battles_won = battles_won

    def display_details(self):
        print(f"Knight: {self.name}")
        print(f"Kingdom: {self.kingdom}")
        print(f"Weapon: {self.weapon}")
        print(f"Battles won: {self.battles_won}")

    # Task 3: Overriding introduce()
    def introduce(self):
        article = "an" if self.weapon[0].lower() in "aeiou" else "a"
        print(
            f"I am {self.name} of {self.kingdom}. "
            f"I fight with {article} {self.weapon} "
            f"and have won {self.battles_won} battles."
        )

    # Task 5: Tournament method
    def fight(self):
        print(f"Sir {self.name} enters the tournament with a {self.weapon}!")

# PART 3

class Prince(RoyalMember):
    def __init__(self, name, age, kingdom, title):
        super().__init__(name, age, kingdom)
        self.title = title

    def introduce(self):
        print(
            f"I am {self.title} {self.name}, "
            f"heir to the throne of {self.kingdom}."
        )


# TASK 1

arthur = RoyalMember("Arthur", 25, "Eldoria")

print(arthur.name)
print(arthur.age)
print(arthur.kingdom)

arthur.introduce() 

# TASK 2: 

knight1 = Knight("Sir Lancelot", 30, "Eldoria", "Sword", 12)
knight2 = Knight("Sir Cedric", 27, "Northvale", "Spear", 8)

knight1.display_details()
print("Kingdom:", knight1.kingdom)
knight1.introduce()

print()

knight2.display_details()
print("Kingdom:", knight2.kingdom)
knight2.introduce()

# TASK 3

knight3 = Knight("Sir Gareth", 32, "Northvale", "axe", 15)

knight3.introduce()


# PART 4
royal_court = [
    RoyalMember("William", 45, "Eldoria"),
    Knight("Lancelot", 30, "Eldoria", "Sword", 12),
    Knight("Cedric", 27, "Northvale", "Spear", 8),
    Prince("Edward", 21, "Eldoria", "Prince"),
    Prince("Henry", 24, "Northvale", "Prince")
]

for member in royal_court:
    member.introduce()


# PART 5
tournament = [
    Knight("Lancelot", 30, "Eldoria", "Sword", 12),
    Knight("Cedric", 27, "Northvale", "Spear", 8),
    Knight("Gareth", 32, "Northvale", "Axe", 15),
    Knight("Percival", 29, "Eldoria", "Bow", 10)
]

for knight in tournament:
    knight.introduce()
    knight.fight()
    print("Battles won:", knight.battles_won)
    print()

most_experienced = tournament[0]

for knight in tournament:
    if knight.battles_won > most_experienced.battles_won:
        most_experienced = knight

print("Most experienced knight:")
print("Name:", most_experienced.name)
print("Battles won:", most_experienced.battles_won)


# FINAL CHALLENGE
class RoyalGuard(RoyalMember):
    def __init__(self, name, age, kingdom, post):
        super().__init__(name, age, kingdom)
        self.post = post

    def guard_duty(self):
        print(f"{self.name} is assigned to guard the {self.post}.")

    def introduce(self):
        print(
            f"I am {self.name} of {self.kingdom}. "
            f"I serve as a Royal Guard at the {self.post}."
        )

print("\n========== FINAL CHALLENGE ==========")

guard1 = RoyalGuard("Thomas", 35, "Eldoria", "Castle Gate")
guard2 = RoyalGuard("Richard", 40, "Northvale", "Throne Room")


royal_court.append(guard1)
royal_court.append(guard2)


for member in royal_court:
    member.introduce()

print("\nRoyal Guard Duties:")

guard1.guard_duty()
guard2.guard_duty()

