
"""
My name is Krish
Roll no. - 2501010158
This is a calorie tracker
"""

import math
import os

def posInt(prompt):
    #Prompt the user until they enter a valid positive integer.
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Calories must be a positive number.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")


def meal(n):
    #Collect meal names and their calorie counts into separate lists.
    meals = []
    calories = []
    for _ in range(1, n + 1):
        meal_name = input(f"Enter the name of meal #{_}: ").strip().title()
        cal = posInt(f"Enter calories for {meal_name}: ")
        meals.append(meal_name)
        calories.append(cal)
    return meals, calories


def diff_calc(limit, consumed):
    #Calculate how much under/over the user is relative to the limit.
    return limit - consumed


def nxFile():
    #Find the next available log file name.
    count = 1
    while os.path.exists(f"log{count}.txt"):
        count += 1
    return f"log{count}.txt"


def save_log(filename, limit, meals, calories):
    #Save the calorie session details into a log file.
    total_calories = sum(calories)
    avg_calories = math.floor(total_calories / len(calories)) if calories else 0
    diff = diff_calc(limit, total_calories)

    with open(filename, "w") as file:
        file.write(f"{'Meal':<20}{'Calories':>10}\n")
        file.write("-" * 30 + "\n")

        for _ in range(len(meals)):
            file.write(f"{meals[_]:<20}{calories[_]:>10}\n")

        file.write("=" * 30 + "\n")
        file.write(f"{'Total':<20}{total_calories:>10}\n")
        file.write(f"{'Average':<20}{avg_calories:>10}\n\n")

        if diff < 0:
            file.write(f"WARNING: Limit exceeded by {abs(diff)} calorie(s)!\n")
        else:
            file.write(f"Within limit. Remaining: {diff} calorie(s).\n")

    print(f"Session saved successfully as {filename}")


def display_summary(limit, meals, calories):
    #Display the table of meals, totals, averages, and warnings... It's just same as what is getting saved in log file.
    total_calories = sum(calories)
    avg_calories = math.floor(total_calories / len(calories)) if calories else 0
    diff = diff_calc(limit, total_calories)

    # Table header
    print(f"\n{'Meal':<20}{'Calories':>10}")
    print("-" * 30)

    # Meal list
    for _ in range(len(meals)):
        print(f"{meals[_]:<20}{calories[_]:>10}")

    # Totals
    print("=" * 30)
    print(f"{'Total':<20}{total_calories:>10}")
    print(f"{'Average':<20}{avg_calories:>10}")

    # Limit status
    if diff < 0:
        print(f"\nWARNING: Calorie limit exceeded by {abs(diff)} calorie(s)!")
    else:
        print(f"\nYou are within the limit. You can still consume {diff} calorie(s).")

    # Ask about saving logs
    save_choice = input("\nDo you want to save this session? (yes/no): ").strip().lower()
    if save_choice in ["yes", "y"]:
        filename = nxFile()
        save_log(filename, limit, meals, calories)
    else:
        print("Session not saved.")


def main():
    print("This tool tracks your daily calories and warns you if you go over your limit. I added a additional feature to log it into a file")
    print("You can also save your session logs for future reference.\n")

    limit = posInt("Enter your daily calorie limit: ")
    n_meals = posInt("Enter the number of meals today: ")

    meals, calories = meal(n_meals)
    display_summary(limit, meals, calories)

main()
