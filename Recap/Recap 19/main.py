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

class ListTask():
  def __init__(self):
    self.start = None
    self.length = 0

  def add(self, newTask):
    noNewTask = NoTask(newTask)
    if self.start:
      aux = self.start
      while aux:
        aux = aux.next
      aux.next = noNewTask
    else:
      self.start = noNewTask
      print(f"{noNewTask.task.show()} added")
    self.length += 1
      
  def removeByTitle(self, titleProved):
    if self.start:
      aux = self.start
      while aux and aux.task.title != titleProved:
        aux = aux.next
      if aux != None:
        print(f"{aux.task} removed")
        self.length -= 1
        if aux == self.start:
          if self.length == 1:
            self.start = None
          else:
            self.start = aux.next
        else:
          if aux.next:
            aux.next.previous = aux.previous
          else:
            aux.previous.next = aux.next
    else:
      print("The list is empty")

