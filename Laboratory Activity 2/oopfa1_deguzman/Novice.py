from Character import Character

class Novice(Character):
    def basicAttack(self, character):
        character.reduceHp(self.getDamage())
        print(f"{self.getUsername()} performed Basic Attack! -{self.getDamage()}")

character1 = Novice('Galileon Thirteen - Novice')
print(character1.getUsername())
print(character1.getHp())
"""
From the added argument of 'Character' within the class Novice(), all the other
variable as well as the defined functions within those varaibles were utilized
simply through inheritance by placing the parent class, which is the 'Character'
within Novive(). Now that it was inherited by the sub-Class Novice(), the
sub-Class can now utilize the prior functions without re-defining them again to
create a similar output, which in this case is the output of printing out their
usernames, with the only difference being that the HP is also printed out.
"""