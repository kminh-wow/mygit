#include <stdio.h>

int main() {
    int n, num, i = 0;
    scanf("%d", &n);
    num = n;

    while (1) {
        int a = n / 10;
        int b = n % 10;
        int c = (a + b) % 10;
        n = b * 10 + c;
        i++;
        
        if (n == num) {
            printf("%d\n", i);
            break;
        }
    }

    return 0;
}
