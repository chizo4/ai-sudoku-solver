# ```ai-sudoku-solver-with-cv``` 🧠

### Python implementation of an AI sudoku solver with board generator.

#

<p align="center">
  <b>Preview of the main program being run:</b>
</p>


<p align="center">
  <img src="images/board_ex.png" width="300" alt="The Image of 2048 Game Board."/>
</p>

## About the Implementation

TODO

<b>solver.py:</b>
- contains the <i>SudokuSolver</i> class;
- sudokus are being solved implementing backtracking algorithm;

#

<b>generator.py:</b>
- contains the <i>SudokuGenerator</i> class;
- sudokus are generated with the simple logic of validating row/column/section;

#

<b>main.py:</b>
- the main program to run the application;
- instantiates <i>SudokuGenerator</i> and <i>SudokuSolver</i> classes;
- the main program is run in the command line;

#

## Running the Code

- Before cloning the remote version of the repo and start playing with the code, please make sure that you have ```python3``` and ```pip``` installed on your machine by running the following commands:

```
python3 -V
```

```
pip -V
```

❗ If your shell failed to recognize these commands, please visit [pip](https://pip.pypa.io/en/stable/installation/) and [python](https://www.python.org/downloads/) to find out more about the installation process.

- Otherwise, if you manage to see the versions of ```python3``` and ```pip``` after running the commands, you can clone the whole repo:

```
git clone https://github.com/chizo4/ai-sudoku-solver.git
```

- After cloning it on your machine, please navigate into the root directory of the project and run the bash script to install any needed libraries. Do not worry if you have some of them pre-installed, the script will only install the ones that are missing. Please run the commands:

```
cd ai-sudoku-solver
```

```
bash setup.sh
```

- The next step to follow is to navigate into the ```src``` directory:

```
cd src
```

- Finally, you are able to run the implementation!

- To try out the computer vision version, run the following command. Please note that this approach randomly selects a sample image from the ```assets```. Feel free to try it out with your own sudoku images!

```
python main_cv.py
```

- To try out the command line generator version, run:

```
python main_gen.py
```

#

## Contribution & Collaboration

In case you had an idea on how to improve the project in any way, feel free to contact me via of the links included in my [GitHub bio](https://github.com/chizo4) and then you might contribute to the project by creating a new branch with a Pull Request.
