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
          if aux.next:
            aux.next.previous = char
          char.previous = aux
        self.cursor = self.start
      else:
        while aux and aux != self.cursor:
          aux = aux.next
        if aux != None:
          char = CharacterNo(newCharacter)
          if beforeOrAfter == "before":
            char.previous = aux.previous
            char.next = aux
            if aux.previous:
              aux.previous.next = char
            else:
              self.start = char
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
    print(f"{newCharacter.value} added")

  def remove(self, beforeOrAfter):
    if self.start:
      aux = self.start
      while aux and aux != self.cursor:
        aux = aux.next
      if aux != None:
        if beforeOrAfter == "before":
          if aux.previous:
            removed = aux.previous
            if removed.previous:
              aux.previous = removed.previous
            removed.previous.next = aux
          else:
            print("Nothing to remove before cursor!")
        elif beforeOrAfter == "after":
          removed = aux.next
          removed.next = aux.next
          removed.previous = aux
        self.length -=1
    else:
      print('The list is empty')


