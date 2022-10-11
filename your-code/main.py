#1. Import the NUMPY package under the name np.
from logging import exception
import numpy as np


#2. Print the NUMPY version and the configuration.
print('--------------------------------------1-2-----------------------------')
print(np.__version__)
print(np.show_config())


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a1 = np.random.random((2, 3, 5))
a2 = np.random.sample((2, 3, 5))
a3 = np.random.randint(5, size = (2,3,5))


#4. Print a.
print('-------------------------------------3-4-----------------------------')
print(a1)
print('-------------------------------------------------------------------')
print(a2)
print('-------------------------------------------------------------------')
print(a3)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones((5,2,3))


#6. Print b.
print('-------------------------------------5-6------------------------------')
print(b)


#7. Do a and b have the same size? How do you prove that in Python code?
print('-------------------------------------7------------------------------')

if a1.size == b.size:
        print('They have the same size')
else:
        print('They have a different size')



#8. Are you able to add a and b? Why or why not?
print('-------------------------------------8------------------------------')
try: a1+b
except: 
        print('operands could not be broadcast together with shapes (2,3,5) (5,2,3), same size but different shapes')



#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
print('------------------------------------9-------------------------------')
c = np.transpose(b, (1,2,0))
print(c)
print()
print(c.shape)


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
print('\n--------------------------------10----------------------------------')
d = a1 + c
print(d)

#Now it works

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print('\n--------------------------------11-----------------------------------')
print(a1[0][0][0])
print()
print(d[0][0][0])
print()
print('We just add 1 to a1')


#12. Multiply a and c. Assign the result to e.
print('\n--------------------------------12-----------------------------------')
e = a1*c
print(e)


#13. Does e equal to a? Why or why not?
print('\n--------------------------------13-----------------------------------')
if np.array_equal(e, a1):
        print('They are equal')    




#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
print('\n--------------------------------14-----------------------------------')
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)
print(f'The mean of d is {d_max}, the minimum is {d_min}, and the mean is {d_mean}')



#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
print('\n--------------------------------15-16-----------------------------------')
f = np.empty([2,3,5])


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

f = []
for out_list in d:
        for in_list in out_list:
                for x in in_list:
                        if d_min < x < d_mean:
                                f.append(25)
                        if d_mean < x < d_max:
                                f.append(75)
                        if x == d_mean:
                                f.append(50)
                        if x == d_min:
                                f.append(0)
                        if x == d_max:
                                f.append(100)

f = np.reshape(f, d.shape)
print(f)


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print('\n--------------------------------17-----------------------------------')
print(d)
print()
print(f)

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""
print('\n--------------------------------18-----------------------------------')

j = []
for x in np.nditer(d):
    if d_min < x < d_mean:
        j += ['B']
    if d_mean < x < d_max:
        j += ['D']
    if x == d_mean:
        j += ['C']
    if x == d_min:
        j += ['A']
    if x == d_max:
        j += ['E']

j = np.reshape(j, d.shape)
print(j)        

