import collections
import sys


def main(letters, words):
    d = collections.defaultdict(list)
    print(d)

    print(letters)
    print(words)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
