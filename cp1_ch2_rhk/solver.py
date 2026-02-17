import math
import sys

def v_x(t):
    return math.exp(-(t * t)) * (t + 10 * math.sin(math.pi*t))


#
# Take the arguments and simply go from the min to the 
# max given the step specified
#
def main(min, max, step) :
    t = min
    while t < max :
        velocity = v_x(t)
        print("t = " + str(t) + "v_x = " + str(velocity))
        t = t + step
    
    return

if __name__ == '__main__':
    main(int(sys.argv[1], 10), int(sys.argv[2], 10), float(sys.argv[3]))