      # 40.1: Class - Example

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


            # Here we are creating a list and putting it through the Song class
            # and assigning it to a variable. Capitalization matters.
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

car_radio = Song(["I have these thoughts so often I ought",
                    "To replace that slot with what I once bought",
                    "Cause somebody stole my car radio",
                    "And now I just sit in silence"])
            # Here we are pulling up the variable that takes the class Song and the object List,
            # then we select which function inside of the class we want to run.
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
car_radio.sing_me_a_song()
            # Here we can do the same as above, but use the __init__ function instead which in this case,
            # just prints what the object is, which is a list for this example.

    # Testing this out...
class Recipe(object):

    def __init__(self, food):
        self.food = food

    def show_me_ingredients(self):
        for line in self.food:
            print('*', line)

pulled_pork = Recipe(["Pork",
                        "BBQ Sauce",
                        "Garlic",
                        "Apple Cider Vinegar",
                        "Ketchup",
                        "Water"])

pulled_pork.show_me_ingredients()
