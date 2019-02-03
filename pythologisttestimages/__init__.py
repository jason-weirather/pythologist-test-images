import os
import pythologisttestimages
from tempfile import TemporaryDirectory
class TestImages(object):
    def __init__(self):
        path = os.path.dirname(pythologisttestimages.__file__)
        self._datadir = os.path.join(path,'Data')
        return
    @property
    def datasets(self):
        dirs = []
        for file in os.listdir(self._datadir):
            if not os.path.isdir(os.path.join(self._datadir,file)): 
                raise ValueError("must be directories in data "+str(file))
            dirs.append(file)
        return dirs
    def get_path(self,dataset):
        return os.path.join(self._datadir,dataset,'Example')
