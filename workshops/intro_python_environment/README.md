# Introduction and Setting Up a Python Environment Bootcamp 

In this workshop, we will be discussing:

- What is python?
- What is a python installation, a script file, and an IDE?
- How do I install python on my computer?
    - Native installation (often with Linux)
    - Anaconda (with Windows, Mac, and Linux - recommended for this bootcamp)
    - Online Environment (Google Colab - works for some workshops, but not for Robotics)
- What is a python package? 
- How do I start programming with python?

## What is Python?
Python is a programming language. There are many, many programming languages you can use to make computers 'do stuff'. C and C++ are very popular languages, as are Rust, Go, Java, Ruby, etc. Different programming languages may have different underlying system design structures, and some are better suited to certain tasks than others. As my CS 120 professor would say, however, programming languages are "tools for the job". One isn't necessarily better than another in all circumstances. You have to pick the one that will get the job you need done. 

We are choosing to base the bootcamps mostly on python for the following reasons:

- For many, it is a relatively easy to learn language, compared to languages like C/C++
- Python is very popular with data scientists and robot engineers. Many packages (already-written pieces of code we use programming libraries) are developed for certain tasks in python. However, for more embedded systems-type applications, C/C++ are often more popular languages. 
- Python is also very popular for machine learning and AI 
- It is fairly easy to install Python on different operating systems. 

Your operating system is the type of "brain" your computer has. Your computer is broken up into its hardware components (its keyboard, its processing chip, its hard drive, its power button) and its software components (its operating system & installed applications). One of the most basic pieces of software is your operating system, since it decides how you interact with the computer, how you store your files, how you install new software, and how you interface with the internal hardware (like the hard drive) and external hardware (like a thumbdrive or a printer). 

Examples of Operating Systems include:
    Windows 10
    Windows 11
    Mac OS 15 Sequoia
    Ubuntu 22.04 (a type a linux system)
    Raspbian Bookworm (also a type of linux system)

Different operating systems have different purposes in functions. However, there are very few operating systems you can't set up a programming environment in. Linux has a reputation of being more friendly to developing with programming language, especially when it comes to using a computer program to control external hardware devices (like a microcontroller plugged into the computer). But there are tons of developers who use MacOS (which uses a Linux-like Unix system) and Windows. 

You can install Python with any of these operating systems. 


## What is a Python Installation, a Script File, and an IDE?
The word "computer program" is more than a little bit abstract. A computer program is some way of giving instructions to a computer. But sometimes a computer file has to go through several changes before your operating system is able to **run** the instructions its given it. A computer programming language is a way of writing instructions that will be executed a certain way on the computer, based on what was written. But how do you write these instructions?

Different kinds of instructions require different formats. 

You could run a program with all 0s and 1s (if you take the Computer Architecture class at UI, you can actually do that as extra credit - have fun). These correspond to signals being "off" or "on" that control the very, very low-level harware of your computer processor. 

You could run a program in machine code, which is a set of instructions designed for your computer processor - your computer chip which may have been made by Intel or Apple -- to run. Machine code instructions are usually words and registers, and are also a bit hard to understand. Machine code is slightly less "low-level" than those binary 0s and 1s, but not much!

You will probably program in another level up, a programming language. A programming language outlines sets of instructions that are easier to read and understand when giving your computer a logical task to perform. There are certainly still nuances in this - for example, in a C program, you write a program with text in a .c file, but then you have to use another program - called a compiler - to turn the c file into another type of file, which you can then run directly. For today though, just know we are using the python programming language, which uses a fairly readable set of words, phrases, and symbols to let you tell a computer what to do. 

python programs are created in files called **scripts**. A python script is a file type that ends in .py. Python is an interpreted language. Once you finish writing a python program, you use your installed python software to **run** that file, which will execute the commands on your computer, one line at a time. You have to have a **python installation** to be able to run your written computer program -- the **python script file**. 

To recap so far:

