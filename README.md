# GessGame

A simulated game of Gess, a chess/go variant, coded in Python.  Gess is a two player game and rules can be found [here:](https://www.chessvariants.com/crossover.dir/gess.html)
<p>One player will play as <strong>w</strong> and the opposing player with will play as <strong>b</strong>; <strong>b</strong> goes first.</p>

The Gess board will start and appear as: 
<br>
[![gess-board.png](https://i.postimg.cc/CK3xvMcL/gess-board.png)](https://postimg.cc/WD7VzVRQ)

<p>To make a move, a string of starting coordintates and ending coordinates must be entered.  For example, to move a players piece from e3 to e6: 
  <strong>gess_game.make_move('e3', 'e6')</strong>.</p>
  
<p>A 'piece' is defined as a 3x3 area only containing the current players stones and must move as a unit. If there is a stone in the center of a players piece, it may move any unobstructed distance. If there is no stone in the center of a players piece, it may only move 3 squares. The direction a piece can move is determined by where stones are located on the perimeter of the piece.</p> 

<p>Once a player loses a ring of their own pieces, the game is over.</p>

