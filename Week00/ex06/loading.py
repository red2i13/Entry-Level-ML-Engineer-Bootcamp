import time
from time import sleep
# from tqdm import tqdm
import sys

def ft_progress(lst):
	
	#print the first iteration
	start_time = time.perf_counter()
	bar =  0 * '=' + '>' + ' ' * int(100 / 2)
	cur_time = time.perf_counter() - start_time
	print(f"ETA:  99s [ 0%] [{bar}] 0/{len(lst)}| elapsed time {cur_time:.2f}s", end='\r', file=sys.stdout, flush=True)
	#the rest of range
	for i in lst:
		remain = 0
		percent = 100 * (lst.index(i) / float(len(lst)-1))
		bar = int((int(percent) - 1) / 2 )* '=' + '>' + ' ' * int((100 - int(percent)) / 2)
		cur_time = time.perf_counter() - remain
		if(percent > 0):
			avg_cycle = (cur_time - start_time) / percent
		if lst.index(i) > 0:
			remain = f"{((100 - percent )* avg_cycle):.2f}"
			print(f"ETA: { remain:>5}s [{int(percent):>3}%][{bar:>10}] {lst.index(i)+1:>5}/{len(lst)} | elapsed time {time.perf_counter() - start_time:.2f} {'s':<2}", end='\r', file=sys.stdout, flush=True)
		remain = time.perf_counter()
		yield lst.index(i)

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(0.01)
print()
print(ret)