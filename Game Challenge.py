class GameProfile:
    def __init__(self , username , health_points , coins):
        self.health_protection(health_points)
        self.username = username
        self.__game_points = health_points
        self.__coins= coins
    @property
    def check_coins(self):
        return self.__coins
    def deposit_coins(self , coins):
        if coins >0:
            self.__coins+= coins
            print(f"{coins} deposited successfully")
        else:
            print("Deposit Failed! Invalid amount")
    def spend_coins(self , coins ):
        if coins >  self.__coins:
            print(f"Failed! your coins are {self.__coins}")
        elif coins <= 0:
            print("Error detected!")
        else:
            self.__coins -= coins
            print(f"{coins} spent and remaining coins are {self.__coins} ")
    def health_protection(self , health_points):
        if health_points > 100:
            print("Error! health cannot be greater than 100")
            raise ValueError("Access denied! Hacker kicked out")
        if health_points < 0:
            print("cheat detected! Health must be between 0 and 100!")
            raise ValueError("Access denied! Hacker kicked out")
    def damage_count(self , damage_health):
        if damage_health < 0:
            print("health cannot be in minus")
        else:
         self.__game_points -= damage_health
         if self.__game_points < 0:
          self.__game_points = 0
         print(f"your remaining health is: {self.__game_points}")
        if  self.__game_points <= 0:
            print("Game Over! player has been eliminated")
    
game = GameProfile("Kinza" , 90 , 500)
print(game.username)
game.health_protection(50)
game.damage_count(120)      
print(f" player Total coins:{game.check_coins}")
game.deposit_coins(-200)
game.spend_coins(100)

        