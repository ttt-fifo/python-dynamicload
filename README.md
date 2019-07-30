# Python 3.7 Dynamic Load Example

How to load your code dynamycaly is one commonly discussed topic for Python. There are multiple stackoverflow discussions about this (examples: <a href="https://stackoverflow.com/questions/951124/dynamic-loading-of-python-modules" target="blank">1</a>) and the methods for dynamic loading have developed over time with the development of the Python versions. In Python 3 the magic methods for modules were introduced and and they became even better in Python 3.7. When would you need to load dynamically your Python code?

* Building plugins

You can create a Python package 'plugins' with pluggable code like this:

```
.
└── plugins
    ├── __init__.py
    ├── plugin00001.py
    ├── plugin00002.py
    └── plugin00003.py
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

... or if you do not need exfunct, only ExClass

```
from examplepackage import ExClass
```

* You even may need to load choosen parts of your code during runtime

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

TODO: These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

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


