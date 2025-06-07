
def create_monster():
    name = input("What's the monster's name? ")
    hp = int(input("What's the monster's HP? "))
    attack = int(input("What's the monster's attack power? "))
    return {"name": name, "hp": hp, "attack": attack}

num_monsters = int(input("How many monsters do you want to create? "))

monster_list = []

for i in range(num_monsters):
    print(f"\nCreating monster {i + 1}:")
    monster = create_monster()
    monster_list.append(monster)

# Step 5: Print a summary of all monsters
print("\n--- Monster Summary ---")
for i in range(len(monster_list)):
    m = monster_list[i]
    print(f"Monster {i + 1}: Name = {m['name']}, HP = {m['hp']}, Attack = {m['attack']}")