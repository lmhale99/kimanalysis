import pandas as pd

from .rawquery import rawquery

def allid(kimid):
    """
    Retrieves all id fields used by kim.

    Parameters
    ----------
    kimid : str
        A short-id, shortcode, extended-id, test-result-id, error-result-id or
        verification-result-id.

    Returns
    -------
    pandas.Series
        All associated ids for the item indicated by kimid
    """
    fields = ['short-id', 'shortcode', 'extended-id', 'test-result-id',
              'error-result-id', 'verification-result-id']
    query = { "$or": []}
    for field in fields:
        query['$or'].append({field:kimid})
    results = rawquery('obj', query=query, fields=fields)
    assert len(results) == 1
    return results.loc[0]
    
def shortid(kimid):
    """
    Finds short-id for a kim item.  *-result-id will be returned for result
    items.

    Parameters
    ----------
    kimid : str
        A short-id, shortcode, extended-id, test-result-id, error-result-id or
        verification-result-id.
    
    Returns
    -------
    str
        The short-id or *-result-id
    """
    results = allid(kimid)
    if pd.notnull(results['short-id']):
        return results['short-id']
    else:
        return results[pd.notnull(results)].iloc[0]

def extendedid(kimid):
    """
    Finds extended-id for a kim item.  *-result-id will be returned for result
    items.

    Parameters
    ----------
    kimid : str
        A short-id, shortcode, extended-id, test-result-id, error-result-id or
        verification-result-id.
    
    Returns
    -------
    str
        The extended-id or *-result-id
    """
    results = allid(kimid)
    if pd.notnull(results['extended-id']):
        return results['extended-id']
    else:
        return results[pd.notnull(results)].iloc[0]

def shortcode(kimid):
    """
    Finds shortcode for a kim item.  *-result-id will be returned for result
    items.

    Parameters
    ----------
    kimid : str
        A short-id, shortcode, extended-id, test-result-id, error-result-id or
        verification-result-id.
    
    Returns
    -------
    str
        The shortcode or *-result-id
    """
    results = allid(kimid)
    if pd.notnull(results['shortcode']):
        return results['shortcode']
    else:
        return results[pd.notnull(results)].iloc[0]