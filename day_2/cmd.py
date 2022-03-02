import sys
import numpy
import glob

import os.path

def detect_problems(filename):
    try:
        data = numpy.loadtxt(fname=filename, delimiter=',')

        max_inflammation = numpy.max(data, axis=0)
        min_inflammation = numpy.min(data, axis=0)

        if (max_inflammation[0] == 0) and (max_inflammation[20] == 20):
            print('Suspicious looking maxima!')   
        elif numpy.sum(min_inflammation) == 0:
            print('Minima add up to zero')
        else:
            print("Data looks OK")
    except:
        raise NameError

def say_something(phrase):
    sys.stdout.write(phrase)
    
def main(filenames_path):
    filenames = glob.glob(filenames_path)
    assert filenames, "No found files"
    for file in filenames:
        if os.path.isfile(file):
            detect_problems(file)
        else:
            print("File doesnt exist")
        

if __name__ == "__main__":
    main(sys.argv[1])
    