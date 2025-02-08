#include <stdio.h>
#include <stdlib.h>

int n,m;

int main(void){
	
	scanf("%d %d", &n, &m);
	int *arr_2;
	arr_2 = (int*)malloc(sizeof(int)*n);
	int c,d,i,j;
	for(c=0; c<n; c++){
		arr_2[c] = c+1;
	}
	for(d=0; d<m; d++){
		scanf("%d %d", &i, &j);
		int temp = arr_2[i-1];
		arr_2[i-1] = arr_2[j-1];
		arr_2[j-1] = temp;
	}
	for(c=0; c<n; c++){
		printf("%d ", arr_2[c]);
	}
	
	

    return 0;
}
