This documentation is for ``3-say_my_name`` module
==================================================

The function is ``say_my_name``
-------------------------------

The function ``say_my_name`` is imported from the module ``3-say_my_name`` in the following line of code:

	>>> say_my_name = __import__("3-say_my_name").say_my_name

	>>> say_my_name("John", "Smith")
	My name is John Smith

	>>> say_my_name("Walter", "White")
	My name is Walter White

	>>> say_my_name(12, "White")
	Traceback (most recent call last):
	TypeError: first_name must be a string

	>>> say_my_name("Walter", 10)
	Traceback (most recent call last):
	TypeError: last_name must be a string

	>>> say_my_name()
	Traceback (most recent call last):
	TypeError: say_my_name() missing 1 required positional argument: 'first_name'
