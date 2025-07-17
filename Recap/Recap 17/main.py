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

class ListCharacter:
  def __init__(self):
    self.start = None
    self.length = 0
    self.cursor = None

  def add(self, newCharacter, beforeOrAfter):
    if self.start:
      aux = self.start
      if self.cursor == aux:
        char = CharacterNo(newCharacter)
        if beforeOrAfter == "before":
          self.start = char
          char.next = aux
          aux.previous = char
        elif beforeOrAfter == "after":
          aux.next = char
          char.previous = aux
      else:
        while aux and aux != self.cursor:
          aux = aux.next
        if aux != None:
          char = CharacterNo(newCharacter)
          if beforeOrAfter == "before":
            char.previous = aux.previous
            char.next = aux
            aux.previous.next = char
            aux.previous = char
          elif beforeOrAfter == "after":
            char.next = aux.next
            char.previous = aux
            if(aux.next):
              aux.next.previous = char
            aux.next = char
    else:
      char = CharacterNo(newCharacter)
      self.start = char
      self.cursor = char
    self.length += 1
    print(newCharacter.value)

