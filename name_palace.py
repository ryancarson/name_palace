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

memory = namedtuple('memory', ['room', 'name', 'action'])

print("Let's create your name palace first. Imagine yourself walking through your house, and enter the names of the rooms in that order. Please enter the room's name (for example Dining Room). Enter DONE when you're finished")

while True:
  room = input("> ")
  if room.lower() == "done":
    break
  rooms.append(room)

print("OK. Here are the rooms in your Memory Palace:")
for s in rooms:
  print(s)

print("Now you can start putting names and actions into those rooms. The more crazy and memorable the actions, the better!")

for s in rooms:
  name = input("\nRoom: "+s+"\nName: ")
  action = input("Action: ")
  palace.append(memory(room=s, name=name, action=action))

print("OK, great! Here is your completed Memory Palace:\n")

for memory in palace:
  print("Room: " + memory.room + ", Name: " + memory.name + ", Action: " + memory.action)
