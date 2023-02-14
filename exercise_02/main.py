import time

#https://www.geeksforgeeks.org/python-program-for-n-th-fibonacci-number/
#https://pynative.com/python-get-execution-time-of-program/
#incorrect fib math
def fib(n):
    if n <= 0:
        return "Incorrect"
    data = [0, 1]
    if n > 2:
        for i in range(2, n):
            data.append(data[i-1] + data[i-2])
    return data[n-1]
 
print(fib(34))   
print("fib(34) "+"took "+str(time.process_time())+ " seconds")                   
