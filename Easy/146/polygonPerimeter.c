#include <stdio.h>
#include <math.h>

int main()
{
    int numSides;
    float circumradius; 
    printf("Enter number of sides: ");
    scanf("%d", &numSides);
    printf("Enter circumradius size: ");
    scanf("%f", &circumradius);

    float oneSide, perimeter;

    oneSide = circumradius * (2 * sin(M_PI/numSides));
    perimeter = oneSide * numSides;
    printf("%6.3f\n", perimeter);
}
