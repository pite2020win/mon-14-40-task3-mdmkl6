import statistics
import logging
import sys
import json
import os

def read(place):
  if os.path.exists(place):
    with open(place) as json_file:
      return json.load(json_file)
  else :
    data={}
    return data;

def save(data,place):
  with open(place, 'w') as outfile:
    json.dump(data, outfile)


def addone(data,name):
  data[name]={}

def choseone(data):
  while data!={}:
    list_to_chose=[]
    for element in data:
      list_to_chose.append(element)
    logging.info(list_to_chose)
    chose=input(':')
    if chose in data:
      return chose
    else:
      logging.info("This option does not exist.Chose again:")

def isfloat(x):
  try:
    x=float(x)
    return 1
  except:
    return 0

def isnote(x):
  if isfloat(x):
    x=float(x)
    if x>=2 and x<=5 and x%0.5==0:
      return 1
    else:
      return 0
  else:
    return 0

def average_of_all_from(data):
  if type(data) is dict:
    list_of_note=[]
    for element in data:
      note=average_of_all_from(data[element])
      if note!=-1 :
        list_of_note.append(note)
    if list_of_note!=[] :
      return statistics.fmean(list_of_note)
    else:
      return -1

  elif type(data) is list:
    list_of_note=list(filter(isnote,data))
    list_of_note=list(map(float,list_of_note))
    if list_of_note!=[] :
      return statistics.fmean(list_of_note)
    else:
      return -1
  else:
    return -1

def prin_all_by_tree(data,deep=0):
  if type(data) is dict:
    for element in data:
      logging.info("{}|__{}".format(deep*"   ",element))
      prin_all_by_tree(data[element],deep+1)
  elif type(data) is list:
    logging.info("{}|__{}".format(deep*"   ",data))
  else:
    logging.error("Błąd")

def get_average_by_class_and_name(data,clas,name):
  for school in  data:
    for _class in data[school]:
      if _class==clas:
        for student in data[school][_class]:
          if student==name:
            return average_of_all_from(data[school][_class][student])
  return -1

def get_school_and_class_of_student(data,name):
  for school in data:
    for _class in data[school]:
      for student in data[school][_class]:
        if student== name:
          return [school,_class]
  return []




def manage_note(subject,data):
  while True:
    logging.info("Notes:")
    logging.info(subject)
    logging.info("Chose:\n1.Add Note.\n2.Delete Note.\n3.Subject average.\n0.Back.")
    a=input()
    os.system('clear')

    if a=='1':
      subject.append(input("Enter note:")) 

    elif a=='2':
      x=''
      while x not in subject:
        x=input("Chose note:")
      subject.remove(x)

    elif a=='3':
      logging.info(average_of_all_from(subject))      

    elif a=='0':
      break
    
    save(data,'data.json')


def manage_subject(student,data):
  while True:
    logging.info("Chose:\n1.Chose subject.\n2.Add subject\n3.Delete subject\n4.Student average.\n5.Print all from student.\n0.Back.")
    a=input()
    os.system('clear')

    if a=='1':
      logging.info("Chose subject:")
      subject=choseone(student)
      manage_note(student[subject],data)         
    elif a=='2':
      student[input("Enter subject name:")]=[]

    elif a=='3':
      logging.info("Chose subject to delate:")
      del student[choseone(student)]

    elif a=='4':
      logging.info(average_of_all_from(student))

    elif a=='5':
      prin_all_by_tree(student)

    elif a=='0':
      break
    
    save(data,'data.json')


def manage_student(_class,data):
  while True:
    logging.info("Chose:\n1.Chose student.\n2.Add studnet.\n3.Delete student.\n4.Class average.\n5.Print all from class\n0.Back.")
    a=input()
    os.system('clear')


    if a=='1':
      logging.info("Chose Student:")
      student=choseone(_class)
      manage_subject(_class[student],data)         
    elif a=='2':
      addone(_class,input("Enter Student name:"))

    elif a=='3':
      logging.info("Chose Student to delate:")
      del _class[choseone(_class)]

    elif a=='4':
      logging.info(average_of_all_from(_class))

    elif a=='5':
      prin_all_by_tree(_class)

    elif a=='0':
      break
    
    save(data,'data.json')


def manage_class(school,data):
  while True:
    logging.info("Chose:\n1.Chose class.\n2.Add class\n3.Delete class\n4.Shool average.\n5.Print all from school..\n0.Back")
    a=input()
    os.system('clear')


    if a=='1':
      logging.info("Chose class:")
      _class=choseone(school)
      manage_student(school[_class],data)
      addone(school,input("Enter class name:"))

    elif a=='2':
      addone(school,input("Enter class name:"))

    elif a=='3':
      logging.info("Chose class to delate:")
      del school[choseone(school)]
    
    elif a=='4':
      logging.info(average_of_all_from(school))

    elif a=='5':
      prin_all_by_tree(school)

    elif a=='0':
      break
    
    save(data,'data.json')


def manage_school(data):
  while True:
    logging.info("Chose:\n1.Chose school\n2.Add School.\n3.Del school\n4.All School average.\n5.Print all.\n6.Student avarage by class and name.\n7.Student class,school by name.\n0.End.")
    a=input()
    os.system('clear')

    if a=='1':
      logging.info("Chose school:")
      school=choseone(data)
      manage_class(data[school],data) 
            
    elif a=='2':
      addone(data,input("Enter school name:"))

    elif a=='3':
      logging.info("Chose school to delate:")
      del data[choseone(data)]

    elif a=='4':
      logging.info(average_of_all_from(data))

    elif a=='5':
      prin_all_by_tree(data)

    elif a=='6':
      x=get_average_by_class_and_name(data,input("Enter class:"),input("Enter name:"))
      if x==-1:
        logging.info("Doesnt found.")
      else:
        logging.info(x)
    
    elif a=='7':
      x=get_school_and_class_of_student(data,input("Enter name: "))
      if x==[]:
        logging.info("Doesnt found.")
      else:
        logging.info("School:{}, Class:{}.".format(x[0],x[1]))


    elif a=='0':
      break
    
    save(data,'data.json')


  
if __name__ == "__main__":

  logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

  data=read('data.json')

  manage_school(data)