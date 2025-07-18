from datetime import datetime

class Page():
  def __init__(self, url:str = None, title:str = None):
    self.url = url
    self.title = title
    self.timestamp = None

class PageNo():
  def __init__(self, page):
    self.page = page
    self.next = None
    self.previous = None

class ListPage():
  def __init__(self)