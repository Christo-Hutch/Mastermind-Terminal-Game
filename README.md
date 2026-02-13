# Mastermind_Terminal_Game
## Brief Description
A simple python game which replicates the well-known board game, Mastermind. This game has many similarities to the more popular online game "Wordle" but instead of using letters in words, Mastermind uses colours and doesn't inform the player of which colours are in correct positions. In it's current state, this game utilises a TUI (Terminal-User-Interface), as I am prioritising the game logic over UI. Since colours are a crucial part of this game, the colorama Python library is required to run this project (essential, external Python libraries are listed in the 'requirements.txt' file). Python was used to create this project due to it's simplistic implementation which is important, since this is just a mini side-project to motivate me, whilst I work on a larger project.

## Technical Description
### Repository Strucuture
```
mastermind-terminal-game
│
├── data/
│   ├── settings.json
│   └── ports/
│
├── src/
│   ├── game_logic.py
│   ├── interface.py
│   └── utils.py
│
├── tests/
│   └── test_logic.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── Main.java
```