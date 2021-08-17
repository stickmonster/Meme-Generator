"""A Class interface for the Ingestor strategy object.

This is an Abstract Base Class from which document type specific Ingestors
shall be realised.
`allowed_extension` monitors file extensions to allow ingestion.
The `parse` method is passed as an abstractmethod to these ingestors.
"""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface:
    """An abstract Interface class of the strategy object ingesting file types.
    
    This interface structures the approach of downstream ingestors.
    `can_ingest` class method is boolean.
    `parse` class method is passed to concrete implementation.
    """
    allowed_extension = []

    @classmethod
    def can_ingest(cls, path):
        """Checks whether input data file is of the correct type.
        
        Concrete ingestors use this method to check
        if file type if an `allowed_extension`.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extension

    @classmethod
    @abstractmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Parse Quote from input data file.
        
        An abstract method to be realised by concrete ingestors.
        """
        pass
