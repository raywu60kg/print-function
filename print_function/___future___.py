import pprint
import random
import sys
random_candidate = ["!", "@", "#", "$", "%", "^", "&", "*", "<", ">", "?"]
def print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    if flush == True:
        pprint.pprint("=======")
        pprint.pprint(*objects)
        pprint.pprint("=======")
    else:
        pprint.pprint("".join(random.sample(random_candidate,5)))   
