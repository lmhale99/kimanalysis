from __future__ import unicode_literals, print_function
import json
import requests
import pandas as pd

def rawquery(database, query=None, fields=None, map=None, reduce=None, sort=None,
             limit=None, skip=None, distinct=None, project=None, flatten=False,
             history=False, count=False, return_df=True):
    """
    Function for generic query of openkim.
    
    Parameters
    ----------
    query : dict
        MongoDB-style query. If not given, will return all results.
    fields : list
        Fields to return. If not given, will return all fields.
    map : str
        JavaScript function that operates on map of map-reduce.
    reduce : str
        JavaScript function that operates on reduce of map-reduce.
    database : str
        The database to access: obj, data, job, log, agent.
    sort : str or list
        Field(s) to sort by and direction.
    limit : int
        How many entries to retrieve.
    skip : int
        How many entries to skip.
    distinct : str
        Fields to make distint.
    project : list
        Reduce result to an array with these columns?
    flatten : bool
        Indicates if the dictionary is to be flattened
    history : bool
        Indicates if all versions are returned (True) or only the newest versions (False).
    count : bool
        If True, only returns a count of the number of items.
    """
    url = "https://query.openkim.org/api"
    
    data = {}
    data['database'] = database
    
    if query is not None:
        data['query'] = json.dumps(query)
    
    if fields is not None:
        fields_dict = {}
        for field in fields:
            fields_dict[field] = 1
        data['fields'] = json.dumps(fields_dict)
        columns = fields
    else:
        columns = None
    
    if map is not None:
        data['map'] = map
        
    if reduce is not None:
        data['reduce'] = reduce
    
    if distinct is not None:
        data['distinct'] = json.dumps(distinct)
    
    if project is not None:
        data['project'] = json.dumps(project)
        
    if sort is not None:
        data['sort'] = json.dumps(sort)
    
    if limit is not None:
        data['limit'] = json.dumps(limit)
    
    if skip is not None:
        data['skip'] = json.dumps(skip)
    
    if flatten is True:
        data['flatten'] = 'on'
        
    if history is True:
        data['history'] = 'on'
        
    if count is True:
        data['count'] = 'on'

    results = requests.post(url, data=data).json()
    
    if return_df is True:
        results = pd.DataFrame(results, columns=columns)
    
    return results