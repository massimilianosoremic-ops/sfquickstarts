import sys
from scipy.constants import convert_temperature

def main(temp_f: float) -> float:
    return convert_temperature(float(temp_f), 'F', 'C')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(main(float(sys.argv[1])))
    else:
        print(main(32.0))
