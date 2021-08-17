import numpy as np
import pandas as pd


def roll_weak(table, cols_target, value_name='Value', res_name='Count'):
    """
    Return table with taken columns (cols_target) to one column.
    
    Parameters:
    -----------
    table : DataFrame
        Editing table
    
    cols_target : array-like
        List of target column names
    
    value_name : string
        Name of column containing column names
    
    res_name : string:
        Name of column containing values
        
    Returns:
    --------
    res : DataFrame
        Table
    
    """
    cols_names = np.setdiff1d(table.columns, cols_target)
    res = pd.DataFrame(np.repeat(table[cols_names].values, len(cols_target), axis=0), columns=cols_names)
    res[value_name] = np.concatenate([cols_target for i in table.index])
    res[res_name] = np.concatenate(table[cols_target].values)
    return res


def roll_strong(table, cols_names, cols_target, cols_values, index_prefix='col_', value_name='Value'):
    """
    Return two tables ...
    
    Parameters:
    -----------
    table : DataFrame
        Editing table
    
    cols_names : array_like
        List of nonchanging column names
    
    cols_target : array-like
        List of target column names
    
    cols_values : array-like
        List of value containing column names
    
    index_prefix : string
        The template for naming column identifiers
    
    value_name : string
        Name of column containing values
    
    Returns:
    --------
    res_values : DataFrame
        Edited table
    
    res_col_names : DataFrame
        Info about columns
    
    """
    table = table.sort_values(by=list(np.concatenate([cols_names, cols_target]))).reset_index() 
    
    res_col_names = table[cols_target].drop_duplicates().reset_index(drop=True) 
    res_col_names = res_col_names.iloc[np.repeat(np.arange(len(res_col_names)), len(cols_values))].reset_index(drop=True)
    res_col_names[value_name] = list(cols_values)*len(table[cols_target].drop_duplicates())
    res_col_names.index = np.char.add(index_prefix, res_col_names.index.astype(str))
    
    res_names = table[cols_names].drop_duplicates().reset_index(drop=True) 
    res_values = []
    len_col_names = len(table[cols_target].drop_duplicates())
    for i in res_names.index:
        i_i = i*len_col_names + np.arange(len_col_names)
        s = np.concatenate([table.loc[i_i, col].values for col in cols_values])
        res_values.append(s)
    res_values = np.array(res_values)
    res_values = pd.DataFrame(data=res_values, columns=res_col_names.index)
    res_values = pd.DataFrame(data=np.concatenate([res_names.values, res_values.values], axis=1), 
                              columns=np.concatenate([res_names.columns, res_values.columns]))
    
    return res_values, res_col_names


def correct_table(table, columns, sums, by_div=True, by_add=True):
    """
    Return table with corrected columns-sums to real sums.
    
    Parameters :
    ------------
    table : DataFrame
        Editing table
    
    columns : array-like
        List of value containing column names
    
    sums : array-like
        List of real sums
    
    by_div : boolean
        Should the problem be solved by division table by its sums and multipl that by real?
    
    by_add : boolean
        Should the problem be solved by adding different of sums to maximal value?
    
    """
    res = table.copy()
    for i in range(len(table.index)):
        index = table.index[i]
        if (res.loc[index, columns].sum() != sums[i]) and by_div:
            res.loc[index, columns] *= sums[i] / res.loc[index, columns].sum()
        if (res.loc[index, columns].sum() != sums[i]) and by_add:
            line = res.loc[index, columns].values
            line[np.argmax(abs(line))] += sums[i] - res.loc[index, columns].sum()
            res.loc[index, columns] = line
    return res