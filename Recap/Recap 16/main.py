import random
import string

class Music:
  def __init__(self, title:str = None, artist:str = None, duration:int = 0):
    self.title = title,
    self.artist = artist,
    self.duration = duration,
    self.code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

  