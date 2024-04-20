## Get Started With Your Project

### 1. Create a Tic-Tac-Toe Python Game Engine With an AI Player (Overview) 02:20

00:00
Create a Tic-Tac-Toe Python Game Engine With an AI Player.
00:05
When you were young, you may have learned
to play tic-tac-toe, known by some as naughts and crosses.
The game remains fun
and challenging until you get a bit older.
00:14
Then you learn to program
and discover the joy of coding a virtual version
of this two-player game.
As an adult, you may still appreciate the simplicity
of the game by using Python to create an opponent
with artificial intelligence.
00:28
In this course, you’ll build an extensible game engine
with an unbeatable computer player
that uses the minimax algorithm to play tic-tac-toe.
Along the way, you’ll dive into immutable class design,
generic plug-in architecture,
and modern Python code practices and patterns.
00:46
In this course, you’ll learn how
to create a reusable Python library
with the tic-tac-toe game engine, model the domain
of tic-tac-toe following Python code style,
implement artificial players including one based on the
minimax algorithm, and build a text-based console front end
for the game with a human player.
01:07
This is an advanced course touching on a wide range
of Python concepts that you should be comfortable
with in order to complete the course smoothly.
Remember that Real Python has tutorials
and courses on all of these subjects if you feel there are
any areas that you need to work on.
01:21
But one of the best ways to learn something is
to throw yourself into it and learn as you go.
You can always dive deeper into them after this course
if you feel you want to know more on any of these areas,
01:33
the project that you are going to build relies solely on
Python’s standard library and has no external dependencies.
It was recorded using Python 3.12,
but you’ll need at least Python 3.11
or later to take advantage of the latest syntax
and features that are leveraged in this course.
01:51
Lastly, you should know the rules
of the game that you’ll be implementing.
The classic tic-tac-toe is played on a three-by-three grid
of cells or squares, where each player places their mark,
an X or an O, in an empty cell. The first player
to place three of their marks in a row horizontally,
vertically, or diagonally wins the game.
02:11
So now that you know what you need
and what you’ll be building, let’s get started
by taking a look at the finished game in action.

### 2. Demo: Check Out What You'll Make 05:59

00:00
Demo and Project Overview.
By the end of this course, you’ll have a highly reusable
and extensible Python library with an abstract game engine
for tic-tac-toe.
00:12
It will encapsulate the universal game rules
and computer players, including one that never loses due
to bare-bones artificial intelligence support.
In addition, you’ll create a sample console front end
that builds on top of your library
and implements a text-based interactive tic-tac-toe
game running in the terminal.
00:32
On-screen, you can see actual gameplay between two players.
00:43
Generally, you can mix
and choose the players from among a human player,
a dummy computer player making moves at random,
and a smart computer player sticking
to the optimal strategy.
00:54
You can also specify which player should make the first move,
increasing their chances of winning or tying.
01:02
Later on, you’ll be able
to adapt your generic tic-tac-toe library
for different platforms, such
as a windowed desktop environment or a web browser.
01:11
While you’ll only follow instructions on building a console
application in this course, you can find Tkinter
and PyScript front end examples in the course materials.
01:20
These front ends aren’t covered here
because implementing them requires considerable familiarity
with threading, asyncio,
and queues in Python, which is beyond the scope
of this course, but feel free to study
and play around with the sample code on your own.
01:36
The Tkinter front end is a streamlined version
of the same game that’s described in a separate tutorial,
which only serves as a demonstration
of the library in a desktop environment.
01:47
Unlike the original, it doesn’t look as slick,
nor does it allow you to restart the game easily.
However, it adds the option to play against the computer
or another human player if you want to.
02:01
The PyScript front end lets you
or your friends play the game in a web browser,
even when they don’t have Python installed on their
computer, which is a notable benefit.
02:14
If you’re adventurous and know a little bit of PyScript
or JavaScript, then you could extend this front end
by adding the ability to play online
with another human player through the network.
02:26
It’s worth noting that each
of the three front ends demonstrated in this section merely
implement a different presentation layer
for the same Python library,
which provides the underlying game logic and players.
02:37
There’s no unnecessary redundancy
or code duplication across them,
thanks to the clear separation of concerns
and other programming principles
that you practice in this course. The project
that you’re going to build consists
of two high-level components as seen on-screen.
02:54
The first component is an abstract tic-tac-toe Python
library, which is agnostic about the possible ways
of presenting the game to the user in a graphical form.
03:04
Instead, it contains the core logic of the game
and two artificial players.
But the library can’t stand on its own,
so you are also going to create a sample front end
to collect user input from the keyboard
and visualize the game in the console using plain text.
03:19
You’ll start by implementing the low-level details
of the tic-tac-toe library,
and then you’ll use those
to implement a higher-level game front end
in a bottom-up fashion.
03:31
When you finish this course,
the complete file structure resulting will
look as seen on-screen.
The
frontends/
folder is meant to house one
or more concrete game implementations, such
as your text-based console version.
03:45
library/
is the home folder for the game library.
You can think of both top-level folders
as related but separate projects.
Note that the console front end contains the
__main__.py
file, making it a runnable Python package that you’ll be able
to invoke from the command line using the
-m
option.
04:04
Once you’ve completed the project
or downloaded the completed code from the course materials
from the
frontends/
folder, you’ll be able to start the game
with a command seen on-screen.
04:27
Remember that Python must be able
to find the tic-tac-toe library,
which your front end depends on, on the module search path.
The best practice for ensuring this is by creating
and activating a virtual environment
and installing the library with
pip
.
04:42
You’ll find detailed instructions on how
to do this in the README file in the supporting materials.
The tic-tac-toe library is a Python package named
tic_tac_toe
consisting of two subpackages.
04:57
tic_tac_toe.game
is a scaffolding designed to be extended
by the front ends and,
tic_tac_toe.logic
is the building
blocks of the tic-tac-toe game.
05:07
You’ll dive deeper into each of them soon.
The
pyproject.toml
file contains the metadata
necessary for building
and packaging the library to install the downloaded library
or the finished code that you build in this course into
an active virtual environment.
05:25
Try the command seen on-screen.
05:32
During development,
you can make an editable install using
pip
with the
-e
or
--editable
flag to mount the library source code instead
of the built package in your virtual environment.
05:43
This will prevent you from having to repeat the installation
after making changes to the library
to reflect them in your front end.
05:52
In the next part of the course,
you’ll get started on creating the game
by looking at modeling the game domain.

