def main():
    #Partial permutation formula P(n,k) = n!/(n-k)!

    from math import factorial

    n = 83
    k = 10
    diff = n - k 

    n_fac = factorial(n)
    diff_fac = factorial(diff)

    partial_perms = ((n_fac)/(diff_fac)) % 1000000

    print partial_perms


main()