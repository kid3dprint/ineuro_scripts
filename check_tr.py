# pip install thedicomsort
from pydicom import dcmread
import os
import random

directory="./FunRaw"
for sub_dir in os.listdir(directory):
  file_list = os.listdir(os.path.join(directory, sub_dir))
  random_file = random.choice(file_list)
  #print(random_file)
  dcm=dcmread(os.path.join(directory, sub_dir)+os.sep+random_file)
  print(dcm.RepetitionTime)
