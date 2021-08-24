import numpy as np
import pandas as pd
from rat.ratmath import get_lines, restore_line
from rat.ratedit import roll_strong
import time


def get_names_and_targets(table_a, table_b, name_cols=None, targets_a=None, targets_b=None):
    """
    Returns arrays of name columns, target columns from table_a and target columns from table_a.
    
    Parameters:
    -----------
    table_a : DataFrame or array-like
        Left table or list of thats columns names
    
    table_b : DataFrame or array-like
        Right table or list of thats columns names
    
    name_cols : array-like or None
        List of name-containing columns names (from both tables)
        If it's None, then it will be defined.
    
    targets_a : array-like or None
        List of value-containing columns from left table
        If it's None, then it will be defined.
        
    targets_b : array-like or None
        List of value-containing columns from right table
        If it's None, then it will be defined.
    
    Returns:
    --------
    name_cols : array-like
        List of name-containing columns names (from both tables)
    
    targets_a : array-like
        List of value-containing columns from left table
        
    targets_b : array-like
        List of value-containing columns from right table
    
    """
    try:
        cols_a = table_a.columns
        cols_b = table_b.columns
    except AttributeError:
        cols_a = table_a
        cols_b = table_b
    if name_cols is None:
        name_cols = np.intersect1d(cols_a, cols_b)
    if targets_a is None:
        targets_a = np.setdiff1d(cols_a, name_cols)
    if targets_b is None:
        targets_b = np.setdiff1d(cols_b, name_cols)
    return name_cols, targets_a, targets_b


def get_rows_target_names(targets_a, targets_b):
    """
    Returns column-arrays of targets for one name.
    
    Parameters:
    -----------
    targets_a : array-like
        List of value-containing columns from left table
        
    targets_b : array-like
        List of value-containing columns from right table
    
    Returns:
    --------
    rows_target_names_a : ndarray
        Values for left target column
    
    rows_target_names_b : 
        Values for right target column
    
    """
    rows_target_names_a = np.repeat(targets_a, len(targets_b))
    rows_target_names_b = np.concatenate([targets_b for i in targets_a])
    return rows_target_names_a, rows_target_names_b


def restore_table(table_a, table_b, 
                  name_cols=None, targets_a=None, targets_b=None, 
                  name_a='A', name_b='B', name_res='X', 
                  integer=False, nonneg=True, obj_type='square_covs', solver='SCS', 
                  correct=True, print_status=False, throw_sums_error=True):
    """
    Returns one simple-restored table ("simple" means "do not roll column to columns")
    
    Parameters:
    -----------
    table_a : DataFrame or array-like
        Left table or list of thats columns names
    
    table_b : DataFrame or array-like
        Right table or list of thats columns names
        
    name_cols : array-like or None
        List of name-containing columns names (from both tables)
        If it's None, then it will be defined.
    
    targets_a : array-like or None
        List of value-containing columns from left table
        If it's None, then it will be defined.
        
    targets_b : array-like or None
        List of value-containing columns from right table
        If it's None, then it will be defined.
        
    name_a : string
        Name of column contains target columns from left table
        
    name_b : string
        Name of column contains target columns  from right table
    
    name_res : string
        Name of result value column
    
    integer : bool
        Should the solve be integer?
        Use correct solver. Some of them must be installed separately.
        https://www.cvxpy.org/tutorial/advanced/index.html
        
    nonneg : bool
        Should the solve be nonnegative?
        
    solver : string
        Solver keyword argument
    
    correct: bool
        Should mistake be corrected?
    
    print_status : bool
        Should status be printed, when the problem be solved?
    
    throw_sums_error: bool
        Should the program be broken, where line_a and line_b has no equivalunt sums?
    
    Returns:
    --------
    table_res : DataFrame
        "Restored" table
    
    """
    name_cols, targets_a, targets_b = get_names_and_targets(table_a, table_b, name_cols, targets_a, targets_b)
    len_a = len(targets_a)
    len_b = len(targets_b)
    
    table_a = table_a.sort_values(by=list(name_cols))
    table_b = table_b.sort_values(by=list(name_cols))
    
    table_res = pd.DataFrame(np.repeat(table_a[name_cols].values, len_a*len_b, axis=0), 
                             columns=name_cols).astype(str)
    
    rows_target_names_a, rows_target_names_b = get_rows_target_names(targets_a, targets_b)
    table_res[name_a] = np.concatenate([rows_target_names_a for i in range(len(table_a))])
    table_res[name_b] = np.concatenate([rows_target_names_b for i in range(len(table_b))])
    
    lines_a = get_lines(table_a, name_cols=list(name_cols), val_cols=list(targets_a), sort=True)
    lines_b = get_lines(table_b, name_cols=list(name_cols), val_cols=list(targets_b), sort=True)
    lines_res = [restore_line(lines_a[i], lines_b[i], integer=integer, nonneg=nonneg, obj_type=obj_type, 
                              solver=solver, correct=correct, print_status=print_status, 
                              throw_sums_error=throw_sums_error) for i in range(len(lines_a))]
    table_res[name_res] = np.concatenate(lines_res)
    
    return table_res


