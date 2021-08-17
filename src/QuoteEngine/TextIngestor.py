"""A class for ingesting data from `.txt` files.
This is a concrete implementation of the ingestor_interface class.
"""
from typing import List

from .ingestor_interface import IngestorInterface
from .QuoteModel import QuoteModel




class TextIngestor(IngestorInterface):
    """A class parsing quotes from .txt formats.
    This class extracts quotes and authors and 
    constructs the Quote object.
    """
    
    allowed_extension = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Checks that file extension is correct and extracts data.
        
        Each parsed Quote object is added into a list and
        returned.
        """
        if not cls.can_ingest(path):
            raise Exception("Oh no!.. Sorry, that seems a little melodramatic... I mean: that didn't work, I'm afraid.")

        quotes = []

        with open(path, 'r') as i:
            lines = i.readlines()

        for row in lines:
            quote, author = row.split("-")
            quotes.append(QuoteModel(quote.strip(), author.strip()))

        return quotes
