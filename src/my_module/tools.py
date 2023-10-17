from tqdm import tqdm
from time import sleep

def really_important_function():
    for i in tqdm(range(100)):
        sleep(0.001)
    return True
