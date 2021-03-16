#include <iostream>
#include <math.h>
#include <fstream>
#include <iomanip>

using namespace std;

float fRiemmanForward(float s, int n)
{
    float sum = 0;
    for (int k = 1; k <= n; k++)
    {
        sum += 1.0 / pow(k, s);
    }
    return sum;
}

double dRiemmanForward(double s, int n)
{
    double sum = 0;
    for (int k = 1; k <= n; k++)
    {
        sum += 1.0 / pow(k, s);
    }
    return sum;
}

float fDirichletForward(float s, int n)
{
    float sum = 0;
    for (int k = 1; k <= n; k++)
    {
        sum += pow(-1.0, k - 1.0) / pow(k, s);
    }
    return sum;
}

float dDirichletForward(float s, int n)
{
    double sum = 0;
    for (int k = 1; k <= n; k++)
    {
        sum += pow(-1.0, k - 1.0) / pow(k, s);
    }
    return sum;
}

float fRiemmanBackward(float s, int n)
{
    float sum = 0;
    for (int k = n; k >= 1; k--)
    {
        sum += 1.0 / pow(k, s);
    }
    return sum;
}

double dRiemmanBackward(double s, int n)
{
    double sum = 0;
    for (int k = n; k >= 1; k--)
    {
        sum += 1.0 / pow(k, s);
    }
    return sum;
}

float fDirichletBackward(float s, int n)
{
    float sum = 0;
    for (int k = n; k >= 1; k--)
    {
        sum += pow(-1.0, k - 1.0) / pow(k, s);
    }
    return sum;
}

float dDirichletBackward(float s, int n)
{
    double sum = 0;
    for (int k = n; k >= 1; k--)
    {
        sum += pow(-1.0, k - 1.0) / pow(k, s);
    }
    return sum;
}


int main() {
    int n[5] = {50,100,200,500,1000};
    float s[5] = {2, 3.6667, 5,7.2,10};
    ofstream myFile;
    myFile.open("results.csv");
    myFile << "Results for float precision. Forward\n";
    myFile << "n, 50, 100, 200, 500, 1000\n";
    myFile << "s, FORWARD, FORWARD, FORWARD, FORWARD, FORWARD\n";
    for(int i = 0;i < 5;i++){
        myFile << setprecision(5) << s[i];
        for(int j = 0;j < 5;j++)
        {
            myFile << "," << setprecision(11) << fDirichletForward(s[i], n[j]); 
        }
        myFile << "\n";
    }
    myFile << "\n";
    myFile << "Results for float precision. Backward\n";
    myFile << "n, 50, 100, 200, 500, 1000\n";
    myFile << "s, BACKWARD, BACKWARD, BACKWARD, BACKWARD, BACKWARD\n";
    for(int i = 0;i < 5;i++){
        myFile << setprecision(5) << s[i];
        for(int j = 0;j < 5;j++)
        {
            myFile << "," << setprecision(11) << fDirichletBackward(s[i], n[j]); 
        }
        myFile << "\n";
    }


    myFile << "\n";
    myFile << "Results for double precision. Forward\n";
    myFile << "n, 50, 100, 200, 500, 1000\n";
    myFile << "s, FORWARD, FORWARD, FORWARD, FORWARD, FORWARD\n";
    for(int i = 0;i < 5;i++){
        myFile << setprecision(5) << s[i];
        for(int j = 0;j < 5;j++)
        {
            myFile << "," << setprecision(11) << dDirichletForward(s[i], n[j]); 
        }
        myFile << "\n";
    }


    myFile << "\n";
    myFile << "Results for double precision. Backward\n";
    myFile << "n, 50, 100, 200, 500, 1000\n";
    myFile << "s, BACKWARD, BACKWARD, BACKWARD, BACKWARD, BACKWARD\n";
    for(int i = 0;i < 5;i++){
        myFile << setprecision(5) << s[i];
        for(int j = 0;j < 5;j++)
        {
            myFile << "," << setprecision(11) << dDirichletBackward(s[i], n[j]); 
        }
        myFile << "\n";
    }

    myFile.close();

}