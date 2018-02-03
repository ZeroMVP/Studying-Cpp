import sys
num_steps = int(sys.argv[1])
max = num_steps
while(num_steps>0):
    spa = " " * (num_steps - 1)
    sh = "#" * (max - num_steps + 1)
    print(spa + sh)
    num_steps-=1

