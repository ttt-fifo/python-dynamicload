# Python 3.7 Dynamic Load Recipe

How to load your code dynamycaly is one commonly discussed topic for Python. There are multiple stackoverflow discussions about this (examples: [1](https://stackoverflow.com/questions/951124/dynamic-loading-of-python-modules), [2](https://stackoverflow.com/questions/547829/how-to-dynamically-load-a-python-class)) and the methods for dynamic loading have developed over time together with the development of the Python versions. In [PEP562](https://www.python.org/dev/peps/pep-0562/) something I call "magic methods for modules" was introduced and and they [were implemented in Python 3.7](https://docs.python.org/3/whatsnew/3.7.html#whatsnew37-pep562). The [current implementation](examplepackage/__init__.py) of the dynamic loading is using exactly these Python 3.7 features. The goals of dynamic loading are: less memory footprint, choosing which parts of your code to be loaded during import time and during runtime.

## Use Cases

* Building a plugin system

You can create a [Python package](https://realpython.com/python-modules-packages/) 'plugins' with pluggable code like this:

```
.
└── plugins                ---> the python package directory
    ├── __init__.py        ---> here the dynamic loading is implemented
    ├── plugin00001.py     ---> module with plugin function 1
    ├── plugin00002.py     ---> module with plugin function 2
    └── plugin00003.py     ---> module with plugin function 3
```

* Whenever your have a huge codebase, but you do not need all your code loaded in the memory all the time

Imagine that the plugin count in the previous example is about 100 000?

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

* You may need to choose which part of your code to be loaded during import time

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

* I would **love** to hear from **you** what are your use cases for using dynamic loading with Python? Do not hesitate to [open an issue](https://github.com/ttt-fifo/python-dynamicload/issues) to initiate a disussion!

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

* Now you would be ready to create your own package - see below "How to Create Your Own Dynamically Loaded Python Package"

### Prerequisites

Python >= 3.7

### How to Create Your Own Dynamically Loaded Python Package

* Develop your own [Python package](https://realpython.com/python-modules-packages/)
    - Spread the code inside the package into multiple modules
    - Every module to contain code, independent from the other modules

* Copy the ```examplepackage/__init__.py``` as the ```__init__.py``` for your module

* Put your dynamic imports into the IMPORTS string of ```__init__.py```
    - Every import should end with '... as somename' in order the parser to work properly
    - Example: ```from .mymodule import somefunction as someothername```

### How to Consume the Dynamically Loaded Python Package

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


