class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


harbour = Room("Harbour", """
15.10.2059. Late autumn. Evening.
You survived after a ship crash, because zombies ate captain of the
ship. Now you stay at a big harbour. It's so cold outside and the wind
blowing really hard. The Sun come down very fsst and you noticed that
of zombies are coming to you and you desided to run. But where?
You can run to them or to a park or jump in the water and try to swim
away
Your actions:
- go to the park
- jump in the water
- run to somewhere
""")

park = Room("Park", """
You are in a park near the city center In the park so dark and you
can see not so far, also you have a flashlight. You know that train
station is on the other side of the park. You had to go...
Would you like to turn the flashlight?
- Yes
- No
""")

train_station = Room("Train Station", """
You are on a big train station in the city center. You see two trains
one of them is still work, in others hiding a lot of evil dog-zombies.
What a train do you prefer?
- 1
- 2
""")

train = Room("Train", """
You are in electrical train on the train station. And the train don't
work just two electrical wires look at you from dashboard. You try make
short circuit but it doesn't work. You decide use battery from you a
flaslight to make short circuit. You have red and black wires, how will
you connect them with battery? Black with plus red with minus or Red
with plus black with minus.
- Black with plus red with minus
- Red with plus black with minus
""")

the_end_winner = Room("The End", """
You look around and say 'I am alone and I am alive' You won!
""")

the_end_loser = Room("The End", """It was a real flop, man.""")

train.add_paths({
    'Black with plus red with minus': the_end_winner,
    'Red with plus black with minus': the_end_loser
})

generic_death = Room("death", "You died.")

train_station.add_paths({
    '1': generic_death,
    '2': train
})

park.add_paths({
    'no': train_station,
    'yes': generic_death
})

harbour.add_paths({
    '*': generic_death,
    'go to the park': park
})

START = harbour