## Model the Tic-Tac-Toe Game Domain

### 1. Model the Game 07:19

00:00
Model the Tic-Tac-Toe Game Domain.
In this step, you’ll identify the parts
that make up the tic-tac-toe game
and implement them using an object-oriented approach.
00:12
By modeling the domain of the game with a mutable object,
you’ll end up with modular
and composable code that’s easier to test, maintain, debug,
and reason about, amongst several other advantages.
00:25
To get started, open the code editor of your choice, such
as Visual Studio Code or PyCharm,
and create a new project called
tic-tac-toe
,
which will also become the name of your project folder.
00:35
Many modern code editors will give you the option
to create a virtual environment
for your project automatically.
So if you want to, you can do that,
but if your editor doesn’t,
then you can make the virtual environment manually.
00:48
On macOS and Linux,
this will create a
tic-tac-toe/
folder and move into it.
00:57
Then it will create a virtual environment in the
venv/
folder
inside
tic-tac-toe/
and activate it.
01:12
If you’re on Windows using Windows Terminal,
then the commands are slightly different.
01:32
Next, scaffold the basic structure of files
and folders in your new project,
remembering to use underscores instead of dashes
for the Python package
in the
src/
subfolder. This skeleton of folders
and files is available in the course materials
if you don’t want to create everything manually. All
of the files in the tree seen on-screen should be empty
at this point. You’ll successively fill them with content
and add more files as you go through the course.
02:01
Start out by editing
pyproject.toml
.
You can enter the minimal packaging configuration seen on-
screen into it.
02:15
You specify the required build tools,
which Python will download
and install if necessary, along
with some metadata for the project.
Adding the
pyproject.toml
file
to the library lets you build
and install it as a Python package into the
active virtual environment.
02:36
Open a terminal with the virtual environment activated
and enter this command
to install the tic-tac-toe library in editable mode.
02:48
Even though there’s no Python code in the library yet,
installing it now
with the
--editable
flag will let the Python interpreter
import the functions
and classes that you’ll be adding shortly
straight from your project.
03:00
Otherwise, every time you made a change in your source code
and wanted to test it, you’d have to remember to build
and install the library into the virtual environment
again. Now you have a general structure for the project,
you can start implementing some code.
03:16
By the end of this step, you’ll have all the essential
pieces of a tic-tac-toe game in place, including the game logic
and state validation, so you’ll be ready
to combine them in an abstract game
engine at the start of the game.
03:29
Each tic-tac-toe player gets assigned one of two symbols,
either cross (X)
or naught (O), which they use
to mark locations on the game board.
Since there are only two symbols belonging to a fixed set
of discrete values, you can define them
with an enumerated type or enum.
03:48
Using enums is preferable over constants due
to their enhanced type safety, common namespace,
and programmatic access to their members.
Create a new Python module called
models
in the
tic_tac_toe.logic
package.
04:04
You’ll use this file
to define tic-tac-toe domain model objects.
Now import the
enum
module from Python’s standard library
and define a new data type in your models.
04:21
The two singleton instances of the
Mark
class,
enum members
CROSS
and
NAUGHT
, represent the player’s symbols.
They’re defined as an extension of
StrEnum
,
which was added to the standard library in Python 3.11.
04:35
Members of
StrEnum
are strings, which means
that you can use them almost anywhere
that a regular string is expected.
Once you assign a given mark to the first player,
the second player must be assigned the only remaining
and unassigned mark.
04:50
Because enums
are glorified classes, you are free to put ordinary methods
and properties into them.
For example, you can define a property of a
Mark
member
that will return the other member.
05:10
The body of the property is a single line of code
that uses a conditional expression
to determine the correct mark.
The quotation marks
around the return type in the property signature are
mandatory to make a forward declaration
and avoid an error due to an unresolved name.
05:25
After all, you claim to return
Mark
,
which hasn’t been fully defined yet.
Alternatively, you can postpone the evaluation
of annotations until after they’ve been defined.
05:43
Adding the special
__future__
import,
which must appear at the beginning of the file,
enables lazy evaluation of type hints.
You’ll use this pattern later
to avoid the circular reference problem
when importing cross-referencing modules.
06:06
You can see a few practical uses
of the
Mark
enum in the REPL session seen on-screen,
06:18
you can refer to a
Mark
by its symbolic name literal,
its string name, or by its value.
You can get the other mark,
06:36
its name, and its value.
You can compare it to a string,
06:52
use it as if it were a string,
and iterate over the available marks.
07:02
You now have a way to represent the available markings
that players will leave on the board to advance the game.
In the next section of the course,
you’ll implement an abstract game board
with well-defined locations for those markings.

### 2. Represent the Square Grid of Cells 06:13

