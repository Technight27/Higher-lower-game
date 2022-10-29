import random
from game_data import data 
def check(A,B):
  if A==B:
     A=random.choice(data)
     B=random.choice(data)
     if A!=B:
       return A,B
     else:
       check(A,B)
  else:
    return A,B

def inputs():
  A=random.choice(data)
  B=random.choice(data)
  A,B=check(A,B)
  z=info(A,B)
  return z
  
  
def info(A,B):
  n1=A["name"]
  d1=A["description"]
  c1=A["country"]
  from art import logo
  from art import vs
  from replit import clear
  clear()
  print(logo)
  print(f"Compare A: {n1}, {d1}, from {c1}")
  n2=B["name"]
  d2=B["description"]
  c2=B["country"]
  print(vs)
  print(f"Compare B: {n2}, {d2}, from {c2}")
  i=input("Who has more followers?")
  r=compare(A,B,i)
  return r
  
def compare(A,B,i):
  co1=int(A["follower_count"])
  co2=int(B["follower_count"])
  print(co1)
  print(co2)
  if co1>co2:
    
    return  i=="A" 
  elif co1<co2:
    
    return i=="B"
  
    
def mains():
  c=0
  result=inputs()
  
  while result==True:
    c=c+1
    result=inputs()
  print(f"Score is {c}")  
mains()  
    
