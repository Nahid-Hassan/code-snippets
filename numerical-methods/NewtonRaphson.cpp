#include <bits/stdc++.h>
using namespace std;

#define error .001


class Newton {
    public:
        double x, h;

    public:
        Newton() {
            x = 1.0; //initial guess
        }

        double function(double x) {
            return (x * x * x - x * x + 2);
        }

        double derivativeFunction(double x) {
            return (3 * x * x - 2 * x);
        }

        double newton() {
            double h = function(x) / derivativeFunction(x);

            while(abs(h) > error) {
                h = function(x) / derivativeFunction(x);
                x = x - h;
            }

            return x;
        }
};

int main() {
    Newton newton;
    double root = newton.newton();

    cout << root << endl;    

    return 0;
}