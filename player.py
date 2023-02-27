class Player:
  """Represent the player who will interact with cats.
  Attributes:
    hp (int) : hit point of the player."""
  def __init__(self):
    """Initialize hit point of the player as default value."""
    self._hp = 25
  
  @property
  def hp_property(self):
    """Return the hit point of the player."""
    return self._hp
    
  def take_damage(self, dmg):
    """Player take damages on each interactions with cats, hit point is subtracted when cat harms player, return zero if it becomes negative value."""
    if self._hp - dmg > 0:
      self._hp -= dmg
    else:
      self._hp = 0
    return self._hp
    
  def __str__(self):
    """Return the string infroms player's hit point status."""
    return '\nYou ' + str(self._hp) + ' have hp.'