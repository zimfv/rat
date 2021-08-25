import numpy as np
import pandas as pd
import cvxpy as cp
 
def get_lines(table, name_cols=[], val_cols=None, sort=True):
    """
    Returns lines of table. Line is vectored raw.
    
    Parameters:
    -----------
    table : DataFrame
        Table
            
    name_cols : array_like
        List of name-containing columns names 
                
    val_cols : array_like
        List of value-containing columns names
               
    sort : bool
        Should the table be sorted by name_cols?
        
    Returns
    -------
    line : ndarray
        Matrix of size (len(table), len(val_cols))
    
    """
    if val_cols is None:
        val_cols = np.setdiff1d(table.columns, name_cols)
    if sort:
        table = table.sort_values(by=name_cols)
    line = table[val_cols].values
    return line


def get_system(line_a, line_b):
    """
    Returns matrix and vector of system with n+m condition-equations with rank n+m-1 if line_a.sum() == line_b.sum()
    
    Parameters:
    -----------
    line_a : ndarray
        vector
        
    line_b : ndarray
        vector
    
    
    Returns:
    --------
    matrix : ndarray
        Matrix of size ()
        
    r : ndarray:
        Vector of size len(line_a) + len(line_b)
    
    """
    n = len(line_a)
    m = len(line_b)
    line_a, line_b = line_a.astype(float), line_b.astype(float)
    if (line_a.astype(int) == line_a).all() and (line_b.astype(int) == line_b).all():
        line_a, line_b = line_a.astype(int), line_b.astype(int)
    
    r = np.concatenate([line_a, line_b])
    matrix_a = np.concatenate(
        [
            np.concatenate([np.zeros(i*m), np.ones(m), np.zeros(m*(n-i-1))]).reshape([1, n*m]) for i in range(n)
        ]
    )
    matrix_b = np.concatenate([np.eye(m) for i in range(n)], axis=1)
    matrix = np.concatenate([matrix_a, matrix_b]).astype(int)
    return matrix, r


def get_problem(line_a, line_b, integer=False, nonneg=True, obj_type='dependences'):
    """
    Returns cvxpy-problem and variable.
    
    Parameters:
    -----------
    line_a : ndarray
        vector
        
    line_b : ndarray
        vector
        
    integer : bool
        Should the solve be integer?
        Use correct solver in restore_line. Some of them must be installed separately.
        https://www.cvxpy.org/tutorial/advanced/index.html
        
    nonneg : bool
        Should the solve be nonnegative?
        
    obj_type : str or function
        Type of minimizing object.
        If that is function, then will be minimize value obj_type(x) by x,
        Else:
            'squares' : minimize sum of squares : (x_ij)^2
            'dependeces' : minimize sum of dependence values : (s*x_ij - a_i*b_j)^2
    
    Returns:
    --------
    prob : Problem
        cvxpy.problems.problem.Problem
    
    x : Variable
        cvxpy.expressions.variable.Variable
    
    """
    A, r = map(lambda i: i[:-1], get_system(line_a, line_b))
    x = cp.Variable(len(line_a)*len(line_b), integer=integer, nonneg=nonneg)
    constraints = [A @ x == r]
    
    if obj_type == 'squares':
        objective = cp.Minimize(cp.sum_squares(x))
    elif obj_type == 'dependences':
        s = line_a.sum()
        long_a = np.repeat(line_a, len(line_b))
        long_b = np.concatenate([line_b for i in line_a])
        objective = cp.Minimize(cp.sum_squares(s*x - long_a*long_b))
    else:
        objective = cp.Minimize(obj_type(x))
        
    prob = cp.Problem(objective, constraints)
    return prob, x


def restore_line(line_a, line_b, integer=False, nonneg=True, obj_type='dependences', solver='SCS', 
                 correct=True, print_status=False, throw_sums_error=True):
    """
    Returns line vector restored from two lines (optimized by minimizing squares sum)
    
    Parameters:
    -----------
    line_a : ndarray
        Vector
        
    line_b : ndarray
        Vector
    
    integer : bool
        Should the solve be integer?
        Use correct solver. Some of them must be installed separately.
        https://www.cvxpy.org/tutorial/advanced/index.html
        
    nonneg : bool
        Should the solve be nonnegative?
        
    obj_type : str or function
        Type of minimizing object.
        If that is function, then will be minimize value obj_type(x) by x,
        Else:
            'squares' : minimize sum of squares : (x_ij)^2
            'dependeces' : minimize sum of dependence values : (s*x_ij - a_i*b_j)^2
    
    solver : string
        Solver keyword argument.
    
    correct: bool
        Should mistake be corrected?
    
    print_status : bool
        Should status be printed, when the problem be solved?
    
    throw_sums_error: bool
        Should the program be broken, where line_a and line_b has no equivalunt sums?
    
    
    Returns:
    --------
    line_res : ndarray
        Vector of size len(line_a)*len(line_b)
    
    """
    if (line_a.sum() != line_b.sum()) and throw_sums_error:
        print((line_a.sum() != line_b.sum()), throw_sums_error, (line_a.sum() != line_b.sum()) and throw_sums_error)
        raise ValueError('Different sums.')
    prob, x = get_problem(line_a, line_b, integer=integer, nonneg=nonneg, obj_type=obj_type)
    prob.solve(solver=solver)
    if print_status:
        print("Status: ", prob.status)
        print("The optimal value is", prob.value)
        print("A solution x is")
        print(x.value, '\n')
    line_res = x.value.copy()
    if correct and (line_res.sum() != line_a.sum()):
        line_res[np.argmax(abs(line_res))] += line_a.sum() - line_res.sum()
    return line_res