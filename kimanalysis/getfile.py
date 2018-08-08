import requests
import edn_format

from . import shortid

def getfile(kimid, filename, contentformat='str'):
    """
    Gets a file associated with a kim-item.

    Parameters
    ----------
    kimid : str
        The kim-id associated with the file. 
    filename : str
        The name of the file to download.
    contentformat : str
        The format to return the file contents as.  Supported values are
        'str' for str, 'edn' a dict of parsed edn content, ...  
        Default value is 'str'.

    Returns
    -------
    any
        The file contents loaded according to contentformat.
    """    
    # Download web content
    url = 'https://openkim.org/files/' + shortid(kimid) + '/' + filename
    r = requests.get(url)
    r.raise_for_status()
    
    if contentformat == 'str':
        contents = r.text
    elif contentformat == 'edn':
        contents = edn_format.loads(r.text)
    else:
        raise ValueError('contentformat value not supported')
    return contents