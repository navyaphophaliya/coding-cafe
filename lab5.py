def cast_spell():
    print("Sparkles everywhere!")
    print("Spell complete!")

cast_spell()


def calculate_chest_volume(length, width, height):
    return length * width * height

volume = calculate_chest_volume(5, 4, 3)
print(volume)


def upgrade_weapon(weapon_name, material="Iron", level=1):
    power = level * 10
    return f"Upgraded {weapon_name} with {material} to level {level}! Power is now {power}."
result = upgrade_weapon("sword", level=5)
print(result)


daily_steps = 9500

def walk_to_the_village_1():
    global daily_steps
    daily_steps = daily_steps + 500
    print(f"Quest complete! Total steps: {daily_steps}")

walk_to_the_village_1()

tigers = 95

def count_tigers():
    tigers = 15
    print(tigers)

print(tigers)
count_tigers()
print(tigers)


import random
import math

radius = random.randint(1, 100)
area = math.pi * math.pow(radius, 2)

print("Radius:", radius)
print("Area:", area)




steps = int(input("Enter your daily step count: "))
water = float(input("Enter your fluid intake in liters: "))

def evaluate_stamina(steps, water):
    if steps > 10000 and water > 3:
        message = "Quest Ready for the Triund Trek!"
    else:
        message = "Rest and Hydrate at the Tavern."
    return message

result = evaluate_stamina(steps, water)

with open("ranger_stamina_log.txt", "a") as file:
    file.write(result + "\n")

print(result)





import time
import random

def attempt_trial(hero_name):
    print(f"{hero_name} is entering the Trial of Shadows...")
    time.sleep(2)

    score = random.randint(1, 100)

    if score >= 50:
        fate = "survived"
    else:
        fate = "failed"

    with open("hall_of_fame.txt", "a") as file:
        file.write(f"{hero_name} scored {score} and {fate}.\n")

    return score

final_score = attempt_trial("Aria")
print(f"Game over! Final score: {final_score}")
