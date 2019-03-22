import sys
import os
from PIL import Image

class ScaleZip():
    """
    A class used to scale thr zip with image.

    ...

    Methods
    -------
    process(zipprocessor)
        This method change the size of img in zip file.

    Attributes
    ----------
    size : tuple
       The size of scaled img.
    """
    def __init__(self, size):
        """
        Parameters
        ----------
        zipname: str
            The name of zip file.
        size : (str, str)
            The final size of img.
        """
        self.size = size

    def process(self, zipprocessor):
        """
        Process the file with img.
        :param zipprocessor : object
        """
        for filename in os.listdir(zipprocessor.temp_directory):
            try:
                im = Image.open(
                                zipprocessor._full_filename(filename)
                               )
                scaled = im.resize(self.size)
                scaled.save(scaled,
                            zipprocessor._full_filename(filename))
            except IsADirectoryError:
                continue