00:00
Represent the Square Grid of Cells.
While some people play variants of tic-tac-toe
with a different number of players
or different sizes of grids, you’ll stick
with the most basic and classic rules.
00:12
You may recall that the classic game’s board is represented
by a three-by-three grid of cells.
Each cell can be empty
or marked with either a cross or a naught.
00:22
Because you represent marks with a single character,
you can implement the grid using a string
of precisely nine characters corresponding to the cells.
A cell can be empty, in which case you’ll fill it
with the space character,
or it can contain the player’s mark.
00:38
In this course, you’ll store the grid in row-major order
by concatenating the rows from top to bottom.
For example, with this representation,
you could express the three gameplays demonstrated
before with a string literal seen on-screen.
00:55
To better visualize them,
you can create the short function in a REPL session.
01:07
The function takes a string of cells as an argument
and prints it out onto the screen in the form
of three separate rows carved out
with the slice operator from the input string
01:21
While using strings to represent the grid
of cells is straightforward,
it falls short in terms of validating its shape and content.
Other than that, plain strings can’t provide some extra grid-
specific properties that you may be interested in.
01:37
For these reasons, you’ll create a new
Grid
data type on top
of a string wrapped in an attribute.
01:53
You define
Grid
as a frozen data class
to make its instances immutable.
So once you create a
Grid
object,
you won’t be able to alter its cells.
02:02
This may sound limiting and wasteful at first
because you’ll be forced to make many instances
of the
Grid
class instead of reusing just one object.
02:10
However, the benefits of immutable objects,
including fault tolerance
and improved code readability,
far outweigh the cost in modern computers. By default,
when you don’t specify any value for the
.cells
attribute,
it will assume a string of exactly nine spaces
to reflect an empty grid.
02:28
However, you can still initialize the grid
with the wrong value for cells,
ultimately crashing the program.
You can prevent this by allowing your objects only
to exist if they’re in a valid state.
02:39
Otherwise, they won’t be created at all, following the fail-
fast and always-valid domain model principles.
Data classes take control of object initialization,
but they also let you run a post-initialization hook
to set derived properties based on
the values of other fields,
for example. You’ll take advantage of this mechanism
to perform cell validation
and potentially discard invalid strings
before instantiating a
Grid
object.
03:24
The
.__post_init__()
method uses a regular expression
to check whether the given value
of the
.cells
attribute is exactly nine characters long
and contains only the expected characters:
"X"
,
"O"
, or
" "
.
03:37
There are other ways to validate strings,
but regular expressions are very compact
and will remain consistent
with the future validation rules you’ll add later on.
03:47
If the
.cells
attribute does not pass the test,
then a
ValueError
is raised.
03:55
Note that the grid is only responsible
for validating the syntactical correctness of a string
of cells, but it doesn’t understand the higher-
level rules of the game.
04:04
You’ll implement the validation
of a particular cell combination’s semantics elsewhere
once you gain additional context.
At this point, you can add a few extra properties
to your
Grid
class, which will become handy when determining
the state of the game.
04:34
These three properties return the current number of crosses,
04:45
naughts,
04:53
and empty cells, respectively.
Because your data class is immutable,
its state will never change,
so you can cache the computed property values with the help
of the
@cached_property
decorator from the
functools
module.
05:06
This will ensure that their code will run at most once no
matter how many times you access the properties,
for example during validation. On-screen,
you can see the
Grid
class in action showing
some of its features.
05:23
You can create an empty
Grid
or one with a particular cell combination.
The grid creation process will check if the grid has too few
cells or the wrong characters.
05:44
You can get the count of Xs, Os,
or empty cells
05:55
using Python code.
You’ve modeled a three-by-three grid of cells,
which can contain a particular combination of player’s marks.
Now it’s time to model the player’s moves so
that artificial intelligence can evaluate
and choose the best option,
and you’ll be doing that in the next video.

### 3. Take a Snapshot of the Player's Move 07:56

00:00
Take a Snapshot of the Player’s Move.
An object representing the player’s
move in tic-tac-toe should primarily answer two questions.
Firstly, the player’s mark: what mark did the player place?
00:14
Secondly, the mark’s location: where was it placed?
However, in order to have the complete picture,
one must also know about the state of the game
before making a move.
00:25
After all, it could be a good
or bad move depending on the current situation.
You may also find it convenient to have the resulting state
of the game at hand so you can assign it a score.
00:36
By simulating that move, you’ll be able to compare it
with other possible moves.
A move object can’t validate itself without knowing some
of the game details, such as the starting player’s mark,
which aren’t available to it.
00:49
You’ll check whether a given move is valid, along
with validating a specific grid cell combination, in a class
responsible for managing the game state.
00:59
Based on these thoughts,
you can add another immutable data class to your models.
01:14
Ignore the two forward declarations of the
GameState
class
for the moment, as you’ll define it
next. Your new class is strictly a data transfer object
whose main purpose is to carry data,
as it doesn’t provide any behavior through methods
or dynamically computed properties.
01:34
Objects of the
Move
class consist
of the mark identifying the player who made a move,
a numeric zero-based indexing of the string of cells,
and the two states before and after making a move.
01:46
The
Move
class will be instantiated, populated with values,
and manipulated by the missing
GameState
class.
Without it, you won’t be able
to correctly create the
Move
objects yourself,
so it’s time to fix that.
02:00
Now, a tic-tac-toe game can be in one of several states,
including three possible outcomes:
the game hasn’t started yet, the game is still going on,
the game is finished in a tie,
the game is finished with player X winning,
and the game is finished
with player O winning. You can determine the current state
of a game of tic-tac-toe based on two parameters:
the combination of the cells in the grid
and the mark of the starting player.
02:31
Without knowing who started the game, you won’t be able
to tell whose turn it is now
and whether the given move is valid.
Ultimately, you can’t properly assess the situation so
that the artificial intelligence can make the right
decision. To fix that,
begin by specifying the
GameState
as another immutable data class consisting of the grid
of cells and the starting player’s
mark.
03:02
By convention, the player who marks the cells
with crosses starts the game, hence the default value
of
Mark("X")
for the starting player’s
mark. However, you can change it according
to your preference by supplying a different
value at runtime.
03:16
Now, add a cached property returning the mark of the player
who should make the next move.
03:31
The current player’s mark will be the same
as the starting player’s mark when the grid is empty
or when both players have marked an equal number of cells.
03:39
In practice, you only need to check the latter condition
because a blank grid implies
that both players have zero marks on the grid.
To determine the other player’s mark, you can take advantage
of the
.other
property in the
Mark
enum.
03:54
Next up, you’ll add some properties
for evaluating the current state of the game.
For example, you can tell that the game hasn’t started yet
when a grid is blank or contains exactly nine empty cells.
04:13
This is where the grid’s properties come in handy.
Conversely, you can conclude
that the game has finished when there’s a clear winner
or there’s a tie.
04:34
The
.winner
property that you’ll implement in a bit will
return a
Mark
instance
or
None
, whereas the
.tie
property will be a Boolean value.
04:43
A tie is where neither player has won,
which means there’s no winner,
and all of the squares are filled,
leaving no empty cells.
05:01
Both the
.game_over
and
.tie
properties rely on the
.winner
property,
which they delegate to.
Finding a winner is slightly more difficult, though. You can,
for example, try to match the current grid
of cells against a predefined collection of winning patterns
with regular expressions.
05:22
There are eight winning patterns: three horizontal lines,
three vertical lines,
05:34
and two diagonal lines.
You define them using templates
resembling regular expressions.
The templates contain question mark (
?
) placeholders
for the concrete player’s
mark.
06:02
You iterate over those templates
and replace the question marks with both players’ marks
to synthesize two regular expressions per pattern, one
containing each player’s mark.
06:16
When the cells match a winning pattern,
then you return the corresponding
mark, the mark of the winner.
Otherwise, you return
None
.
Knowing the winner is one thing,
but you may also want to know the matched winning cells
to differentiate them visually.
06:32
In this case, you can add a similar property.
This will use a list comprehension to return a list
of integer indices of the winning cells.
07:01
Now, you may be concerned about having a bit
of code duplication here between
.winner
and
.winning_cells
, which violates the Don’t Repeat Yourself
(DRY) principle, here.
07:11
That’s okay. The Zen of Python says
that practicality beats purity,
and in this case, extracting the common denominator would
provide little value but make the code much less readable.
07:24
It usually makes sense
to start thinking about refactoring your code when there are
at least three instances of a duplicated code fragment
because then there’s a high chance that you’ll need
to reuse the same piece of code even more.
07:37
GameState
is starting to look pretty good.
It can correctly recognize all possible game states,
but it does lack proper validation, making it prone
to runtime errors.
07:48
In the next video, you’ll rectify that by codifying
and enforcing a few tic-tac-toe rules.

