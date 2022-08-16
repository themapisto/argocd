import os
import subprocess

res = subprocess.check_output('cat /home/ubuntu/argocd/argocd/bluegreen/rollout.yaml | grep "argoproj/rollouts-demo:" ', shell=True)
reslen= len(res)
if reslen==44 :
    print ("green to blue")
    os.system("sh /home/ubuntu/argocd/argocd/bluegreen/blue.sh")
else :
    print ("blue to green")
    os.system("sh /home/ubuntu/argocd/argocd/bluegreen/green.sh")


