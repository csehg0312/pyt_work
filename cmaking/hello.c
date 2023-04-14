#include <stdio.h>
#include <string.h>

int main() {
    int array1[2] = {1, 2};
    int array2[2] = {3, 4};
    int array3[2] = {5, 6};
    int array4[2] = {7, 8};

    int array2d[4][2] = {array1, array2, array3, array4};
    int i;
    int j;

    // Print the 2-dimensional array
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 2; j++) {
            printf("%d ", array2d[i][j]);
        }
        printf("\n");
    }

    return 0;
}



