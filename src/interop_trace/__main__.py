"""Executable module for ``python -m interop_trace``.

Python runs this file when the package is executed as a module. The real entry
logic lives in ``main.py`` so it can also be imported and tested directly.
"""

from interop_trace.main import main

if __name__ == "__main__":
    main()
