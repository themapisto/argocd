#!/bin/sh
sudo cat rollout.yaml | grep "2.0" | xargs sed -i 's/2.0/1.0/g' rollout.yaml

