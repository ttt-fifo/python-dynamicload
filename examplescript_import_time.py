#!/bin/env python3
"""
Example script for dynamic loading during import time
Play with the imports and rerun the script
"""

# Play with the imports -------------------------------------------------------
# (comment and uncomment some of them and rerun the script)
# from examplepackage import examplemodule
# from examplepackage import exampleclass
# from examplepackage import examplefunction
# -----------------------------------------------------------------------------

import sys
from pprint import pprint
import examplepackage

print("Current import status:")
print("======================")
pprint(examplepackage.REGISTRY)
print()
print()
print("Current imported modules")
print("========================")
for module in [m for m in sys.modules if m.startswith('example')]:
    print(module, ':', sys.modules[module])
print()
