#include <iostream>
#include <algorithm>
#include <string>
#include <cstdlib>
#include <ctime>

void randomize_string(std::string &str)
{
    int len = str.length();
    for(int x = len; x > 0; x--)
    {
        int position = std::rand()%len;
        char tmp = str[x-1];
        str[x-1] = str[position];
        str[position] = tmp;
    }
}

bool bogosort(std::string str, std::string str2)
{
    randomize_string(str);
    if(str.compare(str2) != 0){
        return false;
    } else {
        return true;
    }
}

int main(int argc, const char **argv)
{
    std::string jumbled = argv[1];
    std::string sorted = argv[2];
    std::srand(time(NULL));
    int counter = 0;
    while(bogosort(jumbled, sorted) != true){
        counter++;
    }

    std::cout << counter << " iterations\n";
    return 0;
}
