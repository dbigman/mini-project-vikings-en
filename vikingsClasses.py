import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
    

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return ("Odin Owns You All!")

    def receiveDamage(self, damage):
        """Apply damage to the character's health.

        This method reduces the character's health by the specified damage
        amount. If the character's health remains above zero after taking
        damage, a message indicating the amount of damage received is returned.
        If the health drops to zero or below, a message indicating that the
        character has died in combat is returned.

        Args:
            damage (int): The amount of damage to apply to the character's health.

        Returns:
            str: A message indicating the result of the damage application, either
            showing the damage received or stating that the character has died.
        """

        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        """Process damage received by a Saxon.

        This method updates the health of a Saxon based on the damage received.
        If the health remains above zero after taking damage, it returns a
        message indicating the amount of damage taken. If the health drops to
        zero or below, it returns a message indicating that the Saxon has died
        in combat.

        Args:
            damage (int): The amount of damage to be applied to the Saxon's health.

        Returns:
            str: A message indicating the result of the damage received, either
            showing the damage taken or stating that the Saxon has died.
        """

        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
        
# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        """Simulate a Viking attack on a Saxon.

        This method randomly selects a Saxon and a Viking from their respective
        armies. The Viking attacks the Saxon, dealing damage based on the
        Viking's strength. If the Saxon's health drops to zero or below as a
        result of the attack, the Saxon is removed from the Saxon army.

        Returns:
            str: The result of the damage received by the Saxon.
        """

        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        result = random_saxon.receiveDamage(random_viking.strength)
        
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        return result
        
    
    def saxonAttack(self):
        """Simulate an attack from a random Saxon on a random Viking.

        This method randomly selects a Saxon from the Saxon army and a Viking
        from the Viking army. It then simulates the attack by having the Viking
        receive damage equal to the strength of the Saxon. If the Viking's
        health drops to zero or below as a result of the attack, the Viking is
        removed from the Viking army.

        Returns:
            str: The result of the damage received by the Viking, which may include a
                message indicating
            whether the Viking has been killed.
        """

        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        result = random_viking.receiveDamage(random_saxon.strength)
        
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
        return result
       
    
    
    def showStatus(self):
        """Show the current status of the battle.

        This method checks the sizes of the Saxon and Viking armies to determine
        the outcome of the battle. It returns a message indicating whether the
        Vikings have won, the Saxons have survived, or if the battle is still
        ongoing.

        Returns:
            str: A message describing the current status of the battle.
        """

        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
            
       
    pass


