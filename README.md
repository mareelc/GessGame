
A simulated game of Gess, a chess/go variant, coded in Python.  Gess is a two player game and rules can be found [here:](https://www.chessvariants.com/crossover.dir/gess.html)
<p>One player will play as <strong>w</strong> and the opposing player with will play as <strong>b</strong>; <strong>b</strong> goes first.</p>

The Gess board will start and appear as: 
<br>
[![gess-board.png](https://i.postimg.cc/CK3xvMcL/gess-board.png)](https://postimg.cc/WD7VzVRQ)

<p>To make a move, a string of starting coordintates and ending coordinates must be entered in console.  For example, to move a players piece from c18 to c16, 
the console will prompt:  
  <ul>"Enter Starting Coordinate: " 
    <ul>type 'c18' and hit enter.</ul></ul>
  <ul>"Enter Ending Coordinate: "
    <ul>type 'c16' and hit enter.</ul></ul>
</p>
<br> 
<img src="https://github.com/heinl11/GessGame/blob/master/gess_move.gif" />
<p>A 'piece' is defined as a 3x3 area only containing the current players stones and must move as a unit. If there is a stone in the center of a players piece, it may move any unobstructed distance. If there is no stone in the center of a players piece, it may only move 3 squares. The direction a piece can move is determined by where stones are located on the perimeter of the piece.</p> 

<p>A 'ring' is defined as a 3x3 area only containing the current players stones, with no stone in the center, but all perimeter stones occupied.</p>
  <p><strong>Once a player loses a ring of their own stones, the game is over.</strong></p>

