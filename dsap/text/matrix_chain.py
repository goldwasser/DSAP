"""Provides matrix_chain function as an example of dynamic programming."""

def matrix_chain(d):
    """Return a solution to the matrix chain problem.

    d is a list of n+1 integers describing the dimensions of a chain of
    n matrices such that matrix A_k has dimensions d[k]-by-d[k+1].

    Return an n-by-n table such that N[i][j] represents the minimum number of
    multiplications needed to compute the product of A_i through A_j inclusive.
    """
    n = len(d) - 1                       # number of matrices
    N = [[0] * n for i in range(n)]      # initialize n-by-n result to zero
    for b in range(1, n):                # number of products in subchain
        for i in range(n-b):             # start of subchain
            j = i + b                    # end of subchain
            N[i][j] = min(N[i][k] + N[k+1][j] + d[i]*d[k+1]*d[j+1] for k in range(i,j))
    return N
