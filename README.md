## **Project #2: Human vs. Bot Game**
**Goal:** Create a two-player game (a user against a computer) in which the user interacts with the console *or* with a Turtle window. The computer can either play/make moves at random or incorporate some sort of strategy.

### **Step 1: Choose a game.**

Some suggestions looked into:
* [Tic Tac Toe](https://en.wikipedia.org/wiki/Tic-tac-toe)
* [Dot and Boxes](https://en.wikipedia.org/wiki/Dots_and_Boxes)
* [Battleship](https://en.wikipedia.org/wiki/Battleship_(game))
* [Farkle](https://en.wikipedia.org/wiki/Farkle)
* [Math problem solving game](https://docs.google.com/document/d/1vEsXHTvMq4tSr3h6YQWwYdRdJD8EJseD_WfN2knJjh4/edit?usp=sharing)

### **Step 2: Plan the game.**

My game is a simple version of the classic game Snakes and Ladders where a human player competes against a computer-controlled opponent. At the start of the game, both the player and the computer are at the starting point. The game is turn-based, with the human player and computer alternately rolling a die (simulated by generating a random number from 1 to 6) to determine how many squares they can advance. The excitement and unpredictability of the game come mainly from the snakes and ladders. If any player, human or computer, lands on a square with the bottom of a ladder, they move up to a higher square where the ladder ends. On the other hand, if they land on a square with a snake's head, they slide back down to a lower square, which marks the snake's tail. The winner is the first player to arrive precisely at the 100th square. However, the catch is that landing exactly on the 100th square is a must; overshooting due to a larger dice roll leads to a turn being forfeited. The game is primarily built using Python’s turtle module for graphics and the random module to simulate dice rolls. 

Answered the following questions.

1. How does my game work?
2. How long do I think it will take to write all the code for this game?
3. What do I think will be the most challenging part of creating this game?
4. If I happen to finish early, what other features could I try to add to the game to make it better?

### **Step 3: Begin coding the game.**

Wanted to ensure that my program has line comments to explain my thinking and that the code includes ALL of the following. Wanted to showcase my skills by making the code readable, concise, and functioning. 

* `print()`
* `input()`
* `if`
* `def`
* a global variable
* a loop
* a list or a tuple
* a method involving a list, string, or some other object

Whenever you use `def` to make a custom function, be sure to document it using a docstring.

### **Step 4: Test the game.**

Asked these prompts to peers to get feedback on the overall playability and user interface of the game. 

* What parts of the program/game were done well?
* What parts of the program/game could use improvement?
* What do you wish the program/game included?

Will modify code based on their feedback.
