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
  