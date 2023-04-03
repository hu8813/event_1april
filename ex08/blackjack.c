#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char *cards ="23456789TJDKAQ";
    int hash[256] = {0};

    if (argc < 2)
    {
        return 1;
    }

    int sum = 0, i = 0;

    if (argv[1][0] == '\0')
        return (1);

    while (argv[1][i] != '\0')
    {
        if (strchr(cards,argv[1][i]) == NULL)
            return (1);
        hash[argv[1][i]] += 1;
        if (hash[argv[1][i]] > 4)
            return (1);
        if (argv[1][i] == 'T' || argv[1][i] == 'J' || argv[1][i] == 'Q'
            || argv[1][i] == 'D' || argv[1][i] == 'K')
        {
            sum += 10;
            if (sum == 21)
                return (printf("Blackjack!\n"),0);
            if (sum > 21)
                return (printf("%d\n",sum),0);
        }
        else if (argv[1][i] == 'A')
        {
            if (sum + 11 > 21)
            {
                sum += 1;
                if (sum == 21)
                    return (printf("Blackjack!\n"),0);
                if (sum > 21)
                    return (printf("%d\n",sum),0);
            }
            else
            {
                sum += 11;
                if (sum == 21)
                    return (printf("Blackjack!\n"),0);
                if (sum > 21)
                    return (printf("%d\n",sum),0);
            }
        }
        else if (argv[1][i] >= '2' && argv[1][i] <= '9')
        {
            sum += argv[1][i] - '0';
            if (sum == 21)
                return (printf("Blackjack!\n"),0);
            if (sum > 21)
                return (printf("%d\n",sum),0);
        }
        i++;
    }
    if (sum == 21)
    {
        printf("Blackjack!\n");
    }
    else 
    {
         printf("%d\n", sum);
    }
   
    return 0;
}
