# pythologist-test-images

Images for use in unit tests etc.

List available datasets:

```python
from pythologisttestimages import TestImages

print(TestImages().datasets)
```

> ['IrisSpatialFeatures']

get a path pointing to the dataset

```python
path = TestImages().get_path('IrisSpatialFeatures')
print(path)
```
> '/Source/pythologist-test-images/pythologisttestimages/Data/IrisSpatialFeatures/Example'
