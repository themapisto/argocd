#!/bin/bash
sudo cat rollout.yaml | grep "demo:blue" | xargs sed -i 's/demo:blue/demo:green/g' rollout.yaml



