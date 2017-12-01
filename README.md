# PythonBasics
Repo for my endeavors while learning Python


## PythoninOneHour (actually "Python in One Video")

Source: https://youtu.be/N4mEzFDjqtA
Commentary: The only prob appears at the end of the video and it is a conflict in the "toString" method in the child class "Dog". It surfaces due to the variables defined as private in both the parent and child classes and is resolved simply by using "get_***" methods instead of "__***" variables as arguments. E.g. "self.name" in the parent class, but "self.get_name()" in the child class. Another solution is to make the variables public so they can be accessed outside of the class. The author also uses the set and set that is more of a normal practice in Java, but not necessarily in Python.
