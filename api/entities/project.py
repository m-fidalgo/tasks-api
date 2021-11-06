class Project():
  def __init__(self, name, description):
    self.__name = name
    self.__description = description

  @property
  def name(self):
    return self.__name

  @property
  def description(self):
    return self.__description

  @name.setter
  def name(self, name):
    self.__name = name

  @description.setter
  def description(self, description):
    self.__description = description