def restore_alot(tables, name_cols, tab_names=None, name_res='X', 
                 tab_name_prefix='Table_', name_fluid='__FLUID__', 
                 integer=False, nonneg=True, obj_type='square_covs', solver='SCS', 
                 correct=True, print_status=False, print_time=False, 
                 throw_sums_error=False):
    """
    Returns table - consistently restored from =tables.
    
    Parameters:
    -----------
    tables : list
        List of tables
    
    name_cols : array-like
        List of name-containing columns names (from all tables)
    
    tab_names : array-like or None
        List of value names for each table
        If it's None, then it will be defined.
    
    name_res : string
        Name of result value column
    
    tab_name_prefix : string
        Prefix for generete tab_names if it's None.
        
    name_fluid : string
        name_res in interim tables
    
    integer : bool
        Should the solve be integer?
        Use correct solver. Some of them must be installed separately.
        https://www.cvxpy.org/tutorial/advanced/index.html
        
    nonneg : bool
        Should the solve be nonnegative?
        
    solver : string
        Solver keyword argument
    
    correct: bool
        Should mistake be corrected?
    
    print_status : bool
        Should status be printed, when the problem be solved?
    
    print_time : bool
        Should time for every restoring be printed?
    
    throw_sums_error: bool
        Should the program be broken, where line_a and line_b has no equivalunt sums?
    
    Returns:
    --------
    table_res : DataFrame
        "Restored" table
    
    """
    if tab_names is None:
        tab_names = np.char.add(tab_name_prefix, np.arange(len(tables)).astype(str))
    if len(tables) > len(tab_names):
        raise ValueError('Different list lengths.\nlen(val_names) < len(tables)')
    
    if len(tables) == 0:
        return pd.DataFrame()
    if len(tables) == 1:
        return tables[0]
    
    if print_time:
        start = time.monotonic()
        
    big = restore_table(tables[0], tables[1], name_cols=name_cols, 
                        name_a=tab_names[0], name_b=tab_names[1], name_res=name_res, 
                        integer=integer, nonneg=nonneg, obj_type=obj_type, solver=solver, 
                        correct=correct, print_status=print_status, 
                        throw_sums_error=throw_sums_error)
    if print_time:
        message = 'Tables ' + tab_names[0] + ' and ' + tab_names[1] + ' were disaggregated by '
        message += str('%.4f' % (time.monotonic() - start)) + ' seconds.'
        print(message)
        
    for i in range(2, len(tables)):
        if print_time:
            start = time.monotonic()
            
        big, big_names = roll_strong(big, cols_names=name_cols, 
                                     cols_target=np.setdiff1d(big.columns, np.append(name_cols, name_res)),
                                     cols_values=[name_res])
        big = restore_table(big, tables[i], name_cols=name_cols, 
                            name_a=name_fluid, name_b=tab_names[i], name_res=name_res, 
                            integer=integer, nonneg=nonneg, obj_type=obj_type, solver=solver, 
                            correct=correct, print_status=print_status, 
                            throw_sums_error=throw_sums_error)
        big = big.merge(big_names, how='left', left_on=name_fluid, right_index=True)
        big = big[np.concatenate([name_cols, tab_names[:i+1], [name_res]])]
        if print_time:
            message = 'Table ' + tab_names[i] + ' was disaggregated and added to result by '
            message += str('%.4f' % (time.monotonic() - start)) + ' seconds.'
            print(message)
    return big