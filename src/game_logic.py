import json
from random import choice
from pathlib import Path

class Board:
    def __init__(self, number_of_rows: int):
        self.number_of_rows = number_of_rows
        self.current_row_num = 0
        self.board = [['' for _ in range(4)] for _ in range(self.number_of_rows)]
        self.code_maker_code = []
        self.colours = Game.getSettingsData("colours")

    def __str__(self):
        return "\n".join([str(row) for row in self.board])

    def clearBoard(self):
        self.current_row_num = 0
        self.board = [['' for _ in range(4)] for _ in range(self.number_of_rows)]

    def refreshColours(self):
        self.colours = Game.getSettingsData("colours")

    def isBoardFull(self):
        return self.current_row_num == self.number_of_rows
    
    def isBoardEmpty(self):
        return self.current_row_num == 0
    
    def getCurrentRow(self):
        try:
            return self.board[self.current_row_num]
        
        except IndexError as e:
            print(f"ERROR IN 'getCurrentRow': {e}\n")

    def getPreviousRow(self):
        try:
            if self.current_row_num > 0:
                return self.board[self.current_row_num - 1]
            
            else:
                print(f"ERROR IN 'getPreviousRow': Can't get previous row when on first row!\n")
        
        except IndexError as e:
            print(f"ERROR IN 'getPreviousRow': {e}\n")
    
    def changeCurrentRow(self, row_values: list):
        try:
            self.board[self.current_row_num] = row_values
            self.current_row_num += 1
        
        except IndexError as e:
            print(f"ERROR IN 'changeCurrentRow': {e}\nFIX: Setting 'self.current_row_num' to 0\n")
            self.current_row_num = 0

    def setRandomCode(self):
        self.code_maker_code = [choice(list(self.colours.keys())) for _ in range(4)]
    
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
    def compareRow(player_colours: list, target_colours: list):
        try:
            p_list = player_colours[0:]
            t_list = target_colours[0:]
            response = []

            for i in range(len(p_list)):
                if p_list[i] == t_list[i]:
                    response.append('b')
                    p_list[i] = t_list[i] = None
        
            for i in range(len(p_list)):
                if p_list[i] is not None and p_list[i] in t_list:
                    response.append('w')
                    t_list[t_list.index(p_list[i])] = None

            # Sorted to keep response vague
            return sorted(response)
        
        except Exception as e:
            print(f"ERROR IN 'compareRow': {e}\n")

class Game:
    def __init__(self):
        pass
    
    @staticmethod
    def initialiseGame():
        Game.setDefaultSettings()

    @staticmethod
    def setDefaultSettings():
        default_colours = {'r': "red",
                           'b': "blue",
                           'y': "yellow",
                           'w': "white",
                           'p': "purple",
                           'o': "orange"}
        
        default_row_num = 10
        
        default_settings =  {"colours": default_colours,
                             "defaultRowQuantity": default_row_num}
        
        data_folder_path = Path("data")
        data_folder_path.mkdir(parents=True, exist_ok=True)

        with open("data/settings.json", "w") as f:
            json.dump(default_settings, f, indent=4)

    @staticmethod
    def getSettingsData(setting: str):
        with open("data/settings.json", "r") as f:
            settings_data = json.load(f)

        return settings_data[setting]