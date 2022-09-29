from datetime import datetime as dt
  
# Getting current date and time
now = dt.now()
print("Without formatting", now)
  
# Example 1
s = now.strftime("%a %m %y")
print('\nExample 1:', s)
  
# Example 2
si = now.strftime("%A %m %Y")
print('\nExample 2:', si)
  
# Example 3
se = now.strftime("%I:%M:%S")
print('\nExample 3:', se)
  
# Example 4
so = now.strftime("%j")
print('\nExample 4:', so)