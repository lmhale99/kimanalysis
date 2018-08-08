import os
import requests
import tempfile
from zipfile import ZipFile
from . import shortid

def getallfiles(kimid, path='archive.zip'):
    """
    Downloads all source files associated with a model

    Parameters
    ----------
    kimid : str
        The kim id to access all data for.
    path : str, optional
        The path to where the downloaded zip file is to be saved.  Default
        value is 'archive.zip'
    Returns
    -------
    zipfile
        The downloaded contents.
    """
    url = 'https://openkim.org/download/' + shortid(kimid) + '.zip'    
    r = requests.get(url)
    r.raise_for_status()
    
    with open(path, 'wb') as f:
        f.write(r.content)
    modelzip = ZipFile(path)
    
    return modelzip 