#include <stdio.h>
#include <stdlib.h>

int main(void){
	int n,m,c,d;
	
	// 사용자 입력 받기
	scanf("%d %d", &n, &m);

	// 동적 배열 할당 (n 크기)
	int *arr_2 = (int*)malloc(sizeof(int) * n);
	if (arr_2 == NULL) {
		printf("메모리 할당 실패\n");
		return 1;
	}

		for(c = 0; c < n; c++){
		arr_2[c] = c + 1;
	}

	
	for(d = 0; d < m; d++){
		int i, j;
		scanf("%d %d", &i, &j);

		// 배열 범위 초과 방지
		if(i < 1 || i > n || j < 1 || j > n){
			printf("범위를 벗어난 입력값: %d %d\n", i, j);
			continue;
		}


		int temp = arr_2[i - 1];
		arr_2[i - 1] = arr_2[j - 1];
		arr_2[j - 1] = temp;
	}


	for(c = 0; c < n; c++){
		printf("%d ", arr_2[c]);
	}
	


	free(arr_2);

    return 0;
}

