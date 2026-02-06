class Board:
    def __init__(self, numberOfRows: int):
        self.numberOfRows = numberOfRows
        self.currentRowNum = 0
        self.board = [['' for _ in range(4)] for _ in range(self.numberOfRows)]
    
    def __str__(self):
        return "\n".join([str(row) for row in self.board])
    
    def getCurrentRow(self):
        try:
            return self.board[self.currentRowNum]
        
        except IndexError as e:
            print(f"ERROR IN 'getCurrentRow': {e}\n")

    def getPreviousRow(self):
        try:
            if self.currentRow > 0:
                return self.board[self.currentRowNum - 1]
            
            else:
                print(f"ERROR IN 'getPreviousRow': Can't get previous row when on first row!\n")
        
        except IndexError as e:
            print(f"ERROR IN 'getPreviousRow': {e}\n")

    def clearBoard(self):
        self.currentRowNum = 0
        self.board = [['' for _ in range(4)] for _ in range(self.numberOfRows)]

    def isBoardFull(self):
        return self.currentRowNum == self.numberOfRows
    
    def isBoardEmpty(self):
        return self.currentRowNum == 0
    
    def changeCurrentRow(self, rowValues: list):
        try:
            self.board[self.currentRowNum] = rowValues
            self.currentRowNum += 1
        
        except IndexError as e:
            print(f"ERROR IN 'changeCurrentRow': {e}\nFIX: Setting 'self.currentRowNum' to 0\n")
            self.currentRowNum = 0
    
    """
    This static method takes two lists: the player's submitted colours and
    the target colours (code maker's secret colours). If one of the player's
    colours are correct in colour and place, a black pin (represented by the
    letter 'b') is added to the response. If one of the player's colours are
    correct but in the correct place, a white pin (represented by the letter
    'w') is added to the response. If a player has included a colour not
    present, nothing (represented by None) is added to the response.
    """
    @staticmethod
    def compareRow(playerColours: list, targetColours: list):
        try:
            p = playerColours[0:]
            t = targetColours[0:]
            response = []

            for i in range(len(p)):
                if p[i] == t[i]:
                    response.append('b')
                    p[i] = t[i] = None
        
            for i in range(len(p)):
                if p[i] is not None and p[i] in t:
                    response.append('w')
                    t[t.index(p[i])] = None

            # Sorted to keep response vague
            return sorted(response)
        
        except Exception as e:
            print(f"ERROR IN 'compareRow': {e}\n")


class Player:
    def __init__(self):
        pass


class Round:
    def __init__(self):
        pass


class Game:
    def __init__(self):
        pass