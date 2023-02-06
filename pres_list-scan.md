---
marp: true
theme: uncover
---

# Os.scandir() vs Os.listdir()

By: Gabriel Cseh

---

We will discuss the os module in Python and inside that we qualify the:
* os.listdir()
* os.scandir()
and which one to choose for a file manager written in Python

---
### Os.listdir()
* #### Pros:
- the diretcory data is generated into a list
- data can be stored
- no need to generate it all the time
* #### Cons:
- it can be sometimes overuse the memory 
- always have to generate when new file or directory created

---
### Os.scandir()
* #### Pros:
- this is a iterable
- data can be accessed by an iterator for/map
- when called much time better - no need to store in list
- easy to access name/path/is_dir/is_file
* #### Cons:
- can increase cpu usage

---

