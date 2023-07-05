from datetime import datetime

class Person:
    def __init__(self, name, birthday, weight, height):
        self.name = name
        self.age = datetime.now().year - datetime.strptime(birthday, '%m/%d/%Y').year
        self.weight = weight
        self. height = height

    def BMI(self):
        return self.weight / self.height ** 2

    def __str__(self):
        return f"{self.name} is {self.age} years old and has {self.BMI():.2f} BMI"

    def __add__(self, other):
        return self.weight + other.weight


class Athlete(Person):
    def __init__(self, name, birthday, weight, height, fat_perc, sport, oly_medals=0):
        super().__init__(name, birthday, weight, height)
        self.fat_perc = fat_perc
        self.sport = sport
        self.oly_medals = oly_medals

    def check_elite(self):
        return True if self.oly_medals > 0 else False

    def __str__(self):
        if self.check_elite():
            return super().__str__() + f". He is an elite {self.sport} athlete with a {self.fat_perc} body fat"
        else:
            return super().__str__() + f". He is a {self.sport} athlete with a {self.fat_perc} body fat"


class Boxer(Athlete):
    def __init__(self, name, birthday, weight, height, fat_perc, sport, oly_medals, KOs):
        super().__init__(name, birthday, weight, height, fat_perc, sport, oly_medals)
        self.KOs = KOs

    def __str__(self):
        return super().__str__() + f" and a total of {self.KOs} Knock Outs achieved."

    def add_KOs(self, KOs):
        return self.KOs + KOs


class Sprinter(Athlete):
    def __init__(self, name, birthday, weight, height, fat_perc, sport, oly_medals, under_10sec_races):
        super().__init__(name, birthday, weight, height, fat_perc, sport, oly_medals)
        self.under_10sec_races = under_10sec_races

    def __str__(self):
        return super().__str__() + f" and a total of {self.under_10sec_races} times run 100m under 10 seconds."


class Fan(Person):
    def __init__(self, name, birthday, weight, height, team, fav_players):
        super().__init__(name, birthday, weight, height)
        self.team = team
        self.fav_players = fav_players

    def __len__(self):
        return len(self.fav_players)

    def __getitem__(self, key):
        return self.fav_players[key]

    def __setitem__(self, key, value):
        self.fav_players[key] = value

    def __str__(self):
        return f"{self.name} is {self.age} years old and supports {self.team}."


ath1 = Athlete('Lepri', '19/9/1985', 74, 1.75, '9%', 'BJJ', oly_medals=0)
pers = Person('Liolios', '1/12/1982', 66.5, 1.70)
box1 = Boxer('Loma', '17/2/1988', 86, 1.92, '6%', 'Boxing', oly_medals=2, KOs=11)
box2 = Boxer('Mayweather', '24/2/1977', 86, 1.72, '20%', 'Boxing', oly_medals=1, KOs=27)
spr1 = Sprinter('Bolt', '21/8/1986', 72, 1.80, '5%', '100m', oly_medals=8, under_10sec_races=3)
fan1 = Fan('Tsoukalas', '22/3/1958', 80, 1.77, 'Olympiacos', ['Giovanni', 'Rivaldo', 'Djole'])


# requesting value from fan1 list of favorite players:
print(fan1[0])
# setting new value in position 0:
fan1[0] = box1.name
print(fan1[0])

# adding boxers' KOs:
print(box1.add_KOs(box2.KOs))

# adding 2 persons' weight:
print(ath1 + pers)
