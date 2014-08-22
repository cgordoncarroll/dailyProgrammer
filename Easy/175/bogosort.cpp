#include <iostream>
#include <algorithm>
#include <string>
#include <cstdlib>

void randomize_string(std::string &str)
{
    int len = str.length();
    for(int x = len; x > 0; x--)
    {
        int position = rand()%x;
        char tmp = str[x-1];
        str[x-1] = str[position];
        str[position] = tmp;
    }
}

void bogosort(std::string str, std::string str2, int &counter)
{
    randomize_string(str);
    if(str.compare(str2) != 0){
        counter++;
        bogosort(str, str2, counter);
    }
}

int main(int argc, const char **argv)
{
    std::string jumbled = argv[1];
    std::string sorted = argv[2];
    
    int counter = 0;
    bogosort(jumbled, sorted, counter);

    std::cout << counter << " iterations\n";
}
