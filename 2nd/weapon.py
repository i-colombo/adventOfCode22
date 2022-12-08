from expectedResultType import ExpectedResultType

class Weapon():
    @classmethod
    def fromStrategy(cls, strategyValue):
        if Rock.allowsStrategy(strategyValue):
            return Rock()
        elif Paper.allowsStrategy(strategyValue):
            return Paper()
        else:
            return Scissor()
    
    def getScore(self):
        pass

    def getWeaponToWin(self):
        pass

    def getWeaponToDraw(self):
        pass

    def getWeaponToLose(self):
        pass
    
    def fight(self):
        return self.getScore()

    def win(self):
        return 6
    
    def draw(self):
        return 3
    
    def lose(self):
        return 0
    
    def getWeaponTo(self, expectedResult):
        if expectedResult == ExpectedResultType.WIN:
            return self.getWeaponToWin()
        elif expectedResult == ExpectedResultType.DRAW:
            return self.getWeaponToDraw()
        else:
            return self.getWeaponToLose()

class Rock(Weapon):
    @classmethod
    def allowsStrategy(cls, strategyValue):
        return strategyValue in ["A", "X"]
    
    def getScore(self):
        return 1
    
    def fight(self, weapon):
        return super().fight() + weapon.getFightResultForRock(self)
    
    def getFightResultForRock(self, rock):
        return rock.draw()
    
    def getFightResultForPaper(self, paper):
        return paper.win()
    
    def getFightResultForScissor(self, scissor):
        return scissor.lose()

    def getWeaponToWin(self):
        return Scissor()

    def getWeaponToDraw(self):
        return Rock()

    def getWeaponToLose(self):
        return Paper()

class Paper(Weapon):
    @classmethod
    def allowsStrategy(cls, strategyValue):
        return strategyValue in ["B", "Y"]
    
    def getScore(self):
        return 2
    
    def fight(self, weapon):
        return super().fight() +  weapon.getFightResultForPaper(self)

    def getFightResultForRock(self, rock):
        return rock.lose()
    
    def getFightResultForPaper(self, paper):
        return paper.draw()
    
    def getFightResultForScissor(self, scissor):
        return scissor.win()

    def getWeaponToWin(self):
        return Rock()

    def getWeaponToDraw(self):
        return Paper()

    def getWeaponToLose(self):
        return Scissor()

class Scissor(Weapon):
    @classmethod
    def allowsStrategy(cls, strategyValue):
        return strategyValue in ["C", "Z"]
    
    def getScore(self):
        return 3

    def fight(self, weapon):
        return super().fight() + weapon.getFightResultForScissor(self)

    def getFightResultForRock(self, rock):
        return rock.win()
    
    def getFightResultForPaper(self, paper):
        return paper.lose()
    
    def getFightResultForScissor(self, scissor):
        return scissor.draw()
    
    def getWeaponToWin(self):
        return Paper()

    def getWeaponToDraw(self):
        return Scissor()

    def getWeaponToLose(self):
        return Rock()
