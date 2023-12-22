#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <algorithm>
#include <string>
#include <cctype>
using namespace std;
bool checkLetterInVector(const vector<string>&vec,const string& str){
    auto it = find(vec.begin(),vec.end(),str);
    return it!=vec.end();
}
int main(){
    string email;
    string password;
    vector<string> emailSplit = {};
    vector<char> splitAll = {};
    cout << "Input Your Email : ";
    cin >> email;
    cout << "Input Your Password : ";
    cin >> password;
    string s;
    stringstream ss(email);
    string checkAdd = "@";
    int counter = 0;
    while(getline(ss,s,'@')){
        emailSplit.push_back(s);
    }
    for(char x : email){
        if (x == '@'){
            counter += 1;
        }
        splitAll.push_back(x);
    }
    size_t found = email.find(checkAdd);
    if (counter == 1){
        if (splitAll[0] == '6' && splitAll[1] == '6'){
            if (emailSplit[0].size() < 5){
                cout << "This email cannot be registered";
            }else if(!isdigit(splitAll[2]) || !isdigit(splitAll[3]) ||!isdigit(splitAll[4])){
                cout << "This email cannot be registered";
            }else if (email == password){
                cout << "Password must not be the same as email";
            }else{
                if ((emailSplit[1] == "preecha.ac.th" ||emailSplit[1] == "kengdee.ac.th" ||emailSplit[1] == "samart.ac.th")&& emailSplit[0].size() == 5){
                    if (password.size() >= 10){
                        cout << "Complete";
                    }else{
                        cout << "Password must be at least 10 characters";
                    }
                }else{
                    cout << "Password must be at least 10 characters";
                }
            }
        }else{
            cout << "This email cannot be registered";
        }
    }else{
        cout << "This email cannot be registered";
    }
    return 0;
}