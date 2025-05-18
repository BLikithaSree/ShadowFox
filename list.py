"""You have a list of superheroes representing the Justice
League. justice\_league = \["Superman","Batman","WonderWoman","Flash","Aquaman", "Green Lantern"]

Perform the following tasks:

1. Calculate the number of members in the Justice League.
2. Batman recruited Batgirl and Nightwing as new members.
   Add them to your list.
3. Wonder Woman is now the leader of the Justice League.
   Move her to the beginning of the list.
4. Aquaman and Flash are having conflicts, and you need to
   separate them. Choose either "Green Lantern" or "Superman"
   and move them in between Aquaman and Flash.
5. The Justice League faced a crisis, and Superman decided to
   assemble a new team. Replace the existing list with the following
   new members: "Cyborg","Shazam" ,"Hawkgirl","MartianManhunter","Green Arrow".

6. Sort the Justice League alphabetically. The hero at the 0th
   index will become the new leader.

(BONUS: Can you predict who the new leader will be?)

Your task is to write Python code to perform these operations on
the "justice\_league" list. Display the list at each step to observe
the changes.
"""


justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Step 0 - Initial list:", justice_league)

# 1: Count members
print("Step 1 - Number of members:", len(justice_league))

# 2: Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("Step 2 - After adding Batgirl and Nightwing:", justice_league)

# 3: Make Wonder Woman the leader (move to index 0)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Step 3 - Wonder Woman as leader:", justice_league)

# 4: Move Superman between Aquaman and Flash
justice_league.remove("Superman")  # Remove Superman from current position

# Find indexes
aquaman_index = justice_league.index("Aquaman")
flash_index = justice_league.index("Flash")

# Ensure Aquaman comes before Flash
if aquaman_index > flash_index:
    aquaman_index, flash_index = flash_index, aquaman_index

# Insert Superman between Aquaman and Flash
justice_league.insert(flash_index, "Superman")
print("Step 4 - Superman moved between Aquaman and Flash:", justice_league)

# 5: Replace the list with a new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("Step 5 - New team:", justice_league)

# BONUS: Sort the list alphabetically and get the new leader
justice_league.sort()
print("Step 6 - Sorted team:", justice_league)
print("New leader:", justice_league[0])




