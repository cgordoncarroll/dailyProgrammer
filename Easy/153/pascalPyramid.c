#include<stdio.h>

int main(){

    int i, j, n;
    //24 Rows maximum
    int a[25][25]={1};

    printf("Enter num of rows: ");
    scanf("%d", &n);

    printf("\n\n");

    for( i=1; i<=n; i++ ){
        
        //Put largest number of spaces at highest level
        for(j=n;j>i;j--){
            printf(" ");
        }

        for(j=1;j<=i;j++){
            //Populate Matrix Array and Print
            a[i][j] = a[i-1][j-1] + a[i-1][j];
            printf("%d ", a[i][j]);
        }

        printf("\n");
    }
    return 0;
}
