class User():
  def __init__(self, name, email, password):
    self.__name = name
    self.__email = email
    self.__password = password

  @property
  def name(self):
    return self.__name
  
  @property
  def email(self):
    return self.__email
  
  @property
  def password(self):
    return self.__password

  @name.setter
  def name(self, name):
    self.__name = name

  @email.setter
  def email(self, email):
    self.__email = email

  @password.setter
  def password(self, password):
    self.__password = password