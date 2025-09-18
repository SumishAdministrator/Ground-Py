#This code helps in adding a progress bar

import time
from tqdm import tqdm
#from tqdm.notebook import tqdm <-- If Jupiter notebook is used

for ctr in tqdm(range(0,20)):
    time.sleep(0.1)


for ctr in tqdm(range(0,50), bar_format ="{desc}Processing|{bar}| {percentage:1f}% |" " Elapsed:{elapsed}, "):
    time.sleep(0.1)