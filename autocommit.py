import os
import time
while(True):
    if os.system('git diff --exit-code')==0:
        print("git diff is 0")
        f = open('dummy.txt','w')
        f.write(str(time.time()))
        f.close()
        continue
    os.system('git add-commit -m "Committed changes"')
    os.system('git push -u origin master')
    time.sleep(60)
