from . import rawquery

def getitem(itemid):
    """
    Get a KIM item record using one of the item's ids
    
    Parameters
    ----------
    itemid : str
        The item's extended-id, short-id, or shortcode.
        
    Returns
    -------
    pandas.Series
        The record for the item.
    """
    query = { "$or": [{'extended-id':itemid}, {'short-id':itemid}, {'shortcode':itemid}]}
    results = rawquery('obj', query=query)
    assert len(results) == 1
    return results.iloc[0]