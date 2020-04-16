import netron
import sys

if __name__ == "__main__":
    filepath = sys.argv[1]
    netron.start(filepath)