### 4. Introduce a Separate Validation Layer 05:41

00:00
Introduce a Separate Validation Layer. As
with the grid, creating an instance
of the
GameState
class should fail when the supplied
combination of cells and the starting player’s
mark don’t make sense.
00:13
For example, it’s currently possible
to create an invalid game state
that doesn’t reflect genuine gameplay.
You can test this yourself.
Start an interactive Python interpreter session in the
virtual environment where you’d previously installed your
library and run the code seen on-screen.
00:35
Here you initialize a new
GameState
using a grid comprising
a syntactically correct string
with the right characters and length.
But such a cell combination is semantically incorrect
because one player isn’t allowed to fill the entire grid
with their mark. Because validating the game
state is relatively involved,
implementing it in the domain model would violate the single-
responsibility principle and make your code less readable.
01:02
Validation belongs to a separate layer in your architecture,
so you should keep the domain model
and its validation logic in two different Python modules
without mixing their code.
01:15
Go ahead and create two new files in your project:
exceptions.py
and
validators.py
.
You’ll store various helper functions in
validators.py
and a few exception classes in the
exceptions.py
file
to decouple game state validation from the model.
01:33
For improved code consistency,
you can extract the grid validation
that you defined earlier in the
.__post_init__()
method
and move it into the newly created Python module
and wrap it in a new function.
02:03
Note that you replace
self.cells
with
grid.cells
because you’re now referring to a grid instance
through the function’s argument.
02:13
After extracting the grid validation logic,
you should update the corresponding part in the grid model
by delegating the validation to an appropriate abstraction.
02:26
First, you import the new helper function,
02:33
and then you call it in the grid’s
.__post_init__()
hook,
which now uses a higher-level vocabulary
to communicate its intent.
Previously, some low-level details, such as the use
of regular expressions, were leaking into the model,
and it wasn’t immediately clear
what the
.__post_init__()
method does.
02:51
Unfortunately, this change now creates the notorious
circular-reference problem between the model
and validator layers, which mutually depend on each other.
03:01
When you try to import
Grid
,
you’ll get the error seen on-screen.
03:11
This is because Python reads the source
code from top to bottom.
As soon as it encounters an
import
statement, it will jump
to the imported file and start reading it.
03:20
But in this case, the imported
validators
module wants
to import the
models
module,
which hasn’t been fully processed yet.
This is a very common problem in Python when you start
using type hints.
03:33
The only reason you’d need to import
models
is
because of a type hint in your validating function.
You could get away without the import statement
by surrounding the type hint with quotes
to make a forward declaration
as seen earlier on in the course,
but you’ll follow a different idiom this time.
03:50
You can combine the postponed evaluation of annotations
with a special
TYPE_CHECKING
constant.
04:18
You import
Grid
conditionally.
The
TYPE_CHECKING
constant is
False
at runtime,
but third-party tools such
as mypy will pretend it’s
True
when performing static type
checking to allow the import statement to run.
04:31
However, because you no longer import the required type at
runtime, you must now use forward declarations
or take advantage of
from __future__ import annotations
,
which will implicitly turn annotations into string literals.
04:49
Note that the
__future__
import was originally intended
to make the migration from Python 2
to Python 3 more seamless. Today,
you can use it to enable various language features planned
for future releases.
05:01
Once the feature becomes part
of the standard Python distribution
and you don’t need to support older language versions,
you can remove the import.
You can read more about this behavior at the link
to the Python documentation seen on-screen.
05:18
The import statement that previously generated an error
now works correctly.
05:26
With all of this plumbing in place, you are finally ready
to constrain the game state to comply
with the tic-tac-toe rules.
In the next section of the course,
you’ll add a few
GameState
validation functions
to the new
validators
module.

### 5. Discard Incorrect Game States 05:36

00:00
Discard Incorrect Game States.
In order to reject invalid game states,
you’ll implement a familiar post-initialization hook in your
GameState
class that delegates the processing
to another function.
00:35
The validating function,
validate_game_state()
, receives an instance of the game state,
which in turn contains the grid of cells
and the starting player.
00:45
You’ll use this information,
but first you’ll split the validation into a few smaller
and more focused stages by delegating bits
of the state further down in your
validators
module.
01:17
Your new helper function serves as an entry point
to the game state validation
by calling a few subsequent functions
that you’ll define presently.
To prevent instantiating a game state
with an incorrect number of a player’s marks in the grid, such
as the one that you stumbled on earlier on,
you must take the proportion of naughts
to crosses into account.
02:00
At any time,
the number of marks left
by one player must be either the same
or greater by exactly one compared to the number
of marks left by the other player.
02:09
Initially, there are no marks, so the number of Xs
and Os is equal to zero.
When the first player makes a move,
they’ll have one more mark than their opponent,
but as soon as the other player makes their move,
the proportion evens out again, and so on.
02:25
To signal an invalid state,
you raise a custom exception defined in another module.
02:42
It’s customary to have empty classes
extend the built-in
Exception
type in Python without
specifying any methods or attributes in them.
Such classes exist solely for their names,
which convey enough information about the error
that occurred at runtime.
02:56
Notice that you don’t need to use the
pass
statement
or the ellipsis literal (
...
)
as a class body placeholder if you use a docstring,
which can provide additional information.
03:07
Another game state inconsistency related to the number
of marks left on the grid has to do
with the starting player’s mark, which may be wrong.
03:35
The player who left more marks on the grid is guaranteed
to be the starting player.
If not, then you know something must have gone wrong.
Because of the way
Mark
was defined,
you can directly compare the starting player’s
mark to a string literal.
03:58
Finally, there can be only one winner,
and depending on who started the game, the ratio of Xs
and Os left on the grid will be different.
04:28
A starting player has an advantage, so when they win,
they’ll have left more marks than their opponent.
Conversely, the second player is at a disadvantage
so they can only win the game by making an equal number
of moves as the starting player.
05:20
You are almost done with encapsulating the tic-tac-toe game’s
rules in Python code,
but there’s still one more important piece missing.
In the next video, you’ll write code
to systematically produce new game states
by simulating players’ moves.

