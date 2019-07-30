# Python 3.7 Dynamic Load Example

How to load your code dynamycaly is one commonly discussed topic for Python. There are multiple stackoverflow discussions about this (examples: <a href="https://stackoverflow.com/questions/951124/dynamic-loading-of-python-modules" target="_blank">1</a>, <a href="https://stackoverflow.com/questions/547829/how-to-dynamically-load-a-python-class" target="_blank">2</a>) and the methods for dynamic loading have developed over time together with the development of the Python versions. In [PEP562](https://www.python.org/dev/peps/pep-0562/) the "magic methods for modules" were introduced and and they <a href="https://docs.python.org/3/whatsnew/3.7.html#whatsnew37-pep562" target="_blank">became true in Python 3.7</a>. The [current implementation](examplepackage/__init__.py) of the dynamic loading is using exactly these Python 3.7 features. Why and when would you need to load your Python code dynamically?

* Building a plugin system

You can create a Python package 'plugins' with pluggable code like this:

```
.
└── plugins                ---> the python package directory
    ├── __init__.py        ---> here the dynamic loading is implemented
    ├── plugin00001.py     ---> module with plugin function 1
    ├── plugin00002.py     ---> module with plugin function 2
    └── plugin00003.py     ---> module with plugin function 3
```

* Whenever your have a huge codebase, but you do not need all your code loaded in the memory all the time

Imagine that the plugin count in the previous example is about 100000?

```
.
└── plugins
    ├── __init__.py
    ├── plugin00001.py
    ├── plugin00002.py
    ├── plugin00003.py
    ├── ...
    └── plugin99999.py
```

* You need to choose which part of your code to be loaded during import time

At the top of your Python script:

... if you need to use the example function 'exfunct'

```
from examplepackage import exfunct
```

... or if you do not need exfunct to be loaded in memory, only ExClass

```
from examplepackage import ExClass
```

* You may even need to load choosen parts of your code during runtime

Like this:

```
# import time ----
import examplepackage
# ----------------
.....
# runtime --------
.....
f_name = 'exfunct'
.....
f = getattr(examplepackage, f_name)
somevar = f('some', 'awesome', 'args')
# ----------------
```

* I would **love** to hear from **you** how do you use dynamic loading with Python? Do not hesitate to [open an issue](https://github.com/ttt-fifo/python-dynamicload/issues) to initiate a disussion!

## Getting Started

* Download the current github repo locally:

```
git clone https://github.com/ttt-fifo/python-dynamicload
```

* Review the file ```python-dynamicload/examplepackage/__init__.py``` to see how the dynamic loading is implemented

```
vim python-dynamicload/examplepackage/__init__.py
```

* Copy the examplepackage/ directory into one of your [Python site packages directories](https://docs.python.org/3/library/site.html). For a linux system this would do the trick:

```
cd python-dynamicload
mkdir -p ~/.local/lib/python3.7/site-packages
cp -r examplepackage ~/.local/lib/python3.7/site-packages 
```

* Open your [REPL](https://pythonprogramminglanguage.com/repl/) of choice and play with the concepts described into the "Proof of Concept" below

* Now you would be ready to create your own package - see below "How to Create Your Own Dynamic Loaded Python Package"

### Prerequisites

Python >= 3.7

### How to Create Your Own Dynamic Loaded Python Package

TODO: A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

### How to Consume the Dynamic Loaded Python Package

TODO: A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo


### Proof of Concept

TODO: REPL example

## Contributing

TODO:
Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

TODO:
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Todor Todorov** - [ttt-fifo](https://github.com/ttt-fifo)

## License

Feel free to use at your own will - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

TODO:

* Hat tip to anyone whose code was used
* Inspiration
* etc


