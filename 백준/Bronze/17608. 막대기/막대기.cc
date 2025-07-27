#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int s[100000];
    
    for (int i=0; i<n; i++) {
        scanf("%d", &s[i]);
    }

    int v = 0;
    int m = 0;

    for (int i =n-1; i >= 0; i--) {
        if (s[i] > m) {
            v++;
            m = s[i];
        }
    }

    printf("%d\n", v);
    return 0;
}