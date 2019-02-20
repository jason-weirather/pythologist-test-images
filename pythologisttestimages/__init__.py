import os
from pythologistreader.formats.inform.custom import CellProjectInFormLineArea
from pythologistreader.formats.inform.sets import CellProjectInForm
class TestImages(object):
    def __init__(self):
        self.base = os.path.abspath(os.path.join(__file__,'../../data'))
        return
    @property
    def paths(self):
        return {
            'IrisSpatialFeatures':os.path.join(self.base,'IrisSpatialFeatures','Example'),
            'Small':os.path.join(self.base,'Small','Example'),
            'Tiny':os.path.join(self.base,'Tiny','Example'),
        }
    def pythologist(self,key):
        d = {
            'IrisSpatialFeatures':
                    os.path.join(self.base,'IrisSpatialFeatures','pythologist-tumor-margin.h5'),
            'Small':os.path.join(self.base,'Small','pythologist.h5'),
            'Tiny':os.path.join(self.base,'Tiny','pythologist_tiny.h5')
        }
        if key not in d: raise ValueError("Must pick a key in "+str([x for x in d.keys()])) 
        if key == 'IrisSpatialFeatures':
            return CellProjectInFormLineArea(d[key],mode='r')
        else:
            return CellProjectInForm(d[key],mode='r')