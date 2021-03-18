from tkinter import *
import random

print("Enter number of points (>3) and x and y coordidnates")
n=int(input())
x=[0]*n
y=[0]*n
for i in range(n):
   a,b= map(int, input().split())
   x[i]=a
   y[i]=b
print("Enter number of Iterations(keep it less than 10e6)")
op=int(input())
master=Tk()
can=Canvas(master,width=800,height=800,bg='#000000')
can.pack()

def make_point(x,y,r,place):
   return place.create_oval(x-r,y-r,x+r,y+r,fill='#FF6347')

for i in range(n):
   make_point(x[i],y[i],5,can)

a=random.randint(0,n-1)
curr_x=x[a]
curr_y=y[a]
for i in range(op):
   a=random.randint(0,n-1)
   new_x=(curr_x + x[a])/2
   new_y=(curr_y + y[a])/2
   curr_x,curr_y=new_x,new_y
   make_point(new_x,new_y,0,can)


master.mainloop()
