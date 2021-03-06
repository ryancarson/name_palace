from room import Room

class Name_Palace:
  
  rooms = []
  
  def add_memories(self):
    print("\nNow you can start putting names and actions into those rooms.\n"
          "The more crazy and memorable the actions, the better!!\n")
    
    for room in self.rooms:
      print("Room: {}".format(room.name))
      person = input('Person: ')
      action = input('Action: ')
      print('\n')
      room.add_memory(person, action)
  
  def __init__(self):
    while True:
      choice = input("Type your room name or 'DONE' to finish: ")
      if choice.lower() == 'done':
        break
      
      self.rooms.append(Room(name = choice))
    
    self.add_memories()
    
    print("\nOK, great! Here is your completed Memory Palace ...\n")
    for room in self.rooms:
      print("Room: {name}, Person's Name: {person_name}, Action: {action}".format(**room.__dict__))
    
Name_Palace()
