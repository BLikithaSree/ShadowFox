"""Imagine you are doing a workout routine, and you have to complete 100
jumping jacks.
Write a program that:
Asks you to perform 10 jumping jacks at a time.
After each set, it asks, "Are you tired?"
If you reply "yes" or "y," it should ask if you want to skip the remaining sets.
If you reply "yes" or "y," it should break and print, "You completed a total of
jumping jacks."
For example, if you did only 30 jumping jacks and answered "yes," the program
will break and print, "You completed a total of 30 jumping jacks."
If you reply "no" or "n," it should continue and display how many jumping jacks
are remaining. After that, ask you again, "Are you tired?"
For example, if you answered "no," it should display that 70 jumping jacks are
remaining and ask you again, "Are you tired?"
If you reply "no" or "n," it should continue and display how many jumping jacks
are remaining. After that, ask you again, "Are you tired?"
For example, if you answered "no," it should display that 70 jumping jacks are
remaining and ask you again, "Are you tired?"
If you complete all 100 jumping jacks, it should print, "Congratulations! You
completed the workout," and stop the program
"""


total_jacks = 100
done_jacks = 0
set_size = 10

while done_jacks < total_jacks:
    done_jacks += set_size
    print(f"You have completed {done_jacks} jumping jacks.")
    if done_jacks >= total_jacks:
        print("Congratulations! You completed the workout.")
        break
    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()

    if tired in ['yes', 'y']:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        if skip in ['yes', 'y']:
            print(f"You completed a total of {done_jacks} jumping jacks.")
            break
        else:
            remaining = total_jacks - done_jacks
            print(f"Okay! {remaining} jumping jacks remaining. Keep going!\n")
    else:
        remaining = total_jacks - done_jacks
        print(f"Great! {remaining} jumping jacks remaining. Let's keep moving!\n")
