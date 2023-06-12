from datetime import datetime

class Client:
    cnt = 1
    list_of_clients = []

    def __init__(self, name, birthday=None):
        self.cnt = Client.cnt
        Client.cnt += 1
        Client.list_of_clients.append(name)
        self.name = name
        self.birthday = birthday
        self.PRs_list = []
        self.BW_history = {'BW': []}

    def PRs(self, Squat, BP, DL):
        self.Squat = Squat
        self.BP = BP
        self.DL = DL
        self.PRs_list.append(self.Squat)
        self.PRs_list.append(self.BP)
        self.PRs_list.append(self.DL)
        return f"{self.name}'s lifts: Squat: {self.Squat}kg, BP: {self.BP}kg, DL: {self.DL}kg"

    def Age_BW(self, BW, date):
        self.BW = BW
        self.BW_history['BW'].append(f"{BW}kg, {date}")
        age = datetime.strptime(self.birthday, '%d-%m-%Y')
        return f"{self.name}'s age is: {datetime.now().year - age.year} and his bodyweight is {self.BW}kg"

    def __str__(self):
        return f"Client name: {self.name}, client number: {self.cnt}"


Grafakos = Client('Grafakos', '1-12-1982')
Yacoub = Client('Yacoub', '1-12-1982')
Panagiotis = Client('Panagiotis', '1-12-1982')
Dobro = Client('Dobro', '1-12-1982')
Despoina = Client('Despoina', '1-12-1982')
Raia = Client('Raia', '1-12-1982')
Rania = Client('Rania', '1-12-1982')
Mixalis = Client('Mixalis', '1-12-1982')

# print(f"Gym members: {list(enumerate(Client.list_of_clients, 1))}")
# print(Client.list_of_clients)
# print(Dobro)
Dobro.Age_BW(103, '5/5/2023')
Dobro.Age_BW(90, '2/6/2023')
# print(Dobro.BW_history)

Dobro.PRs(90, 70, 90)
# print(Dobro.PRs_list)


while True:
    print('1. Add Client')
    print("2. Client's info")
    print('3. Update Client')
    print('4. Delete Client')
    print('5. List of Clients (names)')
    print('6. Exit')
    choice = int(input('Select action: '))
    if choice == 1:
        new_client_name = input("Give client's name: ")
        new_client_age = input("Give client's birthday: ")
        new_client = Client(new_client_name, new_client_age)
    elif choice == 2:
        client_name = input("Give client's name to get his info: ")
        while client_name not in Client.list_of_clients:
            print('There is no client with this name! Try again please')
            client_name = input("Give client's name to get his info: ")
        else:
            print(Client.client_name.)
    elif choice == 5:
        print(Client.list_of_clients)

    else:
        break
