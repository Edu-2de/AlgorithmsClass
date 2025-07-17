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
      self.current = None

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
      x.previous = aux
      aux.next = x
    else:
      x = MusicNo(newMusic)
      self.start = x
      self.current = x
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

  def nextSong(self):
    if self.start:
      if self.current and self.current.next:
        self.current = self.current.next
        print(self.current.music)
      else:
        print('There are no more songs to advance')
    else:
      print('The list is empty')

  def previousSong(self):
    if self.start:
      if self.current and self.current.previous:
        self.current = self.current.previous
        print(self.current.music)
      else:
        print('There are no more songs to come back to')
    else:
      print('The list is empty')

musics = MusicList()

def menu():
  while True:
    print("\n============= MENU =============")
    print("1. Add a music to the end of the playlist.")
    print("2. Remove a music by code.")
    print("3. Search for a song by title.")
    print("4. List all songs in the playlist")
    print("5. Skip to the next song and skip to the previous one ")
    print("6. exit")
    print("================================")
    choice = input("Choice: ")
    if choice == '1':
      title = input("Title: ")
      artist = input("Artist: ")
      duration = input("Duration(in seconds): ")
      newMusic = Music(title, artist, duration)
      musics.add(newMusic)
      break
    elif choice == '2':
      code = input("Code: ")
      musics.removeByCode(code)
      break
    elif choice


      
