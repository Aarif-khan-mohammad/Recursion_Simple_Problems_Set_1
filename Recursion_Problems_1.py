def first_n_natural(n):
    if n>0:
        first_n_natural(n-1)
        print(n , end=" ")

first_n_natural(10)

def first_n_natural_reverse(n):
    if n>0:
        print(n , end=" ")
        first_n_natural_reverse(n-1)
print()
first_n_natural_reverse(10)

def first_n_odd_natural(n):
    if n>0:
        first_n_odd_natural(n-1)
        print(2*n-1 , end=" ")
        
print()
first_n_odd_natural(10)

def first_n_even_natural(n):
    if n>0:
        first_n_even_natural(n-1)
        print(2*n , end=" ")

print()
first_n_even_natural(10)

def first_n_odd_natural_reverse(n):
    if n>0:
        print(2*n-1 , end=" ")
        first_n_odd_natural_reverse(n-1)
        

print()
first_n_odd_natural_reverse(10)

def first_n_even_natural_reverse(n):
    if n>0:
        print(2*n , end=" ")
        first_n_even_natural_reverse(n-1)
        

print()
first_n_even_natural_reverse(10)

# outputs
# 1 2 3 4 5 6 7 8 9 10 
# 10 9 8 7 6 5 4 3 2 1
# 1 3 5 7 9 11 13 15 17 19
# 2 4 6 8 10 12 14 16 18 20
# 19 17 15 13 11 9 7 5 3 1
# 20 18 16 14 12 10 8 6 4 2


