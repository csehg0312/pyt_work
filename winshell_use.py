import os, sys
import winshell

os.chdir("E:\\")
filepath = os.path.abspath("test.txt")

#
# You create a file and delete it
#
with open(filepath, "w") as f:
  f.write("test1")
winshell.delete_file(filepath)

#
# Then you create a newer version and delete that
#
with open(filepath, "w") as f:
  f.write("test2")
winshell.delete_file(filepath)

#
# Finally you create the newest version
#
with open(filepath, "w") as f:
  f.write("test3")

recycle_bin = winshell.recycle_bin()
print(recycle_bin.versions(filepath))

#
# Now you undelete the previous versions which
# will be renamed as "Copy of..." or something similar.
#
print(winshell.undelete(filepath))
winshell.delete_file(filepath)
print(winshell.undelete(filepath))