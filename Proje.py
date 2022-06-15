#Soru 1
orneklist=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
fl=[]
def flatten(l):
  for e in l:
      if isinstance(e, list):
         flatten(e)  
      else:
        fl.append(e)
flatten(orneklist)
print(fl) 


#Soru 2
l=[[1, 2], [3, 4], [5, 6, 7]]
def reversed_list(l):
  l.reverse()
  for i in range(len(l)):
    (l[i])=(l[i])[::-1]
reversed_list(l)
print(l)