### 6. Simulate Moves by Producing New Game States 02:43

00:00
Simulate Moves by Producing New Game States.
The last property that you’ll add
to your
GameState
class is a fixed list of possible moves,
which you can find by filling the remaining empty cells in
the grid with the current player’s
mark.
00:27
If the game is not over, you identify the locations
of empty cells using a regular expression,
and then make a move to each of those cells.
Making a move creates a new
Move
object, which you append
to the list without mutating the game state.
00:46
If the game is over, you return an empty list of moves.
This is how you construct a
Move
object.
01:15
A move isn’t allowed if a target cell is already occupied
by either your or your opponent’s mark,
in which case you raise an
InvalidMoveException
.
01:25
On the other hand, if the cell is empty,
then you take a snapshot of the current player’s mark,
the target cell’s index,
and the current game state
while synthesizing the following state.
02:08
Don’t forget to define the new exception type
that you imported.
02:20
And that’s it.
You’ve now got a solid domain model of the tic-tac-toe game,
which you can use to build interactive games
for various front ends.
The model encapsulates the game’s rules
and enforces its constraints.
02:36
In the next section of the course,
you’ll build an abstract game engine
and your first artificial player.

## Scaffold a Generic Tic-Tac-Toe Game Engine

### 1. Scaffold Your Game 06:14

00:00
Scaffold a Generic Tic-Tac-Toe Game Engine.
At this point, you should have all the domain models defined
for your tic-tac-toe library.
Now it’s time to build a game engine
that will take advantage of these model classes.
00:14
To facilitate tic-tac-toe gameplay, go ahead
and create three more Python modules
inside the
tic_tac_toe.game
package
as seen on-screen.
00:26
The
engine
module is the centerpiece of the virtual gameplay,
where you’ll implement the game’s main loop.
You’ll define abstract interfaces that the game engine uses,
along with a sample computer player, in the
players
and
renderers
module.
00:41
By the end of this step, you’ll be set
to write a tangible front end for the tic-tac-toe library.
At the very minimum, to play a tic-tac-toe game, you need
to have two players, something to draw on,
and a set of rules to follow.
00:55
Fortunately, you can express these elements
as immutable data classes, which take advantage
of the existing domain model from your library.
01:05
First, create the
TicTacToe
class in the
engine
module.
01:22
Both
Player
and
Renderer
will be implemented in the
following sections as Python’s abstract base classes.
These only describe the high-level
interface for the game engine.
01:32
They’ll eventually get replaced with concrete classes, some
of which may come from an externally defined front end.
The player will know what move to make,
and the renderer will be responsible
for visualizing the grid. To play the game,
you must decide which player should make the first move,
or you can assume the default one,
which is the player with crosses.
01:53
You should also begin with a blank grid of cells
and an initial game state.
02:41
The engine requests that the renderer update the view
and then uses a pull strategy to advance the game
by asking both players
to make their moves in alternating rounds.
02:51
These steps are repeated in an infinite loop
until the game is over.
GameState
only knows about the current player’s mark,
which can be either X or O,
but it doesn’t know about the specific player objects
that were assigned those marks.
03:05
Therefore, you need to map the current mark
to a player object using this helper method.
03:18
Here you compare enum members
by their identities using Python’s
is
operator.
If the current player’s mark, determined
by the game state, is the same as the mark assigned
to the first player, then that’s the player
who should be making the next move.
03:33
Both players supplied
to the
TicTacToe
object should have opposite marks.
Otherwise, you wouldn’t be able
to play the game without violating the rules,
so it’s reasonable to validate the player’s marks when
instantiating the
TicTacToe
class.
03:59
You add a post-initialization hook to the data class
and call another validation function that you have
to add into your
validators
module.
04:32
You use the identity comparison again
to check both players’ marks
and prevent the game from starting when both players use the
same mark. There’s one more thing
that can go wrong. Because it’s up to the players,
including human players, to decide what move they make,
their choice could be invalid.
04:52
Currently, the
TicTacToe
class catches the
InvalidMove
exception, but it doesn’t do anything useful
with it other than ignore such a move
and ask the player to make a different choice.
05:03
It would probably help to let the front end handle errors
by, for example, showing a suitable message.
05:16
To let the front end decide how
to take care of an invalid move,
you expose a hook in the class
by introducing an optional
.error_handler
callback,
which will receive the exception.
05:26
You define the callback’s type
using a type alias, making its type declaration more concise.
05:40
The
TicTacToe
game will trigger this callback in case
of an invalid move,
as long as you provide the error handler.
05:58
Having implemented an abstract tic-tac-toe game engine,
you can proceed to code an artificial player.
In the next section of the course,
you’ll define a generic player interface
and implement it with a sample computer player
that makes moves at random.

### 2. Let the Computer Pick a Random Move 06:28

