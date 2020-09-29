#include <bits/stdc++.h>
using namespace std;

class Bisection {
    public:
        double a, b, c;
        const double eps = .01;
    
    public:
        // constructor for initialize member variable
        Bisection() {
            a = b = c = 0.0;
        }

        // return function value
        double function(double x) {
            return (x * x * x - x * x + 2);
        }

        // guess a and b [a...root....b]
        void guessValue() {
            while(true) {
                if (function(a) * function(b) < 0) {
                    break;
                } else {
                    a -= .5;
                    b += .5;
                }
            }
        }

        // bisection function
        double bisection() {
            guessValue();
            c = a;

            cout << "a :" << a << " b: " << b << endl;
            // return 0.0;

            while((b - a) >= eps) {
                c = (a + b) / 2;
                
                if(function(c) == 0.0) {
                    break;
                } else if (function(a) * function(c) < 0.0) {
                    b = c;
                } else {
                    a = c;
                }
            }
            
            return c;
        }
};

int main() {
    Bisection ob;
    
    double root = ob.bisection();

    cout << "Root: " << root <<endl;

    return 0;
}