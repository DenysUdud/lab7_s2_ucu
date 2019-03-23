from bird import Bird, Penguin, MessengerBird
def getLocalMethods(clss):
    import types
    # This is a helper function for the test function below.
    # It returns a sorted list of the names of the methods
    # defined in a class. It's okay if you don't fully understand it!
    result = []
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if (isinstance(val, types.FunctionType)):
            result.append(var)
    return sorted(result)


def testBirdClasses():
    print("Testing Bird classes...", end="")
    # A basic Bird has a species name, can fly, and can lay eggs
    bird1 = Bird("Parrot")
    assert (type(bird1) == Bird)
    assert (isinstance(bird1, Bird))
    assert (bird1.fly() == "I can fly!")
    assert (bird1.countEggs() == 0)
    assert (str(bird1) == "Parrot has 0 eggs")
    bird1.layEgg()
    assert (bird1.countEggs() == 1)
    assert (str(bird1) == "Parrot has 1 egg")
    bird1.layEgg()
    assert (bird1.countEggs() == 2)
    assert (str(bird1) == "Parrot has 2 eggs")
    assert (getLocalMethods(Bird) == ['__init__', '__repr__', 'countEggs',
                                      'fly', 'layEgg'])

    # A Penguin is a Bird that cannot fly, but can swim
    bird2 = Penguin("Emperor Penguin")
    assert (type(bird2) == Penguin)
    assert (isinstance(bird2, Penguin))
    assert (isinstance(bird2, Bird))
    assert (bird2.fly() == "No flying for me.")
    assert (bird2.swim() == "I can swim!")
    bird2.layEgg()
    assert (bird2.countEggs() == 1)
    assert (str(bird2) == "Emperor Penguin has 1 egg")
    assert (getLocalMethods(Penguin) == ['fly', 'swim'])

    # A MessengerBird is a Bird that can optionally carry a message
    bird3 = MessengerBird("War Pigeon", message="Top-Secret Message!")
    assert (type(bird3) == MessengerBird)
    assert (isinstance(bird3, MessengerBird))
    assert (isinstance(bird3, Bird))
    assert (not isinstance(bird3, Penguin))
    assert (bird3.deliverMessage() == "Top-Secret Message!")
    assert (str(bird3) == "War Pigeon has 0 eggs")
    assert (bird3.fly() == "I can fly!")

    bird4 = MessengerBird("Homing Pigeon")
    assert (bird4.deliverMessage() == "")
    bird4.layEgg()
    assert (bird4.countEggs() == 1)
    assert (getLocalMethods(MessengerBird) == ['__init__', 'deliverMessage'])
    print("Done!")

if __name__ == "__main__":
    testBirdClasses()
