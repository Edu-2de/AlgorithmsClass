class Character:
  def __init__(self, value:str = None):
    self.value = value

  def __str__(self):
    return f"Character: {self.value}"
  
class CharacterNo:
  def __init__(self, character):
    self.character = character
    self.next = None
    self.previous = None
    self.cursor = None