- python is a programming language. It's a way to write instructions to your computer that can be run on your machine. 
- python programs are written in the python programming language. These are text files that end in the .py extension. 
- You have to have python software installed to be able to "run the programs", that is, to be able to tell the computer how to turn your written program file into a set of instructions it can execute. 

When you have the python software installed, you will usually run the prgrams via a **terminal**. 

You have probably seen the terminal in approximately a quarter billion movies. For some reason no one ever sees anyone in movies use a mouse in a terminal. You absolutely can. You don't even have to say "I'm in". 

You execute commands on your computer all the time, but you are probably used to doing that via pointing and clicking on things. Lets say you are want to open a Microsoft Word document stored on a folder in your desktop called "homework". When you point and click on the folder to open that window, you are using a graphical user interface, often abbreviated as GUI. When the folder window pops open, you can see your essay.docx file inside. You can open the file by double clicking on the file. 

You just executed several commands on your computer using a GUI. A terminal is just another way of executing commands on your computer, but it uses text commands via the terminal prompt to do so. Lets change the scenario to a Linux computer, and you want to open your homework using the terminal. You could do the same sequence of commands by type 

    cd Desktop/homework

"cd" in linux world means change directory, and this command has you change directory into the "Desktop" folder, and then the "homework" subfolder. Once there, you would type:

    ls

which would print a list of the files in that folder. You might see the output of:

    essay.odt 

which is your essay document (in an open document format -- hence the extension). Now, if you want to open it, you could type

    libreoffice essay.odt 

which uses the "libreoffice" software program to open the "essay.odt" file so you can work on it. 

Working with terminal commands can be a bit of a learning curve, and commands are different depending on whether or not you are using Windows, Mac, or Linux. We are going to keep it simple in these workshops. 

A quick note -- growing up, I always thought Linux computers were just terminals. That might be the case for some servers, but most of the time, if you install Linux on your computer, it is going to come with a GUI. Thank goodness. Unlike the TV hackers, I like to point and click. 

We will be using a terminal to run our python programs most of the time. In a terminal, the text before the area you can type (the area you can type in is the prompt area) usually displays your file path. You typically want the file path to reflect the folder the python program is stored in. 

For example, if I have a python program named "Hello_World.py", and my filesystem looks like this:

- Documents
    - program_files
        Hello_World.py 
    - homework
        - essay.docx
- Desktop
    - age_of_empires.exe
    - pong.exe
- Downloads
    - Kong_Skull_Island_Illegal_Pirated_Copy.mp4 
    - the_watergate_tapes.wav
    - stuxnet.obj

Then I will want my terminal path to say 

```bash
    ~/Documents/program_files
```
Then I can run my python program in the terminal window by typing 

    python3 hello_world.py 

which tells my computer "use the python3 software I have installed to act on the hello_world.py file I have written". Your computer will do that, and execute the commands you have written in the hello_world.py file. Magic! Sort of. 

One note - most operating systems don't handle spaces in file names or folder names very well, since it is hard for the terminal to be sure if it a space in a filename or a separation from a terminal command and a file name or a separation from one terminal command to another. That's why you'll see underscores used all over the place instead of spaces when it comes to programming. Otherwise you have to get real fancy with quotes. And you will probably have some frustrating bugs anyway. 

Now lets talk about an IDE. IDE stands for 
- **I**ntegrated
- **D**evelopment
- **E**nvironment

Which is usually  a fancy way of saying "software application program that helps you write code files". It's basically a big fancy text editor. Like you might use Microsoft Word to write an essay, you would probably use an IDE to write a programming code file. Some IDEs have terminal windows built in so you don't have to access it from your system, which is nice. 

An IDE is an application, so there are MANY IDEs out there you could use. 

What's the best IDE? I recommend asking that question any time you are bored and want to see your computer science friends have a fistfight. In this office, we probably argue about it at least once a month. 

