# %% ---------------------------------------------------------------------------------------
"""
© https://sudipghimire.com.np

Tuple Exercises

Please read the note carefully and try to solve the problem below:

"""

"""
1. Write a program to create a tuple to  add 5 different numbers.
    a. find out the length of the tuple
    b. find out the 3rd element of the tuple by accessing it through the index
    c. use `enumerate()` function to map each element with its index and print it using the foreach loop
        - please see the reference to the file 02_data_types/06_tuples.py

"""
## ------------------------------------------
# answer 1
num = (1,2,3,4,5)
print(num)
type(num)

# %% ------------------------------------------
# a
num_len = num.__len__() 
print(num_len)

# %% ------------------------------------------
# b
num_index_pos, num_index_neg  = num[2], num[-3]

print(f'The 3rd element using positive index position is {num_index_pos}, and using negative index position {num_index_neg}.')

# %% ------------------------------------------
# c
num_enum = enumerate(num)
for (index, numbers) in num_enum:
    print(f'The index {index} has the element {numbers}.')

# %% ---------------------------------------------------------------------------------------
"""
2. Write a program to create a nested tuple and access different elements of the inner tuple using
   positive and negative index positions.

"""
nst_tuple = (
    (1,2,3,4,5),
    ("Ram", "Shyam", "Hari", "Krishna", "Arun"),
    ("USA", "Nepal", "UK", "India", "China")
)
## accessing 4 from the nested tuple
print(f'The element "4" using positive index position and negative index position are ({nst_tuple[0][3]}, {nst_tuple[-3][-2]}).')

## accessing "Hari" from the nasted tuple
print(f'The element "Hari" using positive index position and negative index position are ({nst_tuple[1][2]}, {nst_tuple[-2][-3]}).')

## accessing "Nepal" from the nasted tuple
print(f'The element "Nepal" using positive index position and negative index position are ({nst_tuple[2][1]}, {nst_tuple[-1][-4]}).')

# %% ---------------------------------------------------------------------------------------

"""
Bonus:
3. create two different tuples t1 and t2 with different elements inside it
    a. create the next tuple t3 to add all values of t1 and t2 using the destructuring method

    - suppose t1 has (1,6,9,4,3)
    - and t2 has (2,7,8,3,5)
    -t3 must have (1,6,9,4,3,2,7,8,3,5)
    - make sure to use destructuring method using `*` operator in the tuples
"""
## Creating two different tuples t1 and t2
t1, t2 = (1,2,3,4,5), ("Ram", "Shyam", "Hari", "Krishna", "Arun")

# a
## create tuple t3 to add all values of t1 amd t2 using the destructuring method
t3 = (*t1, *t2)
print(t3) 

# %% ---------------------------------------------------------------------------------------
