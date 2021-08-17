"""A class for ingesting data from `.docx` files.
This is a concrete implementation of the ingestor_interface class.
"""
from typing import List
import docx

from .ingestor_interface import IngestorInterface
from .QuoteModel import QuoteModel




class DocxIngestor(IngestorInterface):
    """A class parsing quotes from .docx formats.
    This class extracts quotes and authors and 
    constructs the Quote object.
    """
    
    allowed_extension = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Checks that file extension is correct and extracts data.
        
        Each parsed Quote object is added into a list and
        returned.
        """
        if not cls.can_ingest(path):
            raise Exception("Oh no!.. Sorry, that seems a little melodramatic... I mean: that didn't work, I'm afraid.")

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
            return quotes

