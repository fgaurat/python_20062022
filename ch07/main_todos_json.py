import json
from pprint import pprint

def main():
  nb = 0
  with open("todos.json") as f:
    todos = json.load(f)
    
    for todo in todos:
      # if todo['completed']:
      #   nb+=1
      nb +=  1 if todo['completed'] else 0
      
  print(nb)
  with open("todos.json") as f:
    todos = [todo for todo in json.load(f) if todo['completed']]
    print(len(todos))    


if __name__ == "__main__":
  main()