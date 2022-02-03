# %% ---------------------------------------------------------------------------------------

"""
© https://sudipghimire.com.np

Sets Exercises

Please read the note carefully and try to solve the problem below:

"""

"""
1. Write a program to create two different set of countries
    i.  rich: {'USA', 'China', 'Japan', 'Germany', 'France', 'Australia', 'Italy'}
    ii. europe: {'Germany', 'France', 'England', 'Switzerland', 'Italy', 'Portugal', 'Sweden'}

    Use the Set methods to find out:

    a. countries that are rich but not in Europe
    b. countries that are in Europe but not rich
    c. countries that are both rich and are in Europe
    d. countries that are either rich or in Europe, but not both
    e. all the countries in either of the sets. (Names must be unique)
    f. see if two sets are disjoint or not
    g. now remove the common countries from the `rich` set and check if two sets are disjoint or not.
        - hint: use `difference_update()` method. for more, please refer to python documentation
"""
# %% ------------------------------------------
# answer 1.
rich, europe = {'USA', 'China', 'Japan', 'Germany', 'France', 'Australia', 'Italy'}, {'Germany', 'France', 'England', 'Switzerland', 'Italy', 'Portugal', 'Sweden'}
print(rich, europe)

# %% ------------------------------------------
# a 
print(f'Countries that are rich but not in Europe are: {rich - europe}.') 

# %% ------------------------------------------
# b
print(f'Countries that are in Europe but not rich are: {europe - rich}.') 

# %% ------------------------------------------
# c
print(f'Countries that are both rich and are in Europe are: {europe & rich}.') 

# %% ------------------------------------------
# d
print(f'Countries that are either rich or in Europe, but not both: {europe ^ rich}.') 


# %% ------------------------------------------
# e
print(f'All the countries in either of the sets are: {europe | rich}.') 

# %% ------------------------------------------
# f
print(f'rich and europe are disjoint Sets? => {rich.isdisjoint(europe)}.') 

# %% ------------------------------------------
# g
## Removing the common countries from the `rich` set
rich_1 = rich.copy()
rich_1.difference_update(europe)
print(rich_1)

print(f'rich and europe are disjoint Sets? => {rich_1.isdisjoint(europe)}.') 

# %% ---------------------------------------------------------------------------------------
"""
2. Create two more sets
    i.  `asian_rich` and add {'China', 'Japan'} to it.
    ii. `american_rich` and add {'USA', 'Canada'} to it.
   and check whether:

   a. `asian_rich` is a subset of `rich` or not
   b. `rich` is a superset of `asian_rich` or not
   c. `american_rich` is a subset of `rich` or not

"""
# %% ------------------------------------------
# answer 2
asian_rich, american_rich = {'China', 'Japan'}, {'USA', 'Canada'} 
print(asian_rich, american_rich)
# %% ------------------------------------------
# a
print(f'Does `asian_rich` is a subset of `rich`? => {asian_rich <= rich}.') 

# %% ------------------------------------------
# b
print(f'Does `rich` a superset of `asian_rich`? => {rich >= asian_rich}.')

# %% ------------------------------------------
# c
print(f'Does `american_rich` is a subset of `rich`? => {american_rich <= rich}.')

# %% ---------------------------------------------------------------------------------------
