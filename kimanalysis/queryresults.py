from __future__ import unicode_literals, print_function

import pandas as pd

import kimanalysis.unitconvert as uc
from . import rawquery, allowedresultstype, extendedid
from .compatibility import range

def queryresults(resultstype=None, test=None, model=None, verificationcheck=None,
                 species=None, hasfield=None, query=None, limit=None,
                 skip=None, process=True):
    """
    Fetches results records from the data database based on listed parameters.

    Parameters
    ----------
    resultstype : str, optional
        A type of results to limit the search by.
    test : str, optional
        An id for a kim test to limit the search by.
    model : str, optional
        An id for a kim model to limit the search by.
    verificationcheck : str, optional
        An id for a kim verification-check to limit the search by.
    species : list, optional
        A list of elemental species to limit the search by.
    hasfield : str, optional
        Limits search to records that contain the specified field.
    query : str, optional
        A mongoDB query to submit to the data database.  Allows for more
        complex search capabilities. Some queries not allowed if it conflicts
        with the queries built by the properties above.
    limit : int, optional
        A maximum number of matching records to return.
    skip : int, optional
        The number of records to skip before returning.  Can be used with limit
        to retrieve large numbers of records in smaller groups.
    process : bool, optional
        Indicates if the returned information is processed to a flat table
        (True, default), or returned as included in the database (False).
    
    Returns
    -------
    pandas.DataFrame
        The matching results records in tabular form.

    Raises
    ------
    AssertionError
        If query includes terms that conflict with other parameters
    """
    if query is None:
        query = {}

    if resultstype is not None:
        assert 'meta.type' not in query, repr(query)
        query['meta.type'] = allowedresultstype(resultstype)
    
    if test is not None:
        assert 'meta.test' not in query, repr(query)
        query['meta.test'] = extendedid(test)
        
    if model is not None:
        assert 'meta.model' not in query, repr(query)
        query['meta.model'] = extendedid(model)
    
    if verificationcheck is not None:
        assert 'meta.verification-check' not in query, repr(query)
        query['meta.verification-check'] = extendedid(verificationcheck)

    if species is not None:
        assert 'species.source-value' not in query, repr(query)
        #query['species.source-value'] = {'$in' : species}
        query['species.source-value'] = {'$all': species, '$not':{'$elemMatch': {'$nin': species}}}

    if hasfield is not None:
        assert hasfield not in query, repr(query)
        query[hasfield] = { "$exists": "true", "$ne": "null" }
        
    results = rawquery('data', query=query, limit=None, skip=None, return_df=False)
    
    if process is True:
        for i in range(len(results)):
            for key in results[i]:
                try:
                    results[i][key] = uc.set_from_dict(results[i][key])
                except:
                    pass  

            results[i]['model'] = results[i]['meta']['model']
            try:
                results[i]['test'] = results[i]['meta']['test']
            except:
                pass
            try:
                results[i]['test-result-id'] = results[i]['meta']['test-result-id']
            except:
                pass
            try:
                results[i]['verification-check'] = results[i]['meta']['verification-check']
            except:
                pass
            try:
                results[i]['verification-result-id'] = results[i]['meta']['verification-result-id']
            except:
                pass
            del(results[i]['meta'])
    
    return pd.DataFrame(results)