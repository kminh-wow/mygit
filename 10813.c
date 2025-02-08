#include <stdio.h>
#include <stdlib.h>

int main(void){
	int n,m,c,d;
	
	// ����� �Է� �ޱ�
	scanf("%d %d", &n, &m);

	// ���� �迭 �Ҵ� (n ũ��)
	int *arr_2 = (int*)malloc(sizeof(int) * n);
	if (arr_2 == NULL) {
		printf("�޸� �Ҵ� ����\n");
		return 1;
	}

		for(c = 0; c < n; c++){
		arr_2[c] = c + 1;
	}

	
	for(d = 0; d < m; d++){
		int i, j;
		scanf("%d %d", &i, &j);

		// �迭 ���� �ʰ� ����
		if(i < 1 || i > n || j < 1 || j > n){
			printf("������ ��� �Է°�: %d %d\n", i, j);
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

