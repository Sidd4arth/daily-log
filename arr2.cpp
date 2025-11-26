#include <iostream>
using namespace std;

int main() {
    int arr[] = {2, 34, 56, 65, 1123, 234};
    int n = sizeof(arr) / sizeof(arr[0]); // size of array

    int largest = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > largest) {
            largest = arr[i];
        }
    }

    cout << "Largest value is " << largest << endl;
    return 0;
}
