"""Using a for loop, simulate rolling a sixsided die multiple times (at least 20
times).
Count and print the following statistics:
How many times you rolled a 6
How many times you rolled a 1
How many times you rolled two 6s in a row"""

import random
num_rolls = input("Enter number of times:")
num_rolls=int(num_rolls)
count_6 = 0
count_1 = 0
two_6s_in_a_row = 0
previous_roll = 0
for _ in range(num_rolls):
    roll = random.randint(1, 6)
    print("Rolled:", roll)

    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            two_6s_in_a_row += 1
    if roll == 1:
        count_1 += 1

    previous_roll = roll
print("\n--- Statistics ---")
print("Number of times 6 was rolled:", count_6)
print("Number of times 1 was rolled:", count_1)
print("Number of times two 6s were rolled in a row:", two_6s_in_a_row)
