#include <iostream>
#include <cmath>
#include <iomanip>
#include <chrono>

using namespace std;
using namespace chrono;

const int N = 10000000;

float absoluteError(float expected, float approx)
{
    return abs(expected - approx);
}

float relativeError(float expected, float approx)
{
    return absoluteError(expected, approx) / expected;
}

float classicSum(float *arr, int size)
{
    float sum = 0;
    for (int i = 0; i < size; i++)
    {
        sum += arr[i];
    }

    return sum;
}

float recursiveSum(float *arr, int low, int high)
{
    if (low == high)
        return arr[low];
    int mid = (low + high) / 2;
    return recursiveSum(arr, low, mid) + recursiveSum(arr, mid + 1, high);
}

float kahan_algorithm(float *arr, int size)
{
    float sum = 0.0f;
    float err = 0.0f;
    for (int i = 0;i < size;i++)
    {
        float y = arr[i] - err;
        float temp = sum + y;
        err = (temp - sum) - y;
        sum = temp;
    }
    return sum;
}

void check_error(float* arr, int size) {
    float sum = 0;
    for(int i = 0;i < size;i++){
        sum += arr[i];
        if((i + 1) % 25000 == 0) {
            cout << "(" << i + 1 << "," << relativeError((i + 1) * 0.53125, sum) << "), ";
        }
    }
}

void measureTimes(float* arr, int size) {
    auto start = high_resolution_clock::now();
    classicSum(arr, size);
    auto stop =  high_resolution_clock::now();
    auto elapsed = duration_cast<microseconds>(stop - start); 
    cout << "Classic sum algorith took " << elapsed.count() << "ms\n";
    start = high_resolution_clock::now();
    recursiveSum(arr, 0, size - 1);
    stop =  high_resolution_clock::now();
    elapsed = duration_cast<microseconds>(stop - start); 
    cout << "Recursive algorith took " << elapsed.count() << "ms\n";
    start = high_resolution_clock::now();
    kahan_algorithm(arr, size);
    stop =  high_resolution_clock::now();
    elapsed = duration_cast<microseconds>(stop - start);
    cout << "Kahan algorithm took " << elapsed.count() << "ms\n";

}

int main()
{

    float v = 0.53125;
    cout << v << endl;
    float *arr = new float[N];
    for (int i = 0; i < N; i++)
    {
        arr[i] = v;
    }
    cout << fixed << setprecision(7);
    cout << "Testing normal method to sum arr:\n";
    cout << "Absolute Error: " << absoluteError(N * v, classicSum(arr, N)) << endl;
    cout << "Relative Error: " << relativeError(N * v, classicSum(arr, N)) << endl;

    cout << "Testing recursive method to sum arr:\n";
    cout << "Absolute Error: " << absoluteError(N * v, recursiveSum(arr, 0, N - 1)) << endl;
    cout << "Relative Error: " << relativeError(N * v, recursiveSum(arr, 0, N - 1)) << endl;

    cout << "Testing Kahan`s algorithm to sum arr:\n";
    cout << "Absolute Error: " << absoluteError(N * v, recursiveSum(arr, 0, N - 1)) << endl;
    cout << "Relative Error: " << relativeError(N * v, recursiveSum(arr, 0, N - 1)) << endl;


    cout << "Time difference\n";
    measureTimes(arr, N);

    // check_error(arr, N);



    delete[] arr;
}
