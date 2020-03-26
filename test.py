#!/usr/bin/env python

#PBS -l nodes=1:ppn=1,vmem=1GB
#PBS -l walltime=00:00:10

import os
import json
import shutil

#import dipy.tracking as dipytracking
#dipytracking.bench()

with open('config.json') as f:
  config = json.load(f)

try:
    os.stat("output_1")
except:
    os.mkdir("output_1")
shutil.copyfile(config['t1'], "output_1/t1.nii.gz")

try:
    os.stat("output_2")
except:
    os.mkdir("output_2")
shutil.copyfile(config['t1'], "output_2/bad.nii.gz")

#for deprecated output
shutil.copyfile(config['t1'], "out.nii.gz")

#f = open("product.json", "w")
#f.write("{\"tags\": [\"from_app\"], \"brainlife\": [{\"type\": \"success\", \"msg\": \"here is message\"}]}")
#f.close()
