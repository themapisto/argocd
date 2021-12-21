#!/bin/bash
sudo cat rollout.yaml | grep "demo:green" | xargs sed -i 's/demo:green/demo:blue/g' rollout.yaml



