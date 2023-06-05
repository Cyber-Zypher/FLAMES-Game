import time
print('''
       _______________                        |*\_/*|________
      |  ___________  |     .-.     .-.      ||_/-\_|______  |
      | |           | |    .****. .****.     | |           | |
      | |   0   0   | |    .*****.*****.     | |   0   0   | |
      | |     -     | |     .*********.      | |     -     | |
      | |   \___/   | |      .*******.       | |   \___/   | |
      | |___     ___| |       .*****.        | |___________| |
      |_____|\_/|_____|        .***.         |_______________|
        _|__|/ \|_|_.............*.............._|________|_
       / ********** \                          / ********** \ 
                            F.L.A.M.E.S                       
                     --Developed by Sidharth--                  ''')

def remove_common_letters(name1, name2):
    # Convert names to lowercase and remove spaces
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    # Convert names to lists of characters
    name1_list = list(name1)
    name2_list = list(name2)
    
    # Remove common letters between the names
    for letter in name1:
        if letter in name2_list:
            name1_list.remove(letter)
            name2_list.remove(letter)
    
    return name1_list, name2_list

def count_remaining_letters(name_list):
    return len(name_list)

def get_relationship_category(count):
    categories = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings or Soulmates"]
    return categories[count % len(categories)]

def play_flames_game():
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")
    
    name1_list, name2_list = remove_common_letters(name1, name2)
    
    count = count_remaining_letters(name1_list + name2_list)
    
    category = get_relationship_category(count)
    print("Please wait..")
    time.sleep(2)
    print("Relationship category: " + category)
    #print("Please not that, a Relationship is not based on a program or a game. So Just take this as a fun.. Have a nice day..")

while True:
    play_flames_game()