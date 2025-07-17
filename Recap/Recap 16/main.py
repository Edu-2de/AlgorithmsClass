import random
import string

class Music:
  def __init__(self, title:str = None, artist:str = None, duration:int = 0):
    self.title = title
    self.artist = artist
    self.duration = duration
    self.code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

  def __str__(self):
    return f'Music {self.title}, from artist: {self.artist}, duration: {self.duration}, code: {self.code}'
  
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
    return newMusic

  def removeByCode(self, code):
    if self.start:
      aux = self.start
      codeFound = False
      while aux.next and aux.next.music.code != code:
        aux = aux.next
        codeFound = True
      if codeFound == True:
        self.length -= 1
        return f'{aux.music} removed'
      else:
        return 'This code not exist'
    else:
      return 'The list is empty'

  def searchByTitle(self, title):
    if self.start:
      aux = self.start
      while aux.next and aux.next.music.title != title:
        aux = aux.next
      if aux != None:
        return aux.music
      else:
        return 'This music not exist'
    else:
      return 'The list is empty'

  def listByStart(self):
    if self.start:
      aux = self.start
      count = 0
      while (aux):
        count += 1
        print(f"{count}. {aux.music}")
        aux = aux.next
    else:
      print('The list is empty')

  def listByEnd(self):
    if self.start:
      aux = self.start
      count = 0
      while aux.next:
        aux = aux.next
      while aux:
        count += 1
        print(f"{count}. {aux.music}")
        aux = aux.previous
    else:
      print('The list is empty')

  def nextSong(self):
    if self.start:
      if self.current and self.current.next:
        self.current = self.current.next
        print(f'{self.current.music.title} is playing now')
      else:
        print('There are no more songs to advance')
    else:
      print('The list is empty')

  def previousSong(self):
    if self.start:
      if self.current and self.current.previous:
        self.current = self.current.previous
        print(f'{self.current.music.title} is playing now')
      else:
        print('There are no more songs to come back to')
    else:
      print('The list is empty')

  def printCurrent(self):
    if self.current:
      print(f'{self.current.music.title} is playing')
    else:
      print("Nothing is playing")

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
      print(musics.add(newMusic))
    elif choice == '2':
      code = input("Code: ")
      musics.removeByCode(code)
    elif choice == '3':
      title = input("Title: ")
      print(musics.searchByTitle(title))
    elif choice == '4':
      print('Do you want to list the songs from beginning to end or from end to beginning?')
      print('Type beginning or end')
      beginningOrEnd = input("Choice: ")
      if beginningOrEnd == "beginning":
        print(musics.listByStart())
      elif beginningOrEnd == "end":
        print(musics.listByEnd())
      else:
        print("error, (you need type beginning or end)")
    elif choice == '5':
      musics.printCurrent()
      while True:
        try:
          choice = input("Do you want go to previous song or next song (p, n or exit)? ")
          if(choice == 'p'):
            musics.previousSong()
          elif(choice == 'n'):
            musics.nextSong()
          elif(choice == 'exit'):
            break
        except:
          print('error')
    elif choice == '6':
      break

if __name__ == "__main__":
  menu()


      
