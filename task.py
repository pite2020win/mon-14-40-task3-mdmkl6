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
    l=[]
    for x in data:
      l.append(x)
    logging.info(l)
    a=input(':')
    if a in data:
      return a
    else:
      logging.info("This option does not exist.Chose again:")

def isnote(x):
  try:
    x=float(x)
    if x>=2 and x<=5 and x%0.5==0:
      return 1
    else:
      return 0
  except:
    return 0

def average(data):
  if type(data) is dict:
    a=[]
    for x in data:
      i=average(data[x])
      if i!=-1 :
        a.append(i)
    if a!=[] :
      return statistics.fmean(a)
    else:
      return -1

  elif type(data) is list:
    a=list(filter(isnote,data))
    a=list(map(float,a))
    if a!=[] :
      return statistics.fmean(a)
    else:
      return -1
  else:
    return -1

def printree(data,deep=0):
  if type(data) is dict:
    for x in data:
      logging.info("{}|__{}".format(deep*"   ",x))
      printree(data[x],deep+1)
  elif type(data) is list:
    logging.info("{}|__{}".format(deep*"   ",data))
  else:
    logging.error("Błąd")

def sabcan(data,clas,name):
  for x in  data:
    for y in data[x]:
      if y==clas:
        for z in data[x][y]:
          if z==name:
            return average(data[x][y][z])
  return -1

def scsbn(data,name):
  for x in data:
    for y in data[x]:
      for z in data[x][y]:
        if z== name:
          return [x,y]
  return -1




def mnote(data,data2):
  while True:
    logging.info("Notes:")
    logging.info(data)
    logging.info("Chose:\n1.Add Note.\n2.Delete Note.\n3.Subject average.\n0.Back.")
    a=input()
    os.system('clear')

    if a=='1':
      data.append(input("Enter note:")) 

    elif a=='2':
      x=''
      while x not in data:
        x=input("Chose note:")
      data.remove(x)

    elif a=='3':
      logging.info(average(data))      

    elif a=='0':
      break
    
    save(data2,'data.txt')


def msubject(data,data2):
  while True:
    logging.info("Chose:\n1.Chose subject.\n2.Add subject\n3.Delete subject\n4.Student average.\n5.Print all from student.\n0.Back.")
    a=input()
    os.system('clear')

    if a=='1':
      logging.info("Chose subject:")
      subject=choseone(data)
      mnote(data[subject],data2)         
    elif a=='2':
      data[input("Enter subject name:")]=[]

    elif a=='3':
      logging.info("Chose subject to delate:")
      del data[choseone(data)]

    elif a=='4':
      logging.info(average(data))

    elif a=='5':
      printree(data)

    elif a=='0':
      break
    
    save(data2,'data.txt')


def mstudent(data,data2):
  while True:
    logging.info("Chose:\n1.Chose student.\n2.Add studnet.\n3.Delete student.\n4.Class average.\n5.Print all from class\n0.Back.")
    a=input()
    os.system('clear')


    if a=='1':
      logging.info("Chose Student:")
      student=choseone(data)
      msubject(data[student],data2)         
    elif a=='2':
      addone(data,input("Enter Student name:"))

    elif a=='3':
      logging.info("Chose Student to delate:")
      del data[choseone(data)]

    elif a=='4':
      logging.info(average(data))

    elif a=='5':
      printree(data)

    elif a=='0':
      break
    
    save(data2,'data.txt')


def mclass(data,data2):
  while True:
    logging.info("Chose:\n1.Chose class.\n2.Add class\n3.Delete class\n4.Shool average.\n5.Print all from school..\n0.Back")
    a=input()
    os.system('clear')


    if a=='1':
      logging.info("Chose class:")
      clas=choseone(data)
      mstudent(data[clas],data2)
      addone(data,input("Enter class name:"))

    elif a=='2':
      addone(data,input("Enter class name:"))

    elif a=='3':
      logging.info("Chose class to delate:")
      del data[choseone(data)]
    
    elif a=='4':
      logging.info(average(data))

    elif a=='5':
      printree(data)

    elif a=='0':
      break
    
    save(data2,'data.txt')


def mschool(data,data2):
  while True:
    logging.info("Chose:\n1.Chose school\n2.Add School.\n3.Del school\n4.All School average.\n5.Print all.\n6.Student avarage by class and name.\n7.Student class,school by name.\n0.End.")
    a=input()
    os.system('clear')

    if a=='1':
      logging.info("Chose school:")
      school=choseone(data)
      mclass(data[school],data2) 
            
    elif a=='2':
      addone(data,input("Enter school name:"))

    elif a=='3':
      logging.info("Chose school to delate:")
      del data[choseone(data)]

    elif a=='4':
      logging.info(average(data))

    elif a=='5':
      printree(data)

    elif a=='6':
      x=sabcan(data,input("Enter class:"),input("Enter name:"))
      if x==-1:
        logging.info("Doesnt found.")
      else:
        logging.info(x)
    
    elif a=='7':
      x=scsbn(data,input("Enter name: "))
      if x==-1:
        logging.info("Doesnt found.")
      else:
        logging.info("School:{}, Class:{}.".format(x[0],x[1]))


    elif a=='0':
      break
    
    save(data2,'data.txt')




  

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

data=read('data.txt')

data2=data

mschool(data,data2)