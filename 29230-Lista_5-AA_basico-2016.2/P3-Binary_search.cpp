#include<stdio.h>

int binarySearch(int *array, int element, int right) {
    int left = 0;

    while (left <= right) {
        int middle = (left + right) / 2;
        if(array[middle] == element) {
            return middle;
        } else {
            if (array[middle] < element) {
                left = middle + 1;
            }else {
                right = middle - 1;
            }
        }
    }

    return -1;
}

int main() {
    int n, q;

    scanf("%d %d", &n, &q);

    int array [n];


    for (int i = 0; i < n; i++){
        scanf("%d", &array[i]);
    }

    int element;
    for (int i = 0; i < q; i++){
        scanf ("%d", &element);
        printf("%d\n", binarySearch(array, element, n));
    }
    return 0;
}






















