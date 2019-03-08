import time 
import random

if __name__ == "__main__":
    num = input("input number of data: ")
    arr = [random.randint(1,100000) for i in range(0,int(num))]
    jum = 0
    start = time.time()
    for data in arr:
        jum += data
    end = time.time()
    print("sum: ",jum)
    print("time: ",end-start)
    


    