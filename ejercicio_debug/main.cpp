#include <iostream>
#include <fstream>
#include <vector>
#include <tuple>
#include <bits/stdc++.h> 

using namespace std;

float union2D(vector<tuple<float,float>> list) {
    
    sort(list.begin(), list.end(),greater<tuple<float,float>>());

    for(int i=0; i<list.size(); i++)
    {
        cout << get<0>(list[i]) << " " << get<1>(list[i]) << endl;
    }
    
    float maxY = 0;
    float totalArea = 0;
    float newArea = 0;

    totalArea = get<0>(list[0]) * get<1>(list[0]);
    maxY = get<1>(list[0]);

    for(int i=1; i<list.size(); i++)
    {
        if(get<1>(list[i]) > maxY)
        {
            newArea = get<0>(list[i]) * (get<1>(list[i]) - maxY);
            maxY = get<1>(list[i]);
            totalArea += newArea;
        }
    }

    return totalArea;
}

int main() {
    ifstream file("2_test.txt");

    vector<tuple<float,float>> points;

    //reading points from file
    while(!file.eof())
    {
        int num1, num2;
        file >> num1 >> num2;
        tuple<float,float> curTuple = make_tuple(num1, num2);
        points.push_back(curTuple);
    }

    float result = union2D(points);

    cout << result << endl;
}