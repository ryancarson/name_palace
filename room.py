class Room():
  
  name = ''
  person_name = ''
  action = ''
  
  def __init__(self, **kwargs):
    for key, value in kwargs.items():
      setattr(self, key, value)
      
  def add_memory(self, person, action):
    self.person_name = person
    self.action = action