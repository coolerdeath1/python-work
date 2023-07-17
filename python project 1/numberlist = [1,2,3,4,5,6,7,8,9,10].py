#Write a Python program that removes and prints every third number from a list of numbers until the list is empty.
numberlist = [1,2,3,4,5,6,7,8,9,10]
i = 2
while i < len(numberlist):
  print(numberlist[i])
  numberlist.remove(numberlist[i])
  
  i += 2  
  if i >= len(numberlist):
    i = 2
  


    
