"""A class that constructs a quote object.

This class extracts quote data from types of input files.
"""

class QuoteModel:
    """A class container that constructs a QuoteModel.
    
    This class will be realised by ingestors and will then
    construct quote objects.
    """

    def __init__(self, author, body):
        """Initialises quote object.
        
        This object uses `body` and `author` information
        to create a quote object.
        """
        self.author = author
        self.body = body

    def __repr__(self):
        """Object represented as a string format."""
        return f'{self.body} says {self.author}'

