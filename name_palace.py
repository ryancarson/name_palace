from collections import namedtuple

# A palace is a way to remember things. You create 'rooms' and then place things you want to remember in each room. Then when you need to recall, you imagine yourself walking through the rooms in your 'palace'
# To read more about this method, head to http://en.wikipedia.org/wiki/Method_of_loci
palace = []

memory = namedtuple('memory', ['room', 'name'])

# Insert some hard-coded data to make sure it works
palace.append(memory(room='Kitchen', name='Ryan'))
palace.append(memory(room='Dining Room', name='Gill'))

for memory in palace:
  print("Room: " + memory.room + ", Name: " + memory.name)
