"""In this file, I will demonstrate the use of Python enumerate() Method."""

# USAGE
# The enumerate() function adds a counter to an iterable and returns it as an
# enumerate object.

# By default, enumerate() starts counting at 0 byt if you add a second argument
# start, it'll start from that number instead.

# SYNTAX: enumerate(iterable, [start])

# BASIC EXAMPLE
orchids = ['moth', 'boat', 'cattleya', 'vanda', 'dancing-lady']

print(list(enumerate(orchids)))

print()

# SPECIFY DIFFERENT START
# By Default, enumerate() starts counting at 0 but if you add a second argument
# start, it'll start from that number instead
print(list(enumerate(orchids, start=1)))
