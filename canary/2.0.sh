#!/bin/sh
sudo cat rollout.yaml | grep "1.0" | xargs sed -i 's/1.0/2.0/g' rollout.yaml

