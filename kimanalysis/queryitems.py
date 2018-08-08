from . import alloweditemtype, rawquery
import pandas as pd
def queryitems(itemtype=None, driver=None, query=None,
               limit=None, skip=None, process=True):
    """
    Query KIM items in the database.
    
    Parameters
    ----------
    itemtype : str, optional
        The KIM item type
    query : dict
        A MongoDB-style query
        
    Returns
    -------
    pandas.DataFrame
        The records for the matching items.
    """
    if query is None:
        query = {}

    if driver is not None:
        query["$or"] = [{'driver.extended-id':driver}, {'driver.short-id':driver}, {'driver.shortcode':driver}]

    if itemtype is not None:
        assert 'type' not in query
        query['type'] = alloweditemtype(itemtype)
    
    results = rawquery('obj', query=query, return_df=False, limit=limit, skip=skip)

    if process is True:
        for i in range(len(results)):

            try:
                results[i]['driver'] = results[i]['driver']['extended-id']
            except:
                pass

    return pd.DataFrame(results)