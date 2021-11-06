class Task():
  def __init__(self, title, description, expiration_date):
    self.__title = title
    self.__description = description
    self.__expiration_date = expiration_date

  @property
  def title(self):
    return self.__title

  @property
  def description(self):
    return self.__description

  @property
  def expiration_date(self):
    return self.__expiration_date

  @title.setter
  def title(self, title):
    self.__title = title

  @description.setter
  def description(self, description):
    self.__description = description

  @expiration_date.setter
  def expiration_date(self, expiration_date):
    self.__expiration_date = expiration_date
