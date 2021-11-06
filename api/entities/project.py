class Project():
  def __init__(self, name, description, functionaries):
    self.__name = name
    self.__description = description
    self.__functionaries = functionaries

  @property
  def name(self):
    return self.__name

  @property
  def description(self):
    return self.__description

  @property
  def functionaries(self):
    return self.__functionaries

  @name.setter
  def name(self, name):
    self.__name = name

  @description.setter
  def description(self, description):
    self.__description = description

  @functionaries.setter
  def functionaries(self, functionaries):
    self.__functionaries = functionaries
