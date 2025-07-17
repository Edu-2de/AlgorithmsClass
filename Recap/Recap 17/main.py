class Character:
  def __init__(self, value:str = None):
    self.value = value

  def __str__(self):
    return f"Character: {self.value}"