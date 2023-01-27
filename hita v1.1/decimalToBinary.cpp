#include <iostream>
#include <string>
using namespace std;

int binaryFrame[4] = {8,4,2,1};

int convert(int i)
{
    string i_s = to_string(i);
    string i_s0 = i_s[0];
    string i_s1 = i_s[1];
    int first = stoi(i_s0);
    int second = stoi(i_s1);
    return op;
}
int main()
{
    int input;
    cout << "Enter two digit decimal number to convert to 8bit binary number: ";

    here: cin >> input;
    if(input<10 || input >99)
    {
        cout << "\nEnter a two digit number you moron!!!! try again now !";
        goto here;
    }

    cout << convert(input);
    return 0;
}