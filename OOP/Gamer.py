class Gamer:
    active_gamers = 0

    @classmethod
    def get_active_gamers(cls):
        return Gamer.active_gamers

    @classmethod
    def gamer_from_string(cls, data_string):
        nickname, age, points = data_string.split(',')
        Gamer.active_gamers += 1
        return cls(nickname, age, points)

    def __init__(self, nickname, age, points):
        self.nickname = nickname
        self.age = age
        self.points = points
        Gamer.active_gamers += 1

    # methods of the class

    def get_nackname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18

    def get_adult_level_permisions(self):
        if self.is_adult():
            print('you are able to continue')
        else:
            print('you are too yang')

    def logout(self):
        Gamer.active_gamers -= 1


gamer_1 = Gamer('test1', 19, 21)
print(gamer_1.get_age())
gamer_1.get_adult_level_permisions()
gamer_2 = Gamer('test2', 12, 22)
print(gamer_2.get_age())
gamer_2.get_adult_level_permisions()
print(Gamer.active_gamers)
gamer_1.logout()
print(Gamer.active_gamers)

user_from_string = Gamer.gamer_from_string('nick,22,23')
print(user_from_string.points)
print(Gamer.active_gamers)

test=dict.fromkeys((1,2,3),('userKeys','13','43'))  # in this keys it will be a list first param keys will have all three items from keys
print(test)