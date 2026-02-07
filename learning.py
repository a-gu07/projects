import numpy as np

if __name__ == "__main__":
    blank = np.ones((3,4), dtype = np.int8)
    strides = blank.strides # = (4,1): 1 byte to get to next value in row, 4 bytes to get to next row
    can_add = np.ones((4,), dtype = np.int8) # numpy will broadcast to (1,4) since rightmost size matches
    cant_add = np.ones((3,), dtype = np.int8) # cant add, as rightmost size is not same
    blank+can_add # shape: (3,4), values: all 2
    # examples of shapes that can broadcast: (2,2) and (2,), (4,3) and (1,), (50,3) and (1,3)
    # examples of shapes that cant broadcast: (2,3) and (2,2), (4,3) and (2,), (50,3) and (3,3)
    try:
        blank + cant_add
    except:
        print("Cannot broadcast")
    now_can_add = cant_add[:,np.newaxis] # turns into (3,1)
    now_can_add += np.array([[1],[2],[3]], dtype = np.int8) # column vector [2:3:4] using linalg notation
    blank + now_can_add # shape: (3,4), values: 3 for rirst row, 4 for second, 5 for last

    use_arange = np.arange(0, 10, 0.66, dtype = np.float16) # controlled step
    use_linspace = np.linspace(0, 10, 16, dtype = np.float16) # controlled number of entries

    # the outer array here is [10,20]. It is multiplied by the numbers in the inner array [2,3] to create
    # a 2d array
    np.multiply.outer([2,3], [10,20]) 

    # masks
    # must use bitwise operations $ and | on masks
    data_set = np.arange(0, 100, 1, dtype = np.int8).reshape((10, 10))
    extremes = (data_set > 75) | (data_set<25) # (10,10) array with beginning and end values as true
    fifty = data_set == 50 # (10,10) array with all except the value of 50 being false
    x_coords = np.arange(0, 10, 2, dtype = np.int8)
    y_coords = np.linspace(2, 9, 5, dtype = np.int8)
    data_set[x_coords, y_coords] = -100 # fancy indexing
    # fancy indexing can be inficient, using it on the right side of equality makes a copy, not a view
    positive_set = np.where(data_set<0, 0, data_set) # creates a copy of data set where all the -100 are set to 0

    particles = np.random.rand(1000)
    particles = particles.reshape(-1, 2) # lets numpy figure out the number of rows there should be -- > here it is (500,2)
    euclidean = np.linalg.norm(particles, axis = 1) # squashes axis = 1, making it (500,)
    euclidean_matrix = np.linalg.norm(particles, axis=1, keepdims = True) # keeps dimensions, so (500,1)

    # things to learn: np.concatenate, np.stack, np.dot(@), np.linalg.inv, np.linalg.solve, np.linalg.eig, np.einsum 
    