#!/usr/bin/env python

#PBS -l nodes=1:ppn=1,vmem=1GB
#PBS -l walltime=00:00:10

import os

#import dipy.tracking as dipytracking
#dipytracking.bench()

try:
    os.stat("output")
except:
    os.mkdir("output")

f = open("output/test.txt", "w")
f.write("yo")
f.close()

#f = open("product.json", "w")
#f.write("{\"tags\": [\"from_app\"], \"brainlife\": [{\"type\": \"success\", \"msg\": \"here is message\"}]}")
#f.close()