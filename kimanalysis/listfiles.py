#!/usr/bin/env python
from lxml import etree
import requests
import numpy as np
from . import extendedid

def listfiles(itemid):
    """
    Lists available content associated with a kim-item.

    Parameters
    ----------
    itemid : str
        The id for the kim-item.

    Returns
    -------
    list
        The names of the associated content.
    """
    # Access webpage for kimid
    url = 'https://openkim.org/dev-kim-item/' + extendedid(itemid)
    r = requests.get(url)
    try:
        r.raise_for_status()
    except:
        url = 'https://openkim.org/dev-kim-item/' + '-'.join(np.array(itemid.split('-'))[[0,1,2,4]])
        r = requests.get(url)
        r.raise_for_status()    
    
    html = etree.fromstring(r.text, parser=etree.HTMLParser())

    # Build list of all contents associated with the contenttype
    xpath = ".//a[@id='files']/../.."
    contenthtml = html.find(xpath)
    if contenthtml is None:
        raise ValueError('files not found for kim item')

    tablexpath = ".//table"
    contents = []
    for table in contenthtml.findall(tablexpath):
        for alink in table.findall('.//tr/td[1]/a'):
            contents.append(alink.text)

    return contents