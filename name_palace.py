def memory_palace():

    from collections import namedtuple

    '''
    A palace is a way to remember things. You create 'rooms' and then place things
    you want to remember in each room. Then when you need to recall, you imagine
    yourself walking through the rooms in your 'palace'
    To read more about this method, head to
    http://en.wikipedia.org/wiki/Method_of_loci
    '''
    palace = []
    rooms = []

    '''
    The idea is to place a person in a room, doing a memorable action.
    The weirder and more memorable the action, the better. For instance
    Ryan in the kitchen, roasting a basketball on the stove - "Ryan" and
    "roasting" being memorable
    '''

    # TODO Catch errors
    # TODO Test on name memory at certain intervals (review)
    # TODO Add tags to people like school, work, etc
    # TODO Add database to store values
    # TODO Convert to OOP

    Memory = namedtuple('Memory', ['room', 'name', 'action'])

    print("Let's create your name palace first.\n"
          "Imagine yourself walking through your house, and enter the names \n"
          "of the rooms in that order. Enter DONE when you're finished")

    while True:
        room = input("> ")
        if room.lower() == "done":
          break
        rooms.append(room)

    print("\nNow you can start putting names and actions into those rooms.\n"
          "The more crazy and memorable the actions, the better!")

    for room in rooms:
        print("\nRoom: "+room)
        name = input("Name: ")
        action = input("Action: ")
        palace.append(Memory(room=room, name=name, action=action))

    print("\nOK, great! Here is your completed Memory Palace ...\n")

    for Memory in palace:
        print("Room: " + Memory.room + ", Name: " + Memory.name + ", Action: " + Memory.action)

if __name__ == '__main__':
    memory_palace()
