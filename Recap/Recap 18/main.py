from datetime import datetime

class Page():
  def __init__(self, url:str = None, title:str = None):
    self.url = url
    self.title = title
    self.timestamp = None