# argocd

1. canary 배포 : 서비스를 전환할때 deployment안의 pod의 최소 개수를 보장하면서 최소 개수의 pod가 전환이 완료되면 나머지 pod를 순차적으로 변경함 
2. bluegreen 배포 : 서비스를 전환할때 변경전과 변경후의 서비스를 생성하고 변경이 완료되면 변경전의 pod를 제거함
