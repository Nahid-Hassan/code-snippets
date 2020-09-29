#include <bits/stdc++.h>
using namespace std;
#define max_iter 10


class RegularFalsi {
    public:
        double a, b, c;
        const double eps = .001;
    
    public:
        // constructor for initialize a, b and c
        RegularFalsi() {
            a = b = c = 0.0;
        }

        // calculate the function value
        double function(double x) {
            return (x * x * x - x * x + 2);
        }

        // guess value [a, b]
        void guessValue() {
            while(true) {
                if(function(a) * function(b) < 0) {
                    break;
                } else {
                    a -= .5;
                    b += .5;
                }
            }
        }
         
        // main function for calculating root using regular falsi method
        double ruglarFalsi() {
            guessValue();
            c = a;

            for(int i = 0; i < max_iter; i++) {
                c = ((a * function(b) - b * function(a)) / (function(b) - function(a)));

                // cout << "c : = " << c << " " << function(c) << endl;
                if (function(c) == 0.0) {
                    break;
                } else if (function(a) * function(c) < 0) {
                    b = c;
                } else {
                    a = c;
                }
            }

            return c;
        }
};

int main() {
    RegularFalsi regularFalsi;

    double root = regularFalsi.ruglarFalsi();  
    cout << "Root: " << root << endl;

    return  0;
}