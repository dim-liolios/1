clients = [{'name': 'Dimitris', 'surname': 'Liolios', 'father_name': 'Theodosis', 'age': 41, 'PR_total': 410, 'id': 1000}]

def menu():
    print()
    print('MENU')
    print('='*20)
    print('1. Print client')
    print('2. Add client')
    print('3. Update client')
    print('4. Delete client')
    print('5. Exit')
    choice = int(input('Select action: '))
    return choice

# def search_by_surname():
# .isdigit
#  raise exception
# def search_by_id():

while True:
    choice = menu()
    
    # CHOICE 1 - PRINT
    if choice == 1:
        print("Select client's info to choose from. Select between 1 - 3 or 4 to return to previous menu: ")
        print('1. Search by surname?')
        print('2. Search by id?')
        print('3. Search by surname AND id?')
        print('4. Go to previous menu')
        choice1 = int(input("Select by: "))
        while True:
            if choice1 == 1:
                choice_surname = input("Give client's surname: ")
                for x in clients:
                    if x['surname'] == choice_surname:
                            print(x)
                break
            elif choice1 == 2:
                choice_id = int(input("Give client's id: "))
                for x in clients:
                    if x['id'] == choice_id:
                        print(x)
                break
            elif choice1 == 3:
                choice_both_surname = input("Give client's surname: ")
                choice_both_id = int(input("Give client's id: "))
                for x in clients:
                    if x['surname'] == choice_both_surname and x['id'] == choice_both_id:
                        print(x)
                break
            elif choice1 == 4: break
            else: choice1 = int(input("You have to choose between 1 - 4. Select by: "))
                
    # CHOICE 2 - ADD
    elif choice == 2:
        ids_list = []
        for x in clients:
            if x['id'] not in ids_list:
                ids_list.append(x['id'])
        print('Adding new client...')
        new_client = {'name': input("Give client's name: "), 'surname': input("Give client's surname: "),
                      'father_name': input("Give client's father_name: "), 'age': int(input("Give client's age: ")),
                      'PR_total': int(input("Give client's PR_total: ")), 'id': max(ids_list) + 1}
        for x in clients:
            if new_client['name'] == x['name'] and new_client['surname'] == x['surname'] and new_client['father_name'] == x['father_name']:
                print('There is already a client with the same name')
                break
        clients.append(new_client)
        ids_list.append(new_client['id'])
        print('You just added the following client:')
        print(new_client)
        
    # CHOICE 3 - UPDATE
    elif choice == 3:
        print('Updating client...')
        print('Select client to update: ')
        choice3_surname = input("Give client's surname: ")
        choice3_id = int(input("Give client's id: "))
        for x in clients:
            while True:
                if x['surname'] == choice3_surname and x['id'] == choice3_id:
                    print("UPDATE submenu - Available info for update:")
                    print('1. Name')
                    print('2. Surname')
                    print('3. Father_name')
                    print('4. Age')
                    print('5. PR_Total')
                    print('6. Go to previous menu')
                    choice3 = int(input('Select info to update, choose between 1-6: '))
                    if choice3 == 1:
                        x['name'] = input("Give NEW client's name: ")
                        break
                    elif choice3 == 2:
                        x['surname'] = input("Give NEW client's surname: ")
                        break
                    elif choice3 == 3:
                        x['father_name'] = input("Give NEW client's father_name: ")
                        break
                    elif choice3 == 4:
                        x['age'] = int(input("Give NEW client's age: "))
                        break
                    elif choice3 == 5:
                        x['PR_total'] = int(input("Give NEW client's PR_total: "))
                        break
                    elif choice3 ==6:
                        break
                    else:
                        print('You have to choose from 1-6!')
                        continue
                print('Wrong surname and/or id!')
                break
                
    # CHOICE 4 - DELETE
    elif choice == 4:
        print('Deleting client...')
        print('Select client to delete: ')
        choice4_surname = input("Give client's surname: ")
        choice4_id = int(input("Give client's id: "))
        for x in clients:
            if x['surname'] == choice4_surname and x['id'] == choice4_id:
                clients.remove(x)
    elif choice == 5:
        break


print(clients)
# print(ids_list)
