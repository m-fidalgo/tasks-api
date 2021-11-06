class Task():
  def __init__(self, title, description, expiration_date, project):
    self.__title = title
    self.__description = description
    self.__expiration_date = expiration_date
    self.__project = project

  @property
  def title(self):
    return self.__title

  @property
  def description(self):
    return self.__description

  @property
  def expiration_date(self):
    return self.__expiration_date
  
  @property
  def project(self):
    return self.__project

  @title.setter
  def title(self, title):
    self.__title = title

  @description.setter
  def description(self, description):
    self.__description = description

  @expiration_date.setter
  def expiration_date(self, expiration_date):
    self.__expiration_date = expiration_date

  @project.setter
  def project(self, project):
    self.__project = project
