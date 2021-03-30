# CPSC 223p
##  Python Virtual Environments

This is an exercise to ensure you have the required software available to work with virtual environments and our selected plotting library [matplotlib](https://matplotlib.org/).

A program named matplotlib_demo.py is provided along with a `requirements.txt` file.

Create a virtual environment given the requirements and verify that the program executes without errors or warnings.

Finally make a small change to the given program (detailed below) and commit your changes back to your repository.

## Virtual Environments
In Python v.2, virtualenv is the preferred tool for creating virtual environments. Since Python v.3.3, the standard library module [venv](https://docs.python.org/3/library/venv.html#module-venv) is the preferred way to create virtual environments.

A summary of how to use virtual environments is given in [Installing packages using pip and virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments).

Should you wish to use `virtualenv` for Python3 then you must install additional software. On Debian-based systems such as Ubuntu and Raspbian, the software can be installed with the command `sudo apt install python3-virtualenv`. If in doubt, please speak with your instructor to ensure you have the appropriate software installed.

On some systems, the Python v.3 standard library module venv needs additional software installed to operate correctly .On Debian-based systems such as Ubuntu and Raspbian, the software can be installed with the command `sudo apt install python3-venv`. If in doubt, please speak with your instructor to ensure you have the appropriate software installed.

The two options are interoperable with each other and effectively have no difference for the purposes of these exercises.

On most systems the command `python` maps to Python v.2 and the command `python3` maps to Python v.3. These instructions assume that you are using Python v.3 and the command `python3` maps to Python v.3. If it is not, then please use the appropriate command. (In many cases, the command `python` maps to Python v.3 as well.)

Do not add your virtual environment directory to your git repository. The `.gitignore` file already excludes common virtual environment directory names. Please do not force the virtual environment into your repository. Always commit and maintain the `requirements.txt` file so that you and others can recreate the virtual environment.

### Creating a Virtual Environment
Create a virtual environment using the command `python3 -m venv env`.

Activate the virtual environment with the command `source env/bin/activate`. This assumes that the directory `env` is in the current working directory when you issue the command.

Activating the virtual environment will change your prompt to include the string `(env)`.

To deactivate or exit the virtual environment, use the command `deactivate`. You will see your prompt return to what it was prior to having the string `(env)` added to it.

### Installing the Requirements
After creating the virtual environment and activating, install the required software with the command `pip install -r requirements.txt`. Remember, you must be in the same directory as the virtual environment and the `requirements.txt` file.

If you see a warning that there is a newer version of pip available, you can safely ignore this warning for this exercise.


## Instructions
Edit `matplotlib_demo.py`and make the following changes:
* Add a header to the file
* Correct the file for any stylistic problems using `pylint` and `pycodestyle`
* Change the color of the line in the function `simple_plot`
* Output the plots created in `fill_between_demo` to files named `a.pdf`, `b.pdf`, and `c.pdf`
* Do not open any windows. All output shall be through files.
* Change the line and dash pattern for `line2` in `line_demo_dash_control`.

## Example Output
The program shall open three additional windows to display plots.
```
$ ./matplotlib_demo.py
Writing out figure to simple_plot.png
Writing out figure to line_demo_dash_control.png
Writing out figure to timeline.png
$
```

