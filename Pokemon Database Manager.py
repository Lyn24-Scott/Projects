#Pokemon Card manager
#Consists of pokemons Name,Type,HP,Stage,Attacks,Retreat Cost,Abilites
#Certain Rarity Symbols
#Promo Cards,Speical Cards etc.
#This manager consists of the user putting in thier pokemon card then the data will be entered into a database that shows
#The pokemon cards the user has entered

import sqlite3

def create_pokemon_database():
        
        
    conn = sqlite3.connect('pokemon_card_manager.db')
    cursor = conn.cursor()

            
    cursor.execute('''CREATE TABLE IF NOT EXISTS pokemon_cards (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                pokemon_name TEXT NOT NULL,
                                element_type TEXT NOT NULL,
                                hp INTEGER NOT NULL,
                                stage TEXT NOT NULL,
                                attacks TEXT NOT NULL,
                                retreat_cost TEXT NOT NULL,
                                rarity TEXT NOT NULL
                    )''')
    
    conn.commit()
    conn.close()
    print('pokedex created!')


def view_pokemon_database():

    conn = sqlite3.connect('pokemon_card_manager.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pokemon_cards")
    rows = cursor.fetchall()
    for row in rows:
            print(row)

    conn.commit()
    conn.close()

            
#Superclass
class Pokemon:
    
    #initialize Pokenmon card
    def __init__(self,pokemon_name,element_type,hp,stage,attacks,retreat_cost,rarity):
        self.pokemon_name = pokemon_name
        self.element_type = element_type
        self.hp = hp
        self.stage = stage
        self.attacks = attacks
        self.retreat_cost = retreat_cost
        self.rarity = rarity
        
    #Mutator Methods 

    def set_pokemon_name(self,pokemon_name):
        self.pokemon_name = pokemon_name 

    def set_element_type(self,element_type):
        self.element_type = element_type

    def set_hp(self,hp):
        self.hp = hp

    def set_stage(self,stage):
        self.stage = stage

    def set_attacks(self,attacks):
        self.attacks = attacks

    def set_retreat_cost(self,retreat_cost):
        self.retreat_cost = retreat_cost

    def set_rarity(self,rarity):
        self.rarity = rarity


    #Accessors Methods
        
    def get_hp(self):
        return self.hp

    def get_stage(self):
        return self.stage
    
    def get_attacks(self):
        return self.attacks


    def save_to_mon_db(self):
        conn = sqlite3.connect('pokemon_card_manager.db')
        cursor = conn.cursor()
        cursor.execute("""
                        INSERT INTO pokemon_cards (pokemon_name,element_type,hp,stage,attacks,retreat_cost,rarity)
                        VALUES (?,?,?,?,?,?,?)
                        """,
                       (self.pokemon_name,self.element_type,int(self.hp),self.stage,self.attacks,self.retreat_cost,self.rarity))
                       
        conn.commit()
        conn.close()
        print(f'pokemon {self.pokemon_name} added to database.')




class Holo(Pokemon):

    def __init__(self,pokemon_name,element_type,hp,stage,attacks,retreat_cost,rarity,holo):
        super().__init__(pokemon_name,element_type,hp,stage,attacks,retreat_cost,rarity)
        self.holo = holo
        
        
    def get_holo(self):
        return self.holo


class Full_art(Pokemon):

    def __init__(self,pokemon_name,element_type,hp,stage,attacks,retreat_cost,rarity,full_art):
        super().__init__(pokemon_name,element_type,hp,stage,attacks,retreat_cost,rarity,)
        self.full_art = full_art
      
        
    def get_full_art(self):
        return self.full_art

class Promo(Pokemon):

    def __init__(self,pokemon_name,element_type,hp,stage,attacks,retreat_cost,rarity,promo):
        super().__init__(pokemon_name,element_type,hp,stage,attacks,retreat_cost,rarity)
        self.promo = promo
        
   
    def get_promo(self):
        return self.promo

  
class Price():
    

    def __init__(self):
        self.pokemons = []


    def add_pokemon(self,pokemon):
        self.pokemons.append(pokemon)

def calculate_total_price():
    conn = sqlite3.connect('pokemon_card_manager.db')
    cursor = conn.cursor()

                
    cursor.execute('SELECT rarity FROM pokemon_cards')
    p_rows = cursor.fetchall()
    total_price = 0 
    for row in p_rows:
        rarity = row[0]
        if rarity == 'holo':
            total_price += 50
        if rarity =='promo':
            total_price += 30
        if rarity == 'full art':
            total_price += 45

    conn.close()
    return total_price

       

#Have user enter in thier pokemon and put thier info in the database
def enter_pokemon():
    print('Enter Pokemon Card Details')
    name = input('Pokemon Name:')
    element = input('Element:')

    while True:
      
        try:
            hp = int(input('HP: '))
            break

        except ValueError:
                print('HP must be an integer.')
                
    stage = input('Stage:')
    attacks = input('Attacks:')
    retreat_cost = input('Retreat Cost:')
    rarity = input('Rarity (holo,Full Art, Promo, Common, Rare):').lower()

    if rarity.lower() == 'holo':
        return Holo(name,element,hp,stage,attacks,retreat_cost,rarity,holo = True)
    elif rarity.lower() == 'full_art':
        return Full_art(name,element,hp,stage,attacks,retreat_cost,rarity,full_art = True)
    elif rarity.lower() == 'promo':
        return Promo(name,element,hp,stage,attacks,retreat_cost,rarity,promo = True)

    else:
        return Pokemon(name,element,hp,stage,attacks,retreat_cost,rarity)


def delete_pokemon():

    conn = sqlite3.connect('pokemon_card_manager.db')
    cursor = conn.cursor()

    pokemon_delete = input('Enter name of pokemon to delete:')
    cursor.execute("SELECT * FROM pokemon_cards WHERE pokemon_name = ?",(pokemon_delete,))
    if cursor.fetchone():
        cursor.execute("DELETE FROM pokemon_cards WHERE pokemon_name = ?",(pokemon_delete,))
        conn.commit()
        print(f'pokemon {pokemon_delete} has been deleted from database.')

    else:
        print(f'Pokemon {pokemon_delete} not found in the database.')

    conn.close()



def main():

    #Pokemon Database Creation
    create_pokemon_database()
    price = Price()
    while True:
        print("\nMenu:")
        print("1.View Pokemon Manger Database")
        print("2.Add new pokemon to Database")
        print("3.Delete pokemon from Database")
        print("4.Total price for pokemon cards")
        print("99.Exit")
        choice = input("Choose an option (1-4 or 99 to exit): ")
        if choice == "1":
          view_pokemon_database()
        elif choice == "2":
          pokemon = enter_pokemon()
          pokemon.save_to_mon_db()
          price.add_pokemon(pokemon)
          again = input('Enter another mon? (yes/no): ').lower()
          if again != 'yes':
            break
        elif choice == "3":
          delete_pokemon()
        elif choice == "4":
           total_price = calculate_total_price()
           print('Total price of all pokemon cards: $125')
        elif choice == "99":
            print('bye!')
            break


if __name__ == '__main__':
    main()


    
