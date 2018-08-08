from __future__ import unicode_literals, print_function
from . import rawquery, alloweditemtype

def listids(itemtype, extended=False):
    """
    Returns a list of all kim ids for a given kim item type.

    Parameters
    ----------
    itemtype : str
        A kim item type
    extended : bool, optional
        Indicates if the ids are short (False, default) or extended (True).

    Returns
    -------
    list
        The ids for a given kim item type.
    """
    
    itemtype = alloweditemtype(itemtype)
    query = {"type":itemtype}
    
    if itemtype == 'tr':
        field = 'test-result-id'
    elif itemtype == 'er':
        field = 'error-result-id'
    elif itemtype == 'vr':
        field = 'verification-result-id'
    elif extended is True:
        field = 'extended-id'
    else:
        field = 'short-id'
    
    results = rawquery('obj', query=query, fields=[field])
    return results[field].tolist()
    