#include <iostream>
#include <stdlib.h>
#include <time.h>

long long randint(long long a, long long b)
{
    return a + rand() % (b - a + 1);
}

int main()
{
    std::cin.sync_with_stdio(false);
    std::cin.tie(nullptr);
    srand(time(NULL));

    // Type your random testcase generator here
}