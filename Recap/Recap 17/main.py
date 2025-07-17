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

class ListCharacter:
  def __init__(self):
    self.start = None
    self.length = 0

  def add(self, newCharacter):
    if self.start:
      aux = self.start
      if self.cursor == aux:
        char = CharacterNo(newCharacter)
        aux = aux.next
        self.start = char
        char.next = aux

    else:
      char = CharacterNo(newCharacter)
      self.start = char
      self.cursor = self.start
    self.length += 1
    print(newCharacter.value)

