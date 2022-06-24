from pprint import pprint
  
def main():

    all_data = []
    with open('todos.csv','r') as f:
        lines = [line.strip() for line in f.readlines()]
        header = lines[0]
        values = lines[1:]
        list_header = header.split(";")

        for value in values:
            list_value =  value.split(";")
            data_line = dict(zip(list_header,list_value))
            all_data.append(data_line)
            

    pprint(all_data)






def main_write_csv():
    data = [
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": False
  },
  {
    "userId": 1,
    "id": 3,
    "title": "fugiat veniam minus",
    "completed": False
  },
  {
    "userId": 1,
    "id": 4,
    "title": "et porro tempora",
    "completed": True
  }
]


    # thedict = {"name":"Robert"}
    # print(thedict["name"])

    with open('todos.csv','w') as f:
        header = data[0].keys()
        print(*header,sep=";",file=f)
        for d in data:
            print(*d.values(),sep=";",file=f)



if __name__ == "__main__":
    main()