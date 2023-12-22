#include <iostream>
#include <vector>
using namespace std;
int checkDate(int day , int month){
    int date = day % 7;
    if(day < 1){
        return 200;
    }else if((month == 1 ||month == 3 ||month == 5 ||month == 7 ||month == 8 ||month == 10 ||month == 12) && day > 31){
        return 200;
    }else if((month == 4 ||month == 6 ||month == 9 ||month == 11) && day > 30){
        return 200;
    }else if(month == 2 && day > 29){
        return 200;
    }else{
        if (month == 9 || month == 12){
            return (date - 1);
        }else if (month == 1 || month == 4 || month == 7){
            return date;
        }else if (month == 10){
            return (date + 1);
        }else if (month == 5){
            return (date + 2);
        }else if (month == 2 || month == 8){
            return (date + 3);
        }else if (month == 3 || month == 11){
            return (date + 4);
        }else if (month == 6){
            return (date + 5);
        }else{
            return 200;
        }
    }
}
int main(){
    int day;
    int month;
    vector<string> dates = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
    cout << "Input Day = ";
    cin >> day;
    cout << "Input Month = ";
    cin >> month;
    int indexReturn = checkDate(day,month);
    if (indexReturn == 200){
        cout << "Error";
    }else{
        cout << dates[indexReturn];
    }
    return 0;
}
