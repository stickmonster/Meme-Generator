"""A class for ingesting data from `.csv` files.
This is a concrete implementation of the ingestor_interface class.
"""
from typing import List
import pandas
from .ingestor_interface import IngestorInterface
from .QuoteModel import QuoteModel



class CSVIngestor(IngestorInterface):
    """A class parsing quotes from .csv formats.
    This class extracts quotes and authors and 
    constructs the Quote object.
    """

    allowed_extension = ['csv']


    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Checks that file extension is correct and extracts data.
        
        Each parsed Quote object is added into a list and
        returned.
        """
        if not cls.can_ingest(path):
            raise Exception("Oh no!.. Sorry, that seems a little melodramatic... I mean: that didn't work, I'm afraid.")

        quotes = []

        csv_read = pandas.read_csv(path, header = 0)

        for row in csv_read.iterrows():
            quote, author = row
            quotes.append(QuoteModel(quote, author))

        return quotes
