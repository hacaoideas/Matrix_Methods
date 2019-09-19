import numpy as np 


def flip_sign(arr):
    '''Simple function that takes in an array and return
    shuffled version of the array with some elements with their sign inverted'''
    mask = np.random.randint(low=0, high=2, size=arr.shape, dtype=bool)
    arr[mask] = arr[mask]*(-1)
    return arr


if __name__ == "__main__":
    a = np.arange(10)
    print(a)
    print(flip_sign(a))
