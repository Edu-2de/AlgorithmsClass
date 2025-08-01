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
    return super().show()

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
      while aux.next:
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
  
  def listAllTasks(self):
    if self.start:
      aux = self.start
      while(aux):
        print(aux.task.show())
        aux = aux.next
    else:
      print("The list is empty")

  def searchTask(self, searchTitle):
    if self.start:
      aux = self.start
      while aux and aux.task.title != searchTitle:
        aux = aux.next
      if aux != None:
        print(aux.task.show())
      else:
        print("This task not exist")
    else:
      print("The list is empty")


  def tasksByPriority(self):
    if self.start:
      aux = self.start
      auxList = []
      while(aux):
        auxList.append(aux)
        aux = aux.next
      auxList.sort(key=lambda t: t.task.priority, reverse=True)
      for i in auxList:
        print(i.task.show())
    else:
      print("The list is empty")

list = ListTask()

def menu():
  while True:
    print("\n============= MENU =============")
    print("1. Add a simple task")
    print("2. Add a task with a deadline")
    print("3. Remove a task")
    print("4. List tasks")
    print("5. Search for tasks")
    print("6. List by priority")
    print("7. Exit")
    print("================================")
    choice = input("Choice: ")
    if choice == '1':
      title = input("Task title: ")
      description = input("Description: ")
      priority = input("Priority (0 - 10): ")
      task = SimpleTask(title, description, priority)
      list.add(task)
    elif choice == '2':
      title = input("Task title: ")
      description = input("Description: ")
      priority = input("Priority (0 - 10): ")
      deadline = input("Deadline: ")
      task = DeadlineTask(title, description, priority, deadline)
      list.add(task)
    elif choice == '3':
      titleProved = input("Task title:")
      list.removeByTitle(titleProved)
    elif choice == '4':
      list.listAllTasks()
    elif choice == '5':
      title = input('Type the title of task: ')
      list.searchTask(title)
    elif choice == '6':
      list.tasksByPriority()
    elif choice == '7':
      break
 
if __name__ == "__main__":
  menu()