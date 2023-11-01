from enum import Enum
from numpy import double

class GeographicalFeatureType(Enum):
  """Enum describing the type of geographical feature"""

  WOODS = 0
  DESERT = 1
  MOUNTAIN = 2
  RIVER = 3
  CITY = 4


class GeographicalFeature:
  """Describes a geographical feature with a name a color for plotting"""

  def __init__(
    self,
    type: GeographicalFeatureType,
    name: str,
    color: str,
    ease_of_living: double = 0.5,
  ):
    self._color = color
    self._name = name
    self._type = type
    self._ease_of_living = ease_of_living

  @property
  def color(self):
    return self._color

  @property
  def name(self):
    return self._name

  @property
  def type(self):
    return self._type

  @property
  def ease_of_living(self):
    return self._ease_of_living
  
class GeographicalMapSettings:
  def __init__(self, features: list[GeographicalFeature], size: int = 1000, title: str = 'Geographical map', show_legend: bool = True):
    self._features = features
    self._size = size
    self._title = title
    self._show_legend = show_legend

  @property
  def features(self):
    return self._features
  
  @property
  def size(self):
    return self._size
  
  @property
  def title(self):
    return self._title
