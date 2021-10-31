'''
Python first compiles your source code (.py file) into a format known as byte code . Compilation is simply a translation
step, and byte code is a lower-level, and platform-independent, representation of your source code. Compiled code is usually
stored in .pyc files , and is regenerated when the source is updated, or when otherwise necessary. In order to distribute a
program to people who already have Python installed, you can ship either the .py files or the .pyc files.

The bytecode (.pyc file) is loaded into the Python runtime and interpreted by a Python Virtual Machine , which is a piece of
code that reads each instruction in the bytecode and executes whatever operation is indicated. Byte code compilation is automatic,
and the PVM is just part of the Python system that you have installed on your machine. The PVM is always present as part of the
Python system , and is the component that truly runs your scripts. Technically, it's just the last step of what is called the
Python interpreter. And this is how the process is done (very general). Of course, there are optimizations and caches to improve the performance.
'''