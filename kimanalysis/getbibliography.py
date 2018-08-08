import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

import requests

from . import shortid

def getbibliography(kimid):
    url = 'https://openkim.org/dev-kim-item/' + shortid(kimid) + '/citation-bibtex'
    
    r = requests.get(url)
    r.raise_for_status()

    parser = BibTexParser()
    parser.customization = convert_to_unicode
    return bibtexparser.loads(r.text, parser=parser).entries