import cat
class Ocelot(cat.Cat):
  """Represent Ocelot."""
  def feed(self, player):
    """Return the string representing the feeding the cat based on their hunger level and updates the hunger level and take damage to player when cats are unsatisfied by if statements."""
    if self.hunger >= 9:
      player.take_damage(2)
      return self.name + " is absolutely stuff and decided to throw the fish at face."
    elif 6 <= self.hunger <= 8:
      self.update_hunger(1)
      return self.name + " isn't so hungry so only nibbles at the food."
    elif 3 <= self.hunger <= 5:
      self.update_hunger(4)
      player.take_damage(2)
      return self.name + " is pretty hungry and accidently bites you as it snatches the steak from your hand."
    elif self.hunger < 3:
      self.update_hunger(8)
      player.take_damage(3)
      return self.name + " is absolutely starving and bites you on the hand for 3 damage as it is upset at having to wait so long for food." + self.name + " finishes the fish you gave it and is finally satisfied."


  def play(self, player):
    """Return the string representing playing status with the cat based on their hunger level and updates the hunger level and take damage to player when cats become hungry using if statements."""
    if self.hunger > 9:
      self.update_hunger(-1)
      return self.name + " is so full, when you throw the ball, it lays there sleepily in the sun."

    elif self.hunger == 9:
      self.update_hunger(-1)
      return self.name + " is incredibly full and purrs happily as they drift off to sleep.."
    
    elif 6 <= self.hunger <= 8:
      self.update_hunger(-3)
      player.take_damage(3)
      return self.name + " jumps and plays with the soccer ball you threw, then accidentally tackles you when it comes running back."

    elif 4 <= self.hunger <= 5:
      self.update_hunger(-2)
      player.take_damage(4)
      return self.name + " sniffs the basketball you have and then decides that you might be delicious.."

    elif 1 <= self.hunger <= 3:
      self.update_hunger(-1)
      player.take_damage(5)
      return self.name + " is starving, they don't want to play right now. " + self.name + " stalks you, chases you down, tackles you, and takes a large chunk out of your arm for 5 damage."



  def pet(self, player):
    """Return the string representing petting status of the cat based on their hunger level and updates the hunger level and take damage to player when cats are unsatisfied with petting using if statements."""
    if self.hunger >= 9:
      self.update_hunger(-1)
      return self.name + " is absolutely full and crawls into your lap for a nap as it allows you to pet it."
    elif 6 <= self.hunger <= 8:
      self.update_hunger(-1)
      return self.name + " purrs in enjoyment while you pet it and rubs up against your leg."
    elif 4 <= self.hunger <= 5:
      self.update_hunger(-2)
      player.take_damage(2)
      return self.name + " is annoyed by your attempts to pet it and swipes your hand away for 2 damage."
    elif self.hunger <= 3:
      self.update_hunger(-1)
      player.take_damage(5)
      return self.name + " is starving and viscously attacks you with its claws for 5 damage as you try to pet it."