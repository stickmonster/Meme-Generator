"""A class abstracting the file-type ingestor classes.

This is a class that conjoins different ingestors. 
"""
from typing import List
from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor
from .ingestor_interface import IngestorInterface

class Ingestor(IngestorInterface):
    """A simplification of underlying ingestor helper classes.
    
    Checks the extension of the input and chooses the ingestor class to use.
    """

    ingestors= [CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Extraction and processing of data based on file extension.
        
        Input data file checked for type and assigned ingestor.
        """
        for ingestor in cls.ingestors:
  #          print(path)
  #          print(ingestor)
            if ingestor.can_ingest(path):
  #              print("yes")
  #              print(ingestor)
  #              print(path)
                return ingestor.parse(path)



