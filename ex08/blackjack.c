#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        return 1;
    }

    int sum = 0, i = 0;

    while (argv[1][i])
    {
        if (argv[1][i] == 'T' || argv[1][i] == 'J'
            || argv[1][i] == 'D' || argv[1][i] == 'K')
        {
            sum += 10;
        }
        else if (argv[1][i] == 'A')
        {
            if (sum + 11 > 21)
            {
                sum += 1;
            }
            else
            {
                sum += 11;
            }
        }
        else if (argv[1][i] >= '2' && argv[1][i] <= '9')
        {
            sum += argv[1][i] - '0';
        }
        i++;
    }
    if (sum == 21)
    {
        printf("Blackjack!");
    }
    else 
    {
         printf("%d", sum);
    }
   
    return 0;
}