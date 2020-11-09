# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

def addclas(data,clasname):
  data[clasname]={}

def addstudent(data,clasname,studentnumber,studentname,studentsurname):
  data[clasname][studentnumber]={}
  data[clasname][studentnumber]["studentname"]=studentname
  data[clasname][studentnumber]["studentsurname"]=studentsurname

def addsubject(data,clasname,studentnumber,subjectname):
  data[clasname][studentnumber][subjectname]={}
  data[clasname][studentnumber][subjectname]["notes"]=[]

def setnote(data,clasname,studentnumber,subjectname,note,noteindex):
  data[clasname][studentnumber][subjectname]["notes"].insert(noteindex,note)

def getendnote(data,clasname,studentnumber,subjectname):
  s=0
  il=0
  for x in data[clasname][studentnumber][subjectname]['notes']:
    s=s+x
    il=il+1
  data[clasname][studentnumber][subjectname]["lastnote"]=int(s/il)
  return int(s/il)

def getavarge(data,clasname,studentnumber):
  s=0
  il=0
  for x in data[clasname][studentnumber]:
    s=s+data[clasname][studentnumber][x]
    il=il+1
  data[clasname][studentnumber]["avarge"]=int(s/il)
  return (s/il)


data={}

addclas(data,"clas1")
addstudent(data,'clas1','student1','name','surname')