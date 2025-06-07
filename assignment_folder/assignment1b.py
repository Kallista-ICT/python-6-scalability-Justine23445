def monster_character(answer1, answer2, answer3):
    print(f"Monster created : {answer1}, hp : {answer2}, attack power :{answer3}")

def main():
    name = input("What's the monster's name ? ")
    hp = input("What's the monster's hp ? ")
    attackpower = input("What's the monster attack power ? ")
    monster_character(name, hp, attackpower)

def number(turns):
    print(f"Lets create the {turns} monster's")

number("first")
main()
number("second")     
main()
    
