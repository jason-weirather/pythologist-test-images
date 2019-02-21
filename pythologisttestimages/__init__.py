import os
class TestImages(object):
    def __init__(self):
        self.base = os.path.abspath(os.path.join(__file__,'../../data'))
        return
    @property
    def raw(self):
        return {
            'IrisSpatialFeatures':os.path.join(self.base,'IrisSpatialFeatures','Example'),
            'Small':os.path.join(self.base,'Small','Example'),
            'Tiny':os.path.join(self.base,'Tiny','Example'),
        }
    @property
    def pythologist(self):
        d = {
            'IrisSpatialFeatures':
                    os.path.join(self.base,'IrisSpatialFeatures','pythologist-tumor-margin.h5'),
            'Small':os.path.join(self.base,'Small','pythologist.h5'),
            'Tiny':os.path.join(self.base,'Tiny','pythologist_tiny.h5')
        }
        return d
