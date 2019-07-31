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

* Go to the directory of the current recipe and open your [REPL](https://pythonprogramminglanguage.com/repl/) of choice - in my case [bpython](https://bpython-interpreter.org/)

```
ttodorov@personal:~$ cd ~/projects/python-dynamicload/
ttodorov@personal:~/projects/python-dynamicload$ bpython
bpython version 0.18 on top of Python 3.7.4 /home/ttodorov/opt/Python-3.7.4/bin/python3.7
>>>
```

* **Import the example package**

```
>>> import examplepackage
>>>
>>> dir(examplepackage)
['exampleclass', 'examplefunction', 'examplemodule']
>>>
```

1. ```import examplepackage``` actually imports the package
2. ```dir(examplepackage)``` shows you the list of attributes, which you could use from this package. Later on I will show that these attributes are still not loaded in memory, but could be loaded dynamically on demand.

* **Inspect what is loaded in memory before any dynamic loading**

```
>>> import sys
>>>
>>> for module in [m for m in sys.modules if m.startswith('example')]:
...     print(module, ':', sys.modules[module])
...
...
examplepackage : <module 'examplepackage' from '/home/ttodorov/projects/python-dynamicload/examplepackage/__init_
_.py'>
>>>
```

3. ```import sys``` - we need to import sys package for further inspection of sys.modules
4. ```for module in [...]``` iterates through all currently loaded modules which name starts with 'example'
5. ```print(module, ':', sys.modules[module])``` prints every module loaded in memory which name starts with 'example'. We can see that only one module is in memory and it is the ```__init__.py``` from examplepackage.

* **Load dynamically one class**

```
>>> examplepackage.exampleclass
<class 'examplepackage.examplemodule02.MyClassTwo'>
>>>
```

6. Issuing ```examplepackage.exampleclass``` loads dynamically the module examplepackage.examplemodule02 in memory, then it imports dynamically MyClassTwo as examplepackage.exampleclass. Lets inspect this in the next section!

* **Inspect the memory after one dynamic load**

```
>>> for module in [m for m in sys.modules if m.startswith('example')]:
...     print(module, ':', sys.modules[module])
...
...
examplepackage : <module 'examplepackage' from '/home/ttodorov/projects/python-dynamicload/examplepackage/__init_
_.py'>
examplepackage.examplemodule02 : <module 'examplepackage.examplemodule02' from '/home/ttodorov/projects/python-dy
namicload/examplepackage/examplemodule02.py'>
>>>
```

7. ```for module ... print ...``` shows that the module examplepackage.examplemodule02 is now loaded in memory after the dynamic load of examplepackage.exampleclass

* **More inspection by using the REGISTRY variable of the package**

```
>>> from pprint import pprint
>>>
>>> pprint(examplepackage.REGISTRY)
{'exampleclass': <class 'examplepackage.examplemodule02.MyClassTwo'>,
 'examplefunction': 'from .examplemodule01 import myfunction01 as '
                    'examplefunction',
 'examplemodule': 'from . import examplemodule01 as examplemodule'}
>>>
```

8. ```from pprint import pprint``` just imports a helper function for pretty printing
9. ```pprint(examplepackage.REGISTRY)``` shows the contents of the variable REGISTRY, which is a dictionary used to hold the import statements for dynamic loading and/or the current state of the actual imported code. You can see that the key 'exampleclass' is actually loaded class and the keys 'examplefunction', 'examplemodule' are still showing the import strings.

* **One more dynamic load - load dynamically examplefunction**

```
>>> examplepackage.examplefunction
<function myfunction01 at 0x7efc3b8a6830>
>>>
>>> for module in [m for m in sys.modules if m.startswith('example')]:
...     print(module, ':', sys.modules[module])
...
...
examplepackage : <module 'examplepackage' from '/home/ttodorov/projects/python-dynamicload/examplepackage/__init_
_.py'>
examplepackage.examplemodule02 : <module 'examplepackage.examplemodule02' from '/home/ttodorov/projects/python-dy
namicload/examplepackage/examplemodule02.py'>
examplepackage.examplemodule01 : <module 'examplepackage.examplemodule01' from '/home/ttodorov/projects/python-dy
namicload/examplepackage/examplemodule01.py'>
>>>
>>> pprint(examplepackage.REGISTRY)
{'exampleclass': <class 'examplepackage.examplemodule02.MyClassTwo'>,
 'examplefunction': <function myfunction01 at 0x7efc3b8a6830>,
 'examplemodule': 'from . import examplemodule01 as examplemodule'}
>>> 
```


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


