import os
import subprocess

curr_dir = 'C:/Users/csehg/Documents'

p = subprocess.Popen(os.path.join(curr_dir, 'VSCodeUserSetup-x64-1.74.2.exe'))
return_code = p.wait()
print(return_code)