00:00
Let the Computer Pick a Random Move.
First, define an abstract player,
which will be the base class for concrete players to extend.
00:26
An abstract class is one that you can’t instantiate
because its objects wouldn’t stand on their own.
Its only purpose is to provide the skeleton
for concrete subclasses. You can mark a class
as abstract in Python by setting its metaclass to
abc.ABCMeta
, or extending the
abc.ABC
ancestor.
00:48
Using the
metaclass
argument instead
of extending the base class is slightly more flexible,
as it doesn’t affect your inheritance hierarchy.
00:56
This is less important in languages like Python,
which support multiple inheritance,
but as a rule of thumb,
you should favor composition over inheritance
wherever possible. The player gets assigned a
Mark
instance
that they’ll be using during the game.
01:12
The player also exposes a public method
to make a move given a certain game
state.
02:10
Notice how the public
.make_move()
method defines a universal
algorithm for making a move,
but the individual step of getting the move is delegated
to an abstract method, which you must implement
in concrete subclasses.
02:23
Such a design is known
as the template method pattern in
object-oriented programming.
02:31
Making a move entails checking if it’s the given player’s
turn and whether the move exists.
The
.get_move()
method returns
None
to indicate
that no more moves are possible,
and the abstract
Player
class uses the walrus operator (
:=
)
to simplify the calling code.
02:46
To make the game feel more natural,
you can introduce a short delay for the computer player
to wait before choosing their move.
Otherwise, the computer would make its move instantly,
unlike a human player. You can define another,
slightly more specific abstract base class
to represent computer players.
03:25
ComputerPlayer
extends
Player
by adding an additional member,
.delay_seconds
,
to its instances, which is equal by default
to 250 milliseconds.
03:44
It also implements the
.get_move()
method
to simulate a certain wait time
and then calls another abstract method
specific to computer players.
04:04
Having an abstract computer player data type enforces a
uniform interface, which you can conveniently satisfy
with a few lines of code.
For example, you can implement a computer player picking
moves at random in the way seen on-screen.
04:46
You use
random.choice()
to pick a random element from a
list of possible moves.
If there are no more moves in the given game state,
then you’ll get an
IndexError
because of an empty list, so you catch it and return
None
instead. You now have two abstract base classes,
Player
and
ComputerPlayer
, as well
as one concrete
RandomComputerPlayer
, which you’ll be able
to use in your games.
05:10
The only remaining element of the equation
before you can put those classes into action is the abstract
renderer, which you’ll define next.
Giving the tic-tac-toe grid a visual form is entirely up
to the front end, so you’ll only define an abstract
interface in your library.
05:48
This could have been implemented as a regular function
because the renderer exposes only a single operation while
getting the whole state through an argument.
05:56
However, concrete subclasses may need
to maintain an additional state such
as the application’s window,
so having a class may come in handy at some point.
06:08
You now have the tic-tac-toe library
with a robust domain model.
An engine encapsulating the game rules, a mechanism
to simulate moves, and even a concrete computer player.
06:20
In the next section of the course,
you’ll combine all the pieces together
and build a game front end, letting you finally see some
action.

## Build a Game Front End for the Console

### 1. Create the Front End 03:42

00:00
Build a Game Front End for the Console.
So far, you’ve been working on an abstract tic-tac-toe game
engine library, which provides
the building blocks for the game.
00:11
In this section, you’ll bring it to life
by coding a separate project that relies on this library.
It’s going to be a bare-bones game running in
the text-based console.
00:22
The most important aspect
of any game front end is providing visual feedback
to the players through a graphical interface.
Because you are constrained to the text-based console
in this example, you’ll take advantage of ANSI escape codes
to control things such as text formatting and placement.
00:40
Create the
renderers
module in your console front end,
and then define a concrete class
that extends the tic-tac-toe’s abstract
Renderer
in it.
01:10
If you’re using Visual Studio Code
and it doesn’t resolve the imports, try quitting
and reopening the editor.
As you can see on-screen, this worked for me,
allowing the imports to be resolved correctly.
01:23
The
ConsoleRenderer
class overrides the only
abstract method responsible
for visualizing the game’s current state.
In this case, you start
by clearing the screen’s content using a helper function,
which you can define below the class.
01:42
The string literal seen on-screen
represents a non-printable escape character,
which starts a special code sequence. The letter
c
that follows encodes the command to clear the screen.
01:55
Note that the
print()
function automatically ends the text
with a newline character.
To avoid adding an unnecessary blank line,
you can disable this
by setting the
end
argument. When there’s a winner,
you’ll want to distinguish their winning marks
with blinking text.
02:11
You can define another helper function
to encode blinking text using the
relevant ANSI escape code.
02:22
Here you wrap the supplied text with opening
and closing ANSI escape codes using an f-string.
To render the tic-tac-toe grid filled with player’s marks,
you’ll format a multiline template string
and use the
textwrap
module to remove the indentation.
02:58
The
print_solid()
function takes a sequence of cells
and prints them with an additional gutter
around the top left corner.
It contains numbered rows and columns indexed by letters.
03:16
The gutter will make it easier for the player
to specify the coordinates of the target cell
where they want to put their mark
03:27
While this basic display would work
okay, improving this would be desirable.
In the next section of the course, you’ll take a look at how
to make a couple of improvements
to make the game more visually appealing when a winner is
declared.

### 2. Make Visual Improvements When the Game Ends 03:18

00:00
Visual Improvements When the Game Ends.
If there’s a winner, you’ll want to blink some
of their cells and print a message stating who won the game.
Otherwise, you’ll print a solid grid of cells
and optionally inform the players
that there were no winners
in the case of a tie.
00:16
The
ConsoleRenderer
class is now modified.
print_solid()
is now removed
and replaced with a conditional.
00:59
Your messages contain special syntax for the name aliases
of Unicode characters, including emojis, in order
to make the output look more colorful and exciting.
01:11
The example seen on-screen will render the
emoji seen on-screen.
Note that you call yet another helper function,
print_blinking()
, which you’ll define next.
01:31
This new function takes the sequence of cells
and the numeric positions
of those which should be rendered using blinking text.
Then it makes a mutable copy of the cells,
overwrites the specified cells with blinking
and ANSI escape codes,
and delegates the rendering to
print_solid()
.
01:56
At this point, you can test your custom renderer using two
computer players built into the tic-tac-toe library.
Save the code seen on-screen in a file named
play.py
,
located in the
frontends/
folder.
02:10
When
02:47
you run this script, you’ll see two artificial players
making random moves leading to different outcomes each time.
03:05
While it’s interesting to look at their gameplay,
there’s no interactivity whatsoever.
You are going to change that in the next section
of the course by letting human players decide what moves
to make.

