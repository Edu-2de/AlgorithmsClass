class Task():
  def __init__(self, title:str = None, description:str = None, priority:int = 0):
    self.title = title
    self.description = description
    self.priority = priority
  
  def show(self):
    return f"{self.title} - {self.description} - {self.priority}"

class SimpleTask(Task):
  def __init__(self, title:str = None, description:str = None, priority:int = 0):
    super().__init__(title, description, priority),

  def show(self):
    super().show()

class DeadlineTask(Task):
  def __init__(self, title:str = None, description:str = None, priority:int = 0, deadline:str = None):
    super().__init__(title, description, priority)
    self.deadline = deadline
  
  def show(self):
    return f"{self.title} - {self.description} - {self.priority} - {self.deadline}"
  
class NoTask():
  def __init__(self, task):
    self.task = task
    self.next = None
    self.previous = None

  

