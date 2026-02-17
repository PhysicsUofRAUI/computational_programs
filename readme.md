# Purpose
This little repo is meant to hold all the small scripts that I plan on writing to run on my k3s cluster. It is largley inspired by the tutorial on NYUs website here, https://k8s-docs.hsrn.nyu.edu/batch/, and in fact that is why I have an 'nyu_tutorial/' line in my gitignore (I didn't want to include their code with mine). 

The rest of this document is to show how to run these scripts on a k3s cluster (at least how I have made it). It is mostly for me to remember and probably is not the best way, but hey I am just messing around here. Later I will be needing to do some docker stuff just for more complex.

# Steps
1. Create folder to contain python file and YAML.
2. Push it to the remote.
3. Pull from the remote while in the repo on the control plane node. 
4. Navigate to the new folder
5. Create a configmap by running
```kubectl create configmap YOUR_CONFIGMAP --from-file="PROBABLY_PYTHON_FILE.py"```
6. Run
```kubectl apply -f job.yml```
7. To see the results (print them)
```kubectl logs -f job/solver```
8. Run these to clean it up
```
kubectl delete job -l source=YOUR_LABEL
kubectl delete configmap YOUR_CONFIGMAP
```