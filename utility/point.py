class Point:
  '''A point in a 2D space'''

  def __init__(self, x: int, y: int):
    self._x = x
    self._y = y

  @property
  def x(self):
    return self._x
  
  @property
  def y(self):
    return self._y