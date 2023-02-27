import abc
class Cat(abc.ABC):
  """Represents an abstract of cat.
  Attributes:
    name (str): name of cat.
    hunger (int): hunger level of cat."""
  
  def __init__(self, name):
    """Initialize the name of the cat and set the default value of the hunger level as 5 for cats."""
    self._name = name
    self._hunger = 5
    
  @property
  def name(self):
    """Returns the name of cat."""
    return self._name
    
  @property
  def hunger(self):
    """Returns the hunger level of the cat."""
    return self._hunger
    
  def update_hunger(self, val):
    """Hunger level keeps updated for each interaction with player, it will always remain in range of 1 to 10."""
    self._hunger += val
    if self._hunger > 10:
      self._hunger = 10
    elif self._hunger <= 0:
      self._hunger = 1
      
  def __str__(self):
    """Return string with cat's name, and the level bar represent the status of hunger level of cat."""
    full_bar = ''
    full_level = ['|',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ','|']
    for index in range(self._hunger):
      full_level[index + 1] = ' + '
    for element in full_level:
      full_bar += element
    return self.name + ":\nStarving\t\t\t\tFull\n" + full_bar
      
  @abc.abstractmethod
  def feed(self, player):
    """Feeds the cat."""
    pass
    
  @abc.abstractmethod
  def play(self, player):
    """Play with cat."""
    pass
    
  @abc.abstractmethod
  def pet(self, player):
    """Pet the cat."""
    pass