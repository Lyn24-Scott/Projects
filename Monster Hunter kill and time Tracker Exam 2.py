#Exam 2 Monster hunter kill and time tracker
#Tech requirements
#User input
#File handling (CSV), File must have mutilple coloumns.
#Arrays
#Parse string data into an array (or list)
#Basic Operations, Max, Min, and Total Value, and sort array
#Dictionary Usage keys and values to dynamically create a menu
#Create a menu Based on dictionary content
#Error handling
#GUI Interface to display a popup message showing the User's selected option from the menu

#Monster Hunter kill Tracker, Takes monster kill and adds to a counter

#Create Dictionary of set monster names and have the monsters as Keys and Kill Time as values
#Ask user to write New Monster and Time into Dictionary
#Add amount of kills to array

#Save the monster kills and time kills to a file named Monster_Hunter.txt
#Ask the user for the amount of times they killed a certain monster, followed by the time it took

def monster_and_weapon_types():
    
    weapon_types = ['Great Sword', 'Long Sword', 'Sword and Shield', 'Dual Blades', 'Hammer', 'Hunting Horn', 'Lance', 'Gunlance', 'Switch Axe', 'Charge Blade', 'Insect Glaive', 'Light Bowgun,' 'Heavy Bowgun','Hunting Horn','Swtich Axe']
    monsters = ['Anjanath','Barrorh','Odagaron','Ratholos','Rathian','Diablos','Palomu','Belezguese','Kula-la-ku','Nergigante','Teostra','Kushladora','Kirin']

    return weapon_types,monsters

def monster_time():

    while True:
        try:
            time = int(input('Enter kill time (in mintues):'))
            return time
        except ValueError:
            print('Enter a Valid Number')

def monster_kill_and_time(monster_dict):

    weapon_types,monsters = monster_and_weapon_types()
    
    monster_kill = input('Enter Monster name:')
    weapon_kill = input('Enter weapon used:')
    
    if monster_kill not in monsters:
        print('Invalid Monster selection')
        return None
    
    elif weapon_kill  not in  weapon_types:
        print('Not a weapon Type')
        return None

    time = monster_time()

    if monster_kill not in monster_dict:
        monster_dict[monster_kill] = []
    monster_dict[monster_kill].append((time, weapon_kill))

    with open('Monster_Hunter.txt','w') as file:
        file.write(f'Monster:{monster_kill},time:{time},weapon used:{weapon_kill}')
    print('Monster kills and time confirmed!')


    return monster_kill,time,weapon_kill

#Keep track of the monsters killed, weapons used, and amount of time it tookm to kill monster

def add_record(monster_dict):

    try:
        
        monster_kill,time,weapon_kill = monster_kill_and_time(monster_dict)

        if monster_kill not in monster_dict:
            monster_dict[monster_kill] = []
        monster_dict[monster_kill].append((time, weapon_kill))
        
        with open('Monster_Hunter.txt','a') as file:
            file.write(f'Monster:{monster_kill},time:{time},weapon used:{weapon_kill}')
        print('New Monster kills and time added!')
        
    except IOError:
     
     print('Tracker Not loaded')
    
def show_tracker_data (monster_dict):

    try:
        if not monster_dict:
            print('No availalbe data')
            return

         
        with open('Monster_Hunter.txt','r') as file:
            tracker = file.read()
            print(tracker)
            
    except IOError:
     
         print('Tracker Not loaded')


def higest_time_highest_kills(monster_dict):

    times = [time for records in monster_dict.values() for time, _ in records]
        
    try:
        
        with open('Monster_Hunter.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                part = line.split(',')
                time_part = part[1].split(':')[1].strip()
                times.append(int(time_part))

        if not times:
            print('Time data not found')
            return
        
        max_time = max(times)  # Find the highest time
        min_time = min(times)  # Find the lowest time

        print(f'Highest kill time: {max_time} minutes')
        print(f'Lowest kill time: {min_time} minutes')
         

    except IOError:
        print('file not found')

def total_mintues(monster_dict):

    times = [time for records in monster_dict.values() for time, _ in records]
        
    try:
        
        with open('Monster_Hunter.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                part = line.split(',')
                time_part = part[1].split(':')[1].strip()
                times.append(int(time_part))

        if not times:
            print('Time data not found')
            return
        
        total_time = sum(time for records in monster_dict.values() for time, _ in records)
        print(f'Total Monster Time: {total_time}')
    
    except IOError:
        print('file not found')

def display_tracker(monster_dict):

    print('Welcome to the Monster Hunter Kill Tracker!')
    print('-------------------------------------------')
    monsters,weapon_types = monster_and_weapon_types()
    separted_monster_string = ','.join(monsters)
    separted_weapon_string = ','.join(weapon_types)
    print(f'Weapon Types: {separted_monster_string}')
    print('-------------------------------------------')
    print(f'Monsters: {separted_weapon_string}')

    return monsters, weapon_types



def display_menu():

       monster_dict = {}
       while True:
           
        print("\nMenu:")
        print("1.show monster types and weapons")
        print("2.Enter Type of Monster killed and your Time")
        print("3.Add Another Record")
        print("4.Display Tracker data")
        print("5.Lowest and Highest Time for Monster")
        print("6.Show Total Monster Time")
        print("99.Exit")
        
       
        choice = input("Choose an option (1-18 or 99 to exit): ")
        if choice == "1":
           display_tracker(monster_dict)
        elif choice == "2":
           monster_kill_and_time(monster_dict)
        elif choice == "3":
            add_record(monster_dict)
        elif choice == "4":
           show_tracker_data (monster_dict)
        elif choice == "5":
           higest_time_highest_kills(monster_dict)
        elif choice == "6":
           total_mintues(monster_dict)
        elif choice == "99":
            print("Exiting..")
            break

        else:
            print('Enter proper selection')
             
def main():

    display_menu()

    
if __name__ == '__main__':

    main()



