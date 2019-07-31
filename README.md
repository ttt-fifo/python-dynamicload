# Python >= 3.7 Dynamic Load Recipe

How to load your code dynamically is one commonly discussed topic for Python. There are multiple stackoverflow discussions about this (examples: [1](https://stackoverflow.com/questions/951124/dynamic-loading-of-python-modules), [2](https://stackoverflow.com/questions/547829/how-to-dynamically-load-a-python-class)) and the methods for dynamic loading have developed over time together with the development of the Python versions. In [PEP562](https://www.python.org/dev/peps/pep-0562/) something I call "magic methods for modules" was introduced and they [were implemented in Python 3.7](https://docs.python.org/3/whatsnew/3.7.html#whatsnew37-pep562). The [current implementation](examplepackage/__init__.py) of the dynamic loading is using exactly these Python 3.7 features.

## Features

* Easy implementation - just copy ```__init__.py``` to the root of your package and change IMPORTS string

* IMPORTS string is human readable and showing what you schedule for dynamic imports

* Quick and dirty inspection of the package behavior using the REGISTRY dictionary

* The code for parsing REGISTRY dictionary is clear and many other methods of parsing may be implemented instead to suit your needs for dynamic loading

* The documentation (current README) is aiming to be comprehensive for the needs of dynamic loading

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

See [examplescript_import_time.py](examplescript_import_time.py)

* You may even need to load chosen parts of your code during runtime

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

See [examplescript_runtime.py](examplescript_runtime.py)

* I would **love** to hear from **you** what are your use cases for using dynamic loading with Python? Do not hesitate to [open an issue](https://github.com/ttt-fifo/python-dynamicload/issues) to initiate a discussion!

## Getting Started

* Download the current github repo locally:

```
git clone https://github.com/ttt-fifo/python-dynamicload
```

* CWD to the local directory of the cloned repo:

```
cd python-dynamicload
```

* Review the file ```examplepackage/__init__.py``` to see how the dynamic loading is implemented

```
vim examplepackage/__init__.py
```

* Review ```examplescript_init_time.py``` and ```examplescript_runtime.py``` and take some time to play with them

* Open your [REPL](https://pythonprogramminglanguage.com/repl/) of choice and play with the concepts described into the "Proof of Concept" below

* Create your own package - see below "How to Create Your Own Dynamically Loaded Python Package"

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

* In case you do not know which functions, classes, modules, etc. are dynamically loadable from your package (or maybe you are a consumer, who will use the package for the first time):

Open your [REPL](https://pythonprogramminglanguage.com/repl/) of choice, import the package and dir() it:

```
>>> import examplepackage
>>> dir(examplepackage)
['exampleclass', 'examplefunction', 'examplemodule']
>>>
```

* You would like to know what an attribute does?

Use the help() command on one package attribute:

```
>>> help(examplepackage.examplefunction)
Help on function myfunction01 in module examplepackage.examplemodule01:

myfunction01(*arg, **kwarg)
    This is an example dynamically loaded function.
    Arguments: accepts everything as argument
    Returns: True
/tmp/tmp3auxnclb (END)
```

NOTE: the help(...) command first loads the attribute in memory, then reads the docstring of the particular attribute.

* ...and if you would like to have the full help of everything:

Use help(yourpackagename) - NOTE: this will load all the dynamically loadable attributes prior giving you the help, so maybe time consuming:

```
>>> help(examplepackage)
.................
.................
.................
```

* In your script as a consumer you may import dynamically the needed code during import time - see example in [examplescript_import_time.py](examplescript_import_time.py)

* In your script as a consumer you may dynamically import code during runtime - see example in [examplescript_runtime.py](examplescript_runtime.py)

### Proof of Concept

* **Go to the directory of the current recipe and open your [REPL](https://pythonprogramminglanguage.com/repl/) of choice - in my case [bpython](https://bpython-interpreter.org/)**

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
9. ```pprint(examplepackage.REGISTRY)``` shows the contents of the variable REGISTRY, which is a dictionary used to hold the import statements for dynamic loading and/or the current state of the actual imported code. You can see that the key 'exampleclass' is actually loaded class and the keys 'examplefunction', 'examplemodule' are still showing the import strings (this means they are still not dynamically imported)

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

10. ```examplepackage.examplefunction``` loads in memory the module examplepackage.examplemodule01 and afterwards imports examplepackage.examplemodule01.myfunction01 as examplefunction. Lets inspect this - see the following bulletpoints:
11. ```for module in [...] ... print(...)``` now shows three modules loaded in memory: ```examplepackage.___init__```, ```examplepackage.examplemodule01```, ```examplepackage.examplemodule02```
12. ```pprint(examplepackage.REGISTRY)``` - this inspection shows that 'exampleclass' and 'examplefunction' are already dynamically imported, but 'examplemodule' is not imported, because it is showing only the import string. Actually 'examplemodule' is one interesting case, so I dedicate the next paragraph to it - see below...

* **The interesting case of examplemodule**

The examplemodule would be dynamically imported like this: ```from . import examplemodule01 as examplemodule```, but it is currently not imported. Is examplemodule01 already loaded in memory? **Yes**, because we already imported myfunction01 from this module, so examplemodule01 has been loaded in memory during the import of myfunction01 as examplefunction.

* **Load dynamically the last fraction - examplemodule**

```
>>> examplepackage.examplemodule
<module 'examplepackage.examplemodule01' from '/home/ttodorov/projects/python-dynamicload/examplepackage/examplem
odule01.py'>
>>> pprint(examplepackage.REGISTRY)
{'exampleclass': <class 'examplepackage.examplemodule02.MyClassTwo'>,
 'examplefunction': <function myfunction01 at 0x7efc3b8a6830>,
 'examplemodule': <module 'examplepackage.examplemodule01' from '/home/ttodorov/projects/python-dynamicload/examp
lepackage/examplemodule01.py'>}
>>>
```

13. ```examplepackage.examplemodule``` only imports examplepackage.examplemodule01 as examplemodule without loading anything in memory. The reason for this is that examplemodule01 was already loaded in memory.
14. ```pprint(examplepackage.REGISTRY)``` now shows that all dynamically loadable attributes are already imported.

## Contributing

* Having comments, ideas, something unclear? - do not hesitate to open an [issue](https://github.com/ttt-fifo/python-dynamicload/issues) and initiate a discussion

* Are you using this code and for what? - [issue](https://github.com/ttt-fifo/python-dynamicload/issues)

* Having issues with this code? - guess what? - open an [issue](https://github.com/ttt-fifo/python-dynamicload/issues) :-) :-)

Any other ways of contribution are welcomed.

## Versioning

See the [tags on this repository](https://github.com/ttt-fifo/python-dynamicload/tags). 

## Authors

* **Todor Todorov** - [ttt-fifo](https://github.com/ttt-fifo)

## License

Feel free to use at your own will - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Special thanks to [Guido van Rossum](https://gvanrossum.github.io/) for being around and for inventing [this](https://python.org) enormously complex piece of software, which makes our life easier on a daily basis.

* Thanks to all the people working on the idea and implementation of [PEP562](https://www.python.org/dev/peps/pep-0562/)

* Thanks to [Geir Arne Hjelle](https://realpython.com/team/gahjelle/) for the [inspiration](https://realpython.com/python37-new-features/)

## See Also

There are other people (smarter than me) doing similar things out there:

Plugin system using the same approach: [https://realpython.com/python37-new-features/](https://realpython.com/python37-new-features/)

Blog for dynamic import in python3 here: [https://www.bnmetrics.com/blog/dynamic-import-in-python3](https://www.bnmetrics.com/blog/dynamic-import-in-python3)
