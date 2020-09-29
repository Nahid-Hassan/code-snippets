#include <bits/stdc++.h>
using namespace std;

double error = 0.001;
double x = 1.0;

class NewtonRaphsonMethod
{
public:
    double func(double x)
    {
        return (x * x * x) - (2 * x) - 5.0;
    }

    double calculatedDerived(double x)
    {
        return ((3 * x * x) - (x));
    }

    void calculateRoot()
    {
        double h = func(x) / calculatedDerived(x);

        while (abs(h) >= error)
        {
            h = func(x) / calculatedDerived(x);

            x = x - h;
            cout << setprecision(5) << h << "  " << x << endl;
        }

        cout << "Root: " << x << endl;
    }
};

int main()
{
    NewtonRaphsonMethod obj;
    obj.calculateRoot();

    return 0;
}