### 3. Create an Interactive Console Player 03:33

00:00
Create an Interactive Console Player.
At the end of this section, you’ll be able
to play a tic-tac-toe match between a human
and a computer player or two human players,
in addition to the two computer player versions you’ve just
seen. A human player will use the keyboard interface
to specify their moves.
00:18
You can define a new concrete player class in your console
front end, which will implement the abstract
.get_move()
method specified in the library.
00:28
Create the front end’s
players
module
and fill it with the content seen on-screen.
01:04
You keep asking the player for a valid move
until they provide one and make that move.
01:43
Otherwise, the game has finished
and you return
None
to indicate that no moves were possible.
Because the human player types cell coordinates such as
A1
or
C3
, you must convert this text to a numeric index
with the help of the
grid_to_index()
function.
02:16
The function uses regular expressions
to extract the numeric row
and column so that you can calculate the corresponding
index in the flat sequence of cells.
02:28
If it doesn’t find an appropriate combination,
it returns a
ValueError
.
You can now modify your test script
by importing and instantiating
ConsolePlayer
03:06
Running this script will allow you to play
as X against the computer.
Unfortunately, there’s no convenient way
of changing the players or stating who should start the game
because this information is baked into the code.
03:28
Next up, you’ll add a command-line interface to fix that.

### 4. Add a Command-Line Interface 06:09

00:00
Add a Command-Line Interface.
You are almost done building your tic-tac-toe front end.
However, it’s time to add the finishing touches
and turn it into a playable game
by implementing a useful command-line interface using
the
argparse
module.
00:16
That way, you’ll be able to choose the player types
and the starting mark before running the game.
The entry point to your console front end is the special
__main__.py
module, which makes the containing package runnable
through the
python
command.
00:31
Because it’s customary to put minimal wrapper code in it,
you’ll keep the module lightweight
by delegating the processing
to a function imported from another module.
00:46
This makes the code that’s defined in
cli.py
more reusable
across many places and easier to test in isolation.
Here’s how that code might look.
00:59
You import the game engine, your new console renderer,
and a helper function,
parse_args()
, which will be able
to read the command-line arguments
and, based on them, return two-player objects
and the starting player’s mark.
01:28
To implement the passing of arguments,
you can start by defining the available player types
as a Python dictionary, which associates everyday names,
such as
human
, with concrete classes
extending the abstract
Player
.
01:57
This will make it more straightforward
to add more player types in the future.
Next, you can write a function
that will use the
argparse
module
to get the expected arguments from the command line.
03:27
This code translates
to the three optional arguments seen on screen, all
of which have default values.
At this point, the function parses those arguments
and stores their values
as strings in a special
NameSpace
object under the
attributes named
.player_x
,
.player_o
,
and
.starting_mark
, respectively.
03:47
But the function is expected to return a tuple consisting
of custom data types instead of strings.
To make the function’s body comply with its signature,
you can map strings
provided by the user to the respective classes
using your dictionary.
04:09
You translate the user-supplied names
to concrete player classes.
If the starting player’s mark is different from the default
one, then you swap the two players
before returning them from the function.
04:28
To make the code slightly cleaner
and more expressive, you may replace the generic tuple
with a typed named tuple.
04:49
First, you define a
typing.NamedTuple
subclass comprising precisely three named
and typed elements.
You then return an instance of your
NamedTuple
instead
of a generic tuple.
05:05
Doing so gives you additional type safety
and access to the tuple’s elements by name, as well as
by index.
05:29
To play against another human,
you can run your console front end with these arguments.
05:43
If you’d like to try your chances against the computer,
then replace the value of either the
-X
or
-O
option with
random
,
which is currently the only computer player type available.
05:53
Unfortunately, it isn’t particularly challenging
to play against a computer making moves at random.
So in the next chapter of the course,
you’ll implement a more advanced computer player leveraging
the minimax algorithm, making it practically undefeatable.

## Equip the Computer With Artificial Intelligence

### 1. Create Your AI Player 07:39

