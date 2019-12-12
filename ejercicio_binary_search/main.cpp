#include <iostream>
#include <vector>

using namespace std;

int binarySearch(vector<int> arr, int lookFor) {
    int start = 0;
    int end = arr.size();

    while(start<=end) {
        int midPivot = (start+end)/2;

        cout << "Inicio: " << start << endl;
        cout << "Final: " << end << endl;
        cout << "Pivote: " << midPivot << endl;
        cout << "Elemento en pivote: " << arr[midPivot] << endl;

        if(arr[midPivot] == lookFor) {
            return midPivot;
        }else{
            if(arr[midPivot]<lookFor) {
                start = midPivot + 1;
            }else{
                if(arr[midPivot] > lookFor) {
                    end = midPivot - 1;
                }
            }
        }
    }
    return -1;
}

int main() {
    vector<int> test;
    
    for(int i=0; i<49; i++) {
        test.push_back(i);
    }

    binarySearch(test, 49);

    return 0;
}