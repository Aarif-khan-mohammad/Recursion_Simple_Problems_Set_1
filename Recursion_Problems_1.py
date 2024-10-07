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


