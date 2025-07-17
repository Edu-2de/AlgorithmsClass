import random
import string

class Music:
  def __init__(self, title:str = None, artist:str = None, duration:int = 0):
    self.title = title
    self.artist = artist
    self.duration = duration
    self.code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

  def __str__(self):
    return f'Music{self.title}, from artist: {self.artist}, duration: {self.duration}'
  
class MusicNo:
    def __init__(self, music):
      self.music = music
      self.next = None
      self.previous = None

class MusicList:
  def __init__(self):
    self.start = None
    self.length = 0

  def add(self, newMusic):
    if self.start:
      aux = self.start
      while aux.next:
        aux = aux.next
      x = MusicNo(newMusic)
      aux.next = x
    else:
      x = MusicNo(newMusic)
      self.start = x
    self.length += 1

  def removeByCode(self, code):
    if self.start:
      aux = self.start
      codeFound = False
      while aux.next and aux.next.music.code != code:
        aux = aux.next
        codeFound = True
      if codeFound == True:
        print(f'{aux.music} removed')
        self.length -= 1
      else:
        print('This code not exist')
    else:
      print('The list is empty')

  def searchByTitle(self, title):
    if self.start:
      aux = self.start
      while aux.next and aux.next.music.title != title:
        aux = aux.next
      if aux != None:
        print(aux.music)
      else:
        print('This music not exist')
    else:
      print('The list is empty')

  def listByStart(self):
    if self.start:
      aux = self.start
      count = 0
      while (aux):
        count += 1
        print(  f"{count}. {aux.music.title} {aux.music.artist} {aux.music.duration}" )
        aux = aux.next
    else:
      print('The list is empty')

  def listByEnd(self):
    if self.start:
      aux = self.start
      while aux.next:
        aux = aux.next
      while aux:
        print(aux.music)
        aux = aux.previous

    else:
      print('The list is empty')