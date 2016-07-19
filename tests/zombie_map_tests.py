from nose.tools import *
from zombie.zombie_map import *


def test_zombie_game_map():
    # harbour
    assert_equal(START.go('*'), generic_death)

    room = START.go('go to the park')
    assert_equal(room, park)

    # park
    the_park = Room("Park", "Park")
    the_park.add_paths({
        'no': train_station,
        'yes': generic_death
    })

    assert_equal(the_park.go('no'), train_station)
    assert_equal(the_park.go('yes'), generic_death)

    # train station
    the_train_station = Room("Train Station", "Train Station")
    the_train_station.add_paths({
        '1': generic_death,
        '2': train
    })

    assert_equal(the_train_station.go('1'), generic_death)
    assert_equal(the_train_station.go('2'), train)

    # train
    the_train = Room("Train", "Train")
    the_train.add_paths({
        'Black with plus red with minus': the_end_winner,
        'Red with plus black with minus': the_end_loser
    })

    assert_equal(the_train.go('Black with plus red with minus'),
                 the_end_winner)
    assert_equal(the_train.go('Red with plus black with minus'),
                 the_end_loser)
