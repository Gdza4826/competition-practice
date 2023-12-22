#include <iostream>
#include <vector>
using namespace std;
float convertToM(float height){
    float calcu = height / 100;
    return calcu;
}
float bmiCal(float weight , float height){
    float calculateBMI = weight / (height * height);
    return calculateBMI;
}
int main(){
    float hg;
    float wg;
    vector<float> w_arr = {};
    vector<float> h_arr = {};
    vector<float> rs_arr = {};
    int i = 0;
    int counter = 0;
    while (i == 0){
        cout << "Input Your Height = ";
        cin >> hg;
        cout << "Input Your Weight = ";
        cin >> wg;
        if (hg <= 0 || wg <= 0){
            i += 1;
        }else{
            float calM = convertToM(hg);
            h_arr.push_back(calM);
            w_arr.push_back(wg);
        }
    }
    for (int x = 0 ; x < h_arr.size(); x++){
        float calBMI = bmiCal(w_arr[x],h_arr[x]);
        rs_arr.push_back(calBMI);
    }
    for (float y : rs_arr){
        if (y< 18.5){
            counter += 1;
        }
    }
    cout << "BMI < 18.5 = " << counter;
}
