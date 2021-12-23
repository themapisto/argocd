import os
import subprocess

res = subprocess.check_output('cat rollout.yaml | grep "argoproj/rollouts-demo:" ', shell=True)
reslen= len(res)
if reslen==44 :
    print ("green to blue")
    os.system("sh blue.sh")
else :
    print ("blue to green")
    os.system("sh green.sh")

