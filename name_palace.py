from collections import namedtuple

palace = []

memory = namedtuple('memory', ['room', 'name'])

palace.append(memory(room='Kitchen', name='Ryan'))
palace.append(memory(room='Dining Room', name='Gill'))

for memory in palace:
  print("Room: " + memory.room + ", Name: " + memory.name)
