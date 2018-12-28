import time
import threading

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        #time.sleep(0.2)
        print('square:',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        #time.sleep(0.2)
        print('cube:',n*n*n)


def thread(arr):
    t = time.time()
    # two threads for two tasks
    t1 = threading.Thread(target= calc_square, args=(arr,))
    t2 = threading.Thread(target= calc_cube, args=(arr,))


    # exec in parallel
    t1.start()
    t2.start()

    t1.join()
    t2.join()


    print(time.time()- t)
    print("Done!")


def naive(arr):
    t = time.time()
    sq = calc_square(arr)
    cub = calc_cube(arr)
    print(sq, cub)
    print(time.time()- t)
    print("Done!")

arr = [x for x in range(5000)]
# ~9secs
#naive(arr)

# ~1 secs
thread(arr)