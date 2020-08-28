available_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi", "dvd drive"]

valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
# print(valid_choices) #['1', '2', '3', '4', '5', '6', '7']

current_choice = "-"
computer_parts = [] #this is where we add customer's choices

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            #it's already in, so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the list below: ")
        for number, part in enumerate(available_parts):
            print("{0}: {1} ".format(number + 1, part))

    current_choice = input()

print(computer_parts)

# Please add options from the list below:
# 1: computer
# 2: monitor
# 3: keyboard
# 4: mouse
# 5: mouse mat
# 6: hdmi
# 7: dvd drive
# 1
# Adding 1
# Your list now contains: ['computer']
# 2
# Adding 2
# Your list now contains: ['computer', 'monitor']
# 3
# Adding 3
# Your list now contains: ['computer', 'monitor', 'keyboard']
# 2
# Removing 2
# Your list now contains: ['computer', 'keyboard']