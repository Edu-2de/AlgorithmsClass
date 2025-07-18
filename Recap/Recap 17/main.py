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
              aux.previous.next = aux
            else:
              self.start = aux
          else:
            print("Nothing to remove before cursor!")
        elif beforeOrAfter == "after":
          if aux.next:
            removed = aux.next
            if removed.next:
              aux.next = removed.next
              removed.next.previous = aux
            else:
              aux.next = None
          else:
            print("Nothing to remove after cursor!")
        self.length -=1
    else:
      print('The list is empty')

  def moveCursor(self, beforeOrAfter):
    if self.start:
      aux = self.start
      while aux and aux != self.cursor:
        aux = aux.next
      if aux != None:
        if beforeOrAfter == "before":
          if aux.previous:
            self.cursor = aux.previous
          else:
            print("Nothing before cursor!")
        elif beforeOrAfter == "after":
          if aux.next:
            self.cursor = aux.next
          else:
            print("Nothing after cursor!")
        print(f"Cursor now is: {self.cursor}")
    else:
      print('The list is empty')

  def listAllText(self):
    if self.start:
      aux = self.start
      list = []
      while (aux):
        list.append(aux.value)
        aux = aux.next
      print(" ".join(list))
    else:
      print('The list is empty')

  def showCursor(self):
    if self.start:
      aux = self.start
      list = []
      while (aux):
        if aux == self.cursor:
          aux.value = "|" + aux.value
        list.append(aux.value)
        aux = aux.next
      print(" ".join(list))
    else:
      print('The list is empty')

list = ListCharacter()
def menu():
  while True:
    print("\n============= MENU =============")
    print("1. Insert character")
    print("2. Remove character")
    print("3. Move cursor left")
    print("4. Move cursor right")
    print("5. Display text")
    print("6. Exit")
    print("================================")
    choice = input("Choice: ")
    if choice == "1":
      value = input("Type a character: ")
      char = Character(value)
      list.add(char)
    elif choice == "2":
      choice2 = input("Do you want remove before or after cursor? ")
      if choice2 == "before":
        list.remove("before")
      elif choice2 == "after":
        list.remove("after")
    elif choice == "3":
      list.moveCursor("before")
    elif choice == "4":
      list.moveCursor("after")
    elif choice == "5":
      list.listAllText()
    elif choice == "6":
      break

if __name__ == "__main__":
  menu()





