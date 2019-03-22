import os
import shutil
import zipfile
from pathlib import Path


class ZipProcessor:
    '''
    A class used to process Zip files.

    ...

    Methods
    -------
    process_zip()
        Process zip files.

    unzip_files()
        Unzips files.

    zip_files()
        Archives files to zip format.

    Attributes
    ----------
    zipname : str
        The name of zip file.

    processor : object
        The process we want to do.
    """
    '''
    def __init__(self, zipname, processor):
        '''
        Parameters
        ----------
        zipname : str
            The name of the file.
        '''
        self.zipname = zipname
        self.temp_directory = "unzipped-{}".format(zipname[:-4])
        self.processor = processor

    def _full_filename(self, filename):
        """
        returns full path to the file

        :argument filename : str
        """
        return os.path.join(self.temp_directory, filename)

    def process_zip(self):
        """
        Process zip files.
        """
        self.unzip_files()
        self.processor.process()
        self.zip_files()

    def unzip_files(self):
        """
        Unzips files.
        """
        os.mkdir(self.temp_directory)
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(self.temp_directory)

    def zip_files(self):
        """
        Makes zip archives of files.
        """
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in os.listdir(self.temp_directory):
                file.write(self._full_filename(filename), filename)
        shutil.rmtree(str(self.temp_directory))
