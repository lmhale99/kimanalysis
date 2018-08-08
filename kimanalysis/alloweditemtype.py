from __future__ import unicode_literals, print_function
def alloweditemtype(itemtype):
    """
    Checks that a specified KIM item type is allowed and converts it to the
    form used to access records from the obj database.

    Parameters
    ----------
    itemtype : str
        A KIM item type descriptor. May be a full descriptive name or the
        short two letter database type value.

    Returns
    -------
    str
        The short two letter database type value associated with the item type.
    """
    types = {}
    types['model-driver'] = 'md'
    types['model'] = 'mo'
    types['test-driver'] = 'td'
    types['test'] = 'te'
    types['verification-check'] = 'vc'
    types['reference-data'] = 'rd'
    types['test-result'] = 'tr'
    types['verification-result'] = 'vr'
    types['error-result'] = 'er'
    
    if itemtype in types:
        return types[itemtype]
    elif itemtype in types.values():
        return itemtype
    else:
        raise ValueError('Unknown item type: ', itemtype)

def allowedresultstype(resultstype):
    """
    Checks that a specified KIM results type is allowed and converts it to the
    form used to access records from the data database.

    Parameters
    ----------
    resultstype : str
        A KIM results type descriptor. May be a full descriptive name or the
        short two letter database type value.

    Returns
    -------
    str
        The short two letter database type value associated with the results type.
    """
    types = {}
    types['reference-data'] = 'rd'
    types['test-result'] = 'tr'
    types['verification-result'] = 'vr'
    types['error-result'] = 'er'
    
    if resultstype in types:
        return types[resultstype]
    elif resultstype in types.values():
        return resultstype
    else:
        raise ValueError('Unknown results type: ', resultstype)