00:00
Equip the Computer With Artificial Intelligence.
This chapter of the course will involve creating another
computer player, one equipped
with basic artificial intelligence.
00:11
Specifically, it will use the minimax algorithm under the
surface to make the most optimal move in every possible
situation in any turn-based zero-sum game,
such as tic-tac-toe.
00:23
Mastering the details
of the minimax algorithm isn’t your focus in this course,
but if you’d like to learn more about it,
then check out this course which uses a more
straightforward game of nim.
00:33
As an example, before implementing the algorithm, you have
to invent a way of assessing the game score,
which will become the deciding factor
behind choosing the best move.
00:45
You’ll do that by introducing an absolute scale
of numeric values indicating
how well both players are doing.
00:53
For simplicity, you’ll consider static
evaluation of a finished game.
There are three possible outcomes
of the game, which you can assign arbitrary numeric values
to, as seen on-screen.
01:04
The protagonist player whose score you’ll evaluate is known
as the maximizing player
because they try to maximize the game’s overall score.
Therefore, greater value should correspond
to better outcomes as viewed from their perspective.
01:18
The minimizing player, on the other hand, is their opponent
who tries to lower the score as much as possible.
After all, when they win, your player loses.
01:27
While a tie can be equally good
or bad for both players, once you determine the maximizing
and minimizing players, the scale remains absolute, meaning
you don’t need to flip the sign when evaluating
your opponent’s moves.
01:42
You can express this numeric scale in Python
by adding the method seen on-screen
to your
GameState
model in the tic-tac-toe library.
02:22
Because this is a static evaluation,
you can only determine the score when the game is over.
Otherwise, you raise an
UnknownGameScore
exception,
which you must add to the
exceptions
module in the library.
02:48
Knowing the score of a finished game isn’t
that helpful when you want
to make an informed decision about choosing a move up front,
but it’s the first step towards finding the best possible
sequence of moves leading up to winning—
or tying the game, in the worst-case scenario.
03:04
Next, you’ll use the minimax algorithm
to calculate the score
in any game state. When you have several moves
to choose from, you want to pick one
that will increase your expected score.
03:16
At the same time, you want to avoid moves
that could potentially shift the score in
favor of your opponent.
The minimax algorithm can help with that by using the
min()
and
max()
functions
to minimize your opponent’s maximum gain while maximizing
your minimum payoff.
03:32
If that sounds complicated,
then have a look at the graphical visualization
of tic-tac-toe gameplay seen on-screen.
When you imagine all possible game states as a game tree,
choosing the best move boils down to searching
for the most optimal path in such a weighted graph.
03:49
Starting from the current node,
the Minimax algorithm propagates the scores evaluated
statically for the leaf nodes, which correspond
to finished games, by bubbling them up in the game tree.
04:01
Either the minimum
or the maximum score gets propagated at each step,
depending on whose turn it is.
The minimax algorithm starts
by recursively exploring the tree to look ahead
and find all the possible game outcomes.
04:15
Once those are found, it computes their scores
and backtracks to the starting node.
If it’s the maximizing player’s turn that leads
to the next position, then the algorithm picks the
maximum score at that level.
04:27
Otherwise, it picks the minimum score,
assuming the opponent will never make mistakes.
In the game on-screen,
the leftmost branch results in an immediate win
for the maximizing player,
so the connecting edge has the highest weight.
04:42
Choosing the middle branch could also lead to a victory,
but the minimax algorithm pessimistically indicates the
worst-case scenario, which is a tie.
Finally, the branch on the right almost certainly
represents a losing move.
04:58
Create a new
minimax
module in the tic-tac-toe library
and implement the algorithm using the Python
expression seen on-screen.
05:14
The
minimax()
function returns the score associated
with the move passed as an argument
for the indicated maximizing player.
05:24
If the game has finished, then you calculate the score
by performing the static evaluation of the grid.
05:35
Otherwise, you choose either the maximum
or the minimum score, which you’ll find with recursion
for all possible moves at the current position.
05:55
The placement of the
minimax
module in the project’s
directory tree is somewhat subjective
because it would work equally well when defined elsewhere.
06:03
However, you could argue that it logically belongs
to the game’s logic layer since it only depends
on the domain model.
06:11
As long as you made an editable install
of the tic-tac-toe library in your virtual environment,
you’ll be able to test your new function straight away
in a REPL session.
07:12
The computed scores correspond
to the edge weights in the game you saw previously.
Finding the best move is only a matter of choosing the one
with the highest resulting score.
07:22
Note that there can sometimes be multiple alternative paths
to a winning outcome in the game tree.
07:29
In the next section, you’ll create another concrete computer
player which will leverage the minimax algorithm,
and then you’ll use it in your console front end.

### 2. Make Your Minimax Player Unbeatable 05:45

00:00
Make an Undefeatable Minimax Computer Player.
The minimax algorithm calculates the score associated
with a particular move.
To find the best move in a given game state,
you can sort all possible moves by score
and take the one with the highest value.
00:17
By doing that, you’ll use AI
to create an unbeatable tic-tac-toe player with Python.
Go ahead and define the function seen on-screen in the
tic-tac-toe library’s
minimax
module.
00:45
The
find_best_move()
function takes a game state
and returns either the best move for the current player
or
None
to indicate that no more moves are possible.
00:57
Note the use of a partial function to freeze the value
of the
maximizer
argument,
which doesn’t change across
minimax()
invocations.
01:06
This lets you use the
bound_minimax()
function,
which expects exactly one argument, as the ordering key
Python’s
functools.partial()
is a factory that produces a new function
with fewer parameters by pre-populating one
or more of the original function’s arguments
with concrete values.
01:25
Unlike manually defining such a wrapper function
when writing code, the factory can do this dynamically at
runtime and offers a much more concise syntax.
01:36
Next, add a new computer player in the tic-tac-toe
library’s
players
module.
This player will use the
find_best_move()
helper function
that you just created.
02:12
This computer player will always try to find the best move.
However, to make the game less predictable
and reduce the amount of computation, you can let it pick the
first move randomly
before running the expensive minimax algorithm.
02:25
You’ve already implemented the logic
for choosing a random move in
RandomComputerPlayer
.
So now it would help to extract
that common logic into a reusable component.
02:36
Go ahead and modify the code of both the random
and minimax computer players.
03:11
You call the
.make_random_move()
method on the game state
in both classes. You need to define this new method
to choose one of the possible moves using
Python’s
random
module.
03:23
Head over to the
models
module
and define the
.get_random_move()
method in the
GameState
class as seen.
First, import the
random
module
and then create the method within the class body.
04:03
The final step is
to use the new computer player in your front end.
Open the
args
module in the console front end project.
04:22
First, the imports are tidied up
and
MinimaxComputerPlayer
is imported.
04:33
You add the new player type to the mappings of names,
and finally use the
MinimaxComputerPlayer
as the default opponent of the human player.
04:48
You now have three kinds of players to choose from.
You can take your console front end
for the ultimate test drive by selecting different players
to try their chances against each other.
04:59
For example, you can pick two minimax computer players.
05:12
In this case, you should expect the game
to always end in a tie
since both players use the optimal strategy.
One thing you may notice when requesting at least one
MinimaxComputerPlayer
is poor performance,
especially at the beginning of the game.
05:27
That’s because building the entire game tree, even
for a game as relatively basic as tic-tac-toe, is costly.
So in the future, you may want
to check out a few performance optimization possibilities on
your own, but next you’ll take a look back at
what you’ve learned in this course.

### 3. Create a Tic-Tac-Toe Python Game Engine With an AI Player (Summary) 01:08

00:00
Well done.
You’ve made it to the end of this course.
You’ve built a front-end agnostic tic-tac-toe library
with the game’s core logic
and two artificial computer players,
including an unbeatable one leveraging
the minimax algorithm.
00:14
You also created a sample front end
that renders the game in the text-based console
and takes input from a human player.
Along the way, you followed good programming practices,
including object-oriented design with elements
of the functional paradigm,
and took advantage of the latest enhancements in Python.
00:33
In this course, you’ve learned how
to create a reusable Python library
with the tic-tac-toe game engine; model the domain
of tic-tac-toe following a Python code style;
implement artificial players, including one based on the
minimax algorithm; and build a text-based console front end
for the game with a human player.
00:54
If you haven’t already done so,
make sure you download the course materials so
that you can experiment with the alternative front ends.
01:02
We hope you found this course useful,
and we’ll see you again soon at realpython.com.

