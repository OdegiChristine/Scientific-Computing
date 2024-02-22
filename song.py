# Odegi Christine, SCT211-0093/2022
# Scientific Computing Assignment #3

# This program...

def main():
    stanza1_lines()
    print()
    stanza2_lines()
    print()
    stanza3_lines()
    print()
    stanza4_lines()
    print()
    stanza5_lines()
    print()
    stanza6_lines()
    print()
    last_verse()


def last_two():
    print('''I don't know why she swallowed that fly,
Perhaps she'll die.''')


def spider():
    print('''She swallowed the spider to catch the fly,''')


def bird():
    print('''She swallowed the bird to catch the spider,''')


def cat():
    print('''She swallowed the cat to catch the bird,''')


def dog():
    print('''She swallowed the dog to catch the cat,''')


def last_verse():
    print('''There was an old woman who swallowed a horse,
She died of course.''')


# The first few lines of the stanzas
def stanza1_lines():
    print('''There was an old woman who swallowed a fly.''')
    last_two()


def stanza2_lines():
    print('''There was an old woman who swallowed a spider,
That wriggled and iggled and jiggled inside her.''')
    spider()
    last_two()


def stanza3_lines():
    print('''There was an old woman who swallowed a bird.
How absurd to swallow a bird.''')
    bird()
    spider()
    last_two()


def stanza4_lines():
    print('''There was an old woman who swallowed a cat.
Imagine that to swallow a cat.''')
    cat()
    bird()
    spider()
    last_two()


def stanza5_lines():
    print('''There was an old woman who swallowed a dog,
What a hog to swallow a dog.''')
    dog()
    cat()
    bird()
    spider()
    last_two()


def stanza6_lines():
    print('''There was an old woman who swallowed a kid,
Oh how stupid to swallow a kid.
She swallowed the kid to catch the dog,''')
    dog()
    cat()
    bird()
    spider()
    last_two()


main()
