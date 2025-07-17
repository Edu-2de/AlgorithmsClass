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
  
class NoMusic:
    def __init__(self, music):
      self.music = music
      self.proximo = None
      self.anterior = None

class MusicList:
  def __init__(self):
    self.start = None
    self.length = 0
  