"""A class for ingesting data from `.pdf` files.
This is a concrete implementation of the ingestor_interface class.
"""
from typing import List
import subprocess
import random

from .ingestor_interface import IngestorInterface
from .QuoteModel import QuoteModel
from random import randint
from .TextIngestor import TextIngestor



class PDFIngestor(IngestorInterface):
    """A class parsing quotes from .pdf formats.
    This class extracts quotes and authors and 
    constructs the Quote object.
    """
        
    allowed_extension = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Checks that file extension is correct and extracts data.
        
        Each parsed Quote object is added into a list and
        returned.
        """
        if not cls.can_ingest(path):
            raise Exception("Oh no!.. Sorry, that seems a little melodramatic... I mean: that didn't work, I'm afraid.")

        tmp = f'./tmp{random, randint(0, 1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, 'r')
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len()>0:
                parsed = line.split(' - ')
                new_quote = QuoteModel(parsed[0], parsed [1])
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes


