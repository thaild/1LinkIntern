class Human:
        gender
        nationality
        favourite_drink
        core_characteristic
        favourite_beverage
        name
        age

        def love
        def drink
        def laugh
        def do_your_special_thing

    class Americans(Humans)
        def drink(beverage):
            if beverage != favourite_drink: print "You call that a drink?"
            else: print "Great!"

    class French(Humans)
        def drink(beverage, cheese):
            if beverage == favourite_drink and cheese == None: print "No cheese?"
            elif beverage != favourite_drink and cheese == None: print "Révolution!"

    class Brazilian(Humans)
        def do_your_special_thing
            win_every_soccer_world_cup()

    class Germans(Humans)
        def drink(beverage):
            if favourite_drink != beverage: print "I need more beer"
            else: print "Lecker!"

    class HighSchoolStudent(Americans):
        def __init__(self, name, age):
             self.name = name
             self.age = age

jeff = HighSchoolStudent(name, age):
hans = Germans()
ronaldo = Brazilian()
amelie = French()

for friends in [jeff, hans, ronaldo]:
    friends.laugh()
    friends.drink("cola")
    friends.do_your_special_thing()

print amelie.love(jeff)
>>> True
print ronaldo.love(hans)
>>> False