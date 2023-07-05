import pandas as pd
from datetime import datetime

class Client_program:

    def __init__(self, df):
        self.df = pd.read_csv(df).set_index('id')

    
    def get_main_menu_choice(self):
        print('MAIN MENU')
        print('=' * 20)
        print('1. Print client')
        print('2. Add client')
        print('3. Update client')
        print('4. Delete client')
        print('5. Save to file and Exit')
        print()
        choice_menu = input('Select action: ')
        if choice_menu.isdigit():
            return int(choice_menu)

    
    def choice1_print_client(self):
        print()
        print("PRINTING client info")
        print('-' * 15)
        print('1. Search client by surname?')
        print('2. Search client by id?')
        print('3. Return to main menu')
        print()
        choice1 = input("Select by: ")
        check_1 = True
        while check_1 and choice1.isdigit():
            if int(choice1) == 1:
                choice_surname = input("Give client's surname: ").strip().title()
                if choice_surname in self.df['surname'].values:
                    print(self.df.loc[self.df['surname'] == choice_surname])
                    check_1 = False
                else:
                    print('Sorry, no client with this surname in file!')
                    print()
                    check_1 = False
            elif int(choice1) == 2:
                choice_id = input("Give client's id: ")
                if choice_id.isdigit():
                    if int(choice_id) in self.df.index:
                        print(self.df.loc[self.df.index == int(choice_id)])
                        check_1 = False
                    else:
                        print('Sorry, no client with this id in file!')
                        print()
                        check_1 = False
                else:
                    print('You have to give a number!')
                    check_1 = False
            elif int(choice1) == 3:
                check_1 = False
            else:
                print("You have to choose between 1 - 3!")
                check_1 = False

    
    def choice2_add_client(self):
        print()
        print('ADDING client')
        print('-' * 15)
        ids_list = self.df.index
        new_client = {'name': input("Give client's name: ").strip().title(),
                      'surname': input("Give client's surname: ").strip().title(),
                      'father_name': input("Give client's father_name: ").strip().title(),
                      'age': datetime.now().year -
                                   datetime.strptime(input("Give client's birthday(dd/mm/yy): ").strip(),
                                                     '%m/%d/%Y').year,
                      'pr_total': int(input("Give client's PR total: "))}
        if len(ids_list) != 0:
            new_client['id'] = max(ids_list) + 1
        else:
            new_client['id'] = 1
        return new_client

    
    def choice2_add_client_check_duplicate(self, new_client):
        clients_identifier_list = []
        new_client_tuple = (new_client['name'], new_client['surname'],
                            new_client['father_name'], new_client['age'])
        for x in range(len(self.df)):
            clients_identifier_list.append((self.df.iloc[x, 0], self.df.iloc[x, 1],
                                            self.df.iloc[x, 2], self.df.iloc[x, 3]))
        if new_client_tuple in clients_identifier_list:
            return False
        else:
            return True

    
    def choice3_update_client(self):
        print()
        print('UPDATING client')
        print('-' * 15)
        choice3_id = int(input("Give client's id: "))
        check_3 = True
        while check_3:
            if choice3_id not in self.df.index:
                print('Wrong id!')
                check_3 = False
            else:
                print('You are about to update the following client:')
                print(self.df.loc[self.df.index == choice3_id])
                print()
                print('UPDATE submenu - Available info for update:')
                print('1. Name')
                print('2. Surname')
                print('3. Father_name')
                print('4. Birthday')
                print('5. PR total')
                print()
                choice3 = int(input('Select info to update: '))
                print()
                if choice3 not in range(1, 6):
                    print('You have to choose from 1-5!')
                else:
                    if choice3 == 1:
                        self.df.loc[self.df.index == choice3_id, 'name'] = input("Give client's NEW name: ").strip().title()
                    elif choice3 == 2:
                        self.df.loc[self.df.index == choice3_id, 'surname'] = input("Give client's NEW surname: ").strip().title()
                    elif choice3 == 3:
                        self.df.loc[self.df.index == choice3_id, 'father_name'] = input(
                            "Give client's NEW Father_name: ").strip().title()
                    elif choice3 == 4:
                        self.df.loc[self.df.index == choice3_id, 'birthday'] = input(
                            "Give client's NEW birthday (dd/mm/yy): ").strip().title()
                    elif choice3 == 5:
                        self.df.loc[self.df.index == choice3_id, 'pr_totale'] = int(input(
                            "Give client's NEW PR total: ").strip())
                    check_3 = False
                    print(self.df.loc[self.df.index == choice3_id])

    
    def choice4_delete_client(self):
        print()
        print('DELETING client')
        print('-' * 15)
        choice4_id = int(input("Give client's id: "))
        check_4 = True
        while check_4:
            if choice4_id in self.df.index:
                print('Trying to delete the following client:')
                print(self.df[self.df.index == choice4_id])
                print()
                choice4 = input('Are you sure you want to delete this client? - Type "y" for yes or "n" for no: ')
                if choice4 == 'y':
                    # df = df.loc[df.index != choice4_id]
                    self.df = self.df.drop(choice4_id)
                check_4 = False
            else:
                print('No client has this id!')
                check_4 = False

    
    def save_to_csv(self):
        self.df.to_csv('client_program.csv')
        print(self.df)
