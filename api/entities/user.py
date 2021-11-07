class User():
  def __init__(self, name, email, password, is_admin):
    self.__name = name
    self.__email = email
    self.__password = password
    self.__is_admin = is_admin

  @property
  def name(self):
    return self.__name
  
  @property
  def email(self):
    return self.__email
  
  @property
  def password(self):
    return self.__password

  @property
  def is_admin(self):
    return self.__is_admin

  @name.setter
  def name(self, name):
    self.__name = name

  @email.setter
  def email(self, email):
    self.__email = email

  @password.setter
  def password(self, password):
    self.__password = password

  @is_admin.setter
  def is_admin(self, is_admin):
    self.__is_admin = is_admin