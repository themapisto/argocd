import os
import subprocess


res = subprocess.check_output('cat /home/ubuntu/argocd/argocd/canary/rollout.yaml | grep "particule/simplecolorapi:" ', shell=True)
result= res.decode('utf-8')
b=result[-4]
print(b)

if b=="1" :
    print ("1.0 to 2.0")
    os.system("sh /home/ubuntu/argocd/argocd/canary/2.0.sh")
else :
    print ("2.0 to 1.0")
    os.system("sh /home/ubuntu/argocd/argocd/canary/1.0.sh")