There are some terminal-based programming text editors you can use, that mostly rely on typing commands. Vim, Emacs, and Nano are examples. Vim and Nano come preinstalled with most linux version. It is often easier for programming to use something with a little bit of a GUI and maybe a terminal, so IDEs like VS Code and PyCharm are maybe more popular if you are getting started. I'm using the VS Code IDE to write this guide in the markdown (.md) language write now. 

I used Nano my ENTIRE undergraduate. I have started fights with that statement many times. I wish I could say it was because I was hard core. Actually, it was because I didn't know an IDE was an option. I sure learned to debug, though. 

When you install your python environment, we will also install an IDE to make it easier for you to write program and debug your code. I would recommend something like VS Code (a Microsoft application, but it runs on most OS's, and is useful for many languages) or PyCharm (easy to install with Anaconda, meant for Python) or Spyder.  

There are also some specialized IDEs, that may be only designed for one language or device. If you are around for the Arduino bootcamp later, you'll install the Arduino IDE. 

Review:
- an IDE is an application that helps you write programming files. They can be basic ways to edit text, or they can have fancier features, like GUI code highlighting, or maybe a built in terminal.
- A python program file is a text file with a .py extension. It contains written instructions to the computer. 
- Your python software installation lets you run your written python files on your computer. 
- You use your terminal, located where your python file is, to run your written python file using the python software. 

Whew! Lets move on to installing python. We will start with the installing Python software, then move on to installing an IDE. After that, we'll go over writing a python code file and running it on your computer, using the terminal. 


## How Do I Install Python on my Computer?

### Native Installation
You can install python directly on your computer with some systems. If you have a linux OS (Ubuntu is a 'flavor' or linux, as well as Arch, RedHat, PopOS, and many others) you can download the python software directly onto your machine. For these sets of workshops, you will likely want a version of Python3 greater than 3.10 to make sure systems are compatible. Most modern python installations will meet or exceed that version by default. If you have a linux machine, you may already have Python installed (most Raspberry Pi OS's come with it natively.)

To check if you have python already installed (on a Linux machine), you can open a terminal window and type:

```bash
    python3 --version
```

or 

```bash
    python --version 
```

This should print out a version number, if the software is already installed. If not, you will probably get a "command python3 not found" message or something similar. 

For this workshop, we are going to focus mostly on creating a python installation via the Anaconda software, since this creates **virtual environments** for you to play around with python. 

A **virtual environment** installs packages and software in a standalone way that doesn't interfere with the base software installed on your computer. The advantage of a virtual environment comes from the fact that if you mess up installing some software or dependencies, you won't screw up your whole system. You can also try different installation versions of software in different virtual environments if need be. The disadvantages include more overhead to activate and manage different virtual environments, and sometimes (depending on the type of virtual environment you are using) unavailability of certain packages. 

If you want to do a **base native install**, however, we will link some tutorials for that. On linux, this is fairly straightforward. On Windows, it is less straightforward - however, on most modern Windows computers you can install **WSL** -- The **W**indows **S**ubsystem for **L**inux. This gives you a Linux-like interface right on your Windows machine! It has some additional considerations for finding files and managing external devices, however, so be aware. 


1. [Here is a guide for installing python on Windows using WSL as the terminal interface and VS Code as the IDE](https://learn.microsoft.com/en-us/windows/python/web-frameworks)

2. [Here is a guide with a couple of different options for installing python on Ubuntu](https://www.cherryservers.com/blog/install-python-on-ubuntu)


If you are planning to do a LOT of programming the future, I would recommend considering getting some sort of Linux environment set up. This could be via a Dual Boot or something similar (I completely imaged my machine and use Ubuntu every day. I love my Ubuntu laptop. However, I didn't image it perfectly and lost access to an SSD. User beware.)


For the purpose of this camp, we are going to mainly focus on this guide:

[Installing Python via Anaconda for Windows with VSCode as Your IDE](Install_Anaconda_Windows.md)

If you are having trouble with the installation, one way to quickly get up and going is by using Google Colab. In that case, you can follow [this externally linked guide to using Google Colab](https://www.marqo.ai/blog/getting-started-with-google-colab-a-beginners-guide)


## What are Python Packages and How do I Install Them?

If you want to build a car, you might start with a frame, maybe some tires, and an engine -- but you would probably buy these things to assemble into your car. You probably won't start mining the precious metals you need to make the car components. 

Python packages are pieces of pre-assembled code that you can fit into your own programs. These usually take the form of **function** calls (functions take inputs, perform operations, and give you back an output, typically) and/or **classes** (collections of functions and variables in a structured format) that are take a lot of the headaches out of doing programming. One of the reasons python is such a popular language is because many programmers have developed for it by writing large collections of useful packagaes or libraries. 

You have to import python packages into your code file to be able to use the pieces of code inside the packages. But before you can import a library into your programming script file, you first must install the library. 

If you are using conda, this will usually take the form of:
```bash
    conda install <package_name>
```
where "package_name" is the name of the library you are trying to install. 

If you have a more native linux-like environment, you will either run 

```bash
    pip install <package_name>
```
or 

```bash
    pip3 install <package_name>
```

Interesting note - "python" for a long time meant python2, where the more modern version (Python3, which we are using today) was referenced by "python3". Now, many systems default to using the word "python" for python3 -- so which one you use depends on your installation. pip is the package manager for native python distributions (which you may need to install on your system first) where conda install is the package management command for anaconda. like python/python3, you may use pip or pip3 depending on your installation. Heads up, if both are installed, this can get confusing. 

If you are using Google Colab, many of the packages you would want to use already come pre-installed. If, however, you need something else, you can use the pip command with a % sign in front of it directly inside the python script code cell, for example 

    %pip install <package_name>

When you import a package into a code file, you type 

    import <package_name>

Calling a function, classes, or other object inside the package library uses the dot notation. For example

    <package_name>.<function_I_want>

calls the "function I want" function on the "package_name" package. 

You have to use the package name in front of each object you want to access inside the package. If the package name is really long, this can get annoying. You can rename the package name on import if you want by typing 

    import <package_name> as <short_name>

after which, you could run:
    
    <short_name>.<function_I_want>

There is more to imports than this, and ways you can restrict what you want to import if a package is really large, but we won't go into it much for this workshop. 



## How do I Start Programming in Python? 
Let's make a really simple python program. Open up a blank python file and name it something like "learn.py". Type:

    variable = 0
    for i in range(0, 10):
        print(variable)
        variable += 1
    if variable > 5:
        print("Variable is larger than 5")
    else:
        print("Variable smaller than or equal to 5")
    variable = variable - 2
    print(variable)

and run the program using 

```bash
    python learn.py
``` 
You should get output that looks like: 

```bash
0
1
2
3
4
5
6
7
8
9
Variable is larger than 5
8
```
The first line creates a variable (named variable) and assigns it a value of 0. Then a loop starts, which creates another variable i, and wants the code to execute the lines indented below it for the values of i between 0 and 9 (range doesn't include the value 10). Each time, it prints the variable, then adds a value of 1 to its existing value. After that loop, the code checks the value of variable. It prints one thing if variable is great than 5, and another if it is less than or equal to 5. Finally, 2 is subtracted from variable, and the value is printed once more. 

## Common Mistakes to Avoid
Don't name your python file the same name as a library you plan to import. Python will get confused and will likely not import the library correctly (or say it can't find the file)

Indentation matters in python. If code it not indented correctly, you will get errors. 

Some loops in python include the last number article provided and some do not. You will probably have to look up which do and which don't. 

Some objects are copied when assigned to new variables and some are not. If something is behaving oddly in the code, it might be because your code was acting on the original object and not a copy of it. Be especially aware with list and dictionary objects. 

## Where to Go Next 
Some packages we will be using in future workshops you may want to install:
- pandas
- matplotlib
- seaborn
- scikit-learn
- opencv (this one can sometimes cause issues in conda, so be aware. You may want to use Google Colab)
