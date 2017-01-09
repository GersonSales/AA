#include<stdio.h>

int binarySearch(long int *array, long int element, long int right) {
    int left = 0;
    int backup = -1;

    while (left <= right) {
        int middle = left + (right - left) / 2;

        if(array[middle] == element) {
            backup = middle;
            right = middle -1;
        } else {
            if (array[middle] < element) {
                left = middle + 1;
            }else {
                right = middle - 1;
            }
        }
    }
    return backup;
}

int main() {
    long int n, q, result;

    scanf("%ld %ld", &n, &q);
    long int array [100000], results[500000];


    int count = 0;
    for (int i = 0; i < n; i++){
        long long int number;
        scanf("%lli", &number);
        if (number < 0){
            count++;
        }
        array[i] = number;
    }


    long long int element;
    for (int i = 0; i < q; i++) {
        scanf ("%li", &results[i]);
    }
    for (int i = 0; i < q; i ++) {
        result = binarySearch(array, results[i], n);
        printf("%ld\n", result);
    }
    return 0;
}






















