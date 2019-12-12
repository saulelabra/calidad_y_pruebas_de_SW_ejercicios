#include <iostream>

using namespace std;

float evaluatePoli(float *a,float x, int n) {
    float evaluated = a[n];

    for(int i=n; i>=0; i--)
    {
        evaluated = evaluated*x;
        evaluated += a[i-1];
    }

    return evaluated;
}

int main() {
    float array [4] = {1,2,3,4};

    float result = evaluatePoli(array, 1, 3);

    cout << "Evaluated: " << result << endl;

    return 0;
}