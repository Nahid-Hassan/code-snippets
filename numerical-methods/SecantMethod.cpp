
#include <bits/stdc++.h>
using namespace std;

#define error 0.001

class SecantMethod {
    public:
        double x0, x1;
        int counter;
    
    public:
        SecantMethod() {
            x0 = 0.0;
            x1 = 0.0;
            counter = 0;
        }
        double func(double x) {
            return (x * x * x) - (2 * x) - 5.0;
        }

        double guessValue() {
            while(func(x0) > 0.0) {
                x0 -= .5;
            }

            while(func(x1) < 0.0) {
                x1 += .5;
            }
        }

        void rootSecant() {
            guessValue();

            double x = (x0 * func(x1) - x1 * func(x0)) / (func(x1) - func(x0));
        
            while(fabs(func(x)) >= error) {
                x0 = x1;
                x1 = x;
                counter++;

                x = (x0 * func(x1) - x1 * func(x0)) / (func(x1) - func(x0));

            }
            cout << "Total iteration: " << counter << endl;
            cout << "The solution is: " << x << endl;
        }


};

int main() {
    SecantMethod obj;
    obj.rootSecant();

    return 0;
}
