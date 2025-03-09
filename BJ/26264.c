#include <stdio.h>
#include <string.h>

int main(){
    int N;
    char Answer[800001];

    scanf("%d", &N);
    scanf("%s", Answer);

    int bigdata = 0, security = 0;
    int length = strlen(Answer);

    for (int i = 0; i < length;) {
        // "bigdata" 체크 (길이 검사 추가)
        if (i <= length - 7 && strncmp(&Answer[i], "bigdata", 7) == 0) {
            bigdata++;
            i += 7;  // "bigdata" 단어 스킵
        }
        // "security" 체크 (길이 검사 추가)
        else if (i <= length - 8 && strncmp(&Answer[i], "security", 8) == 0) {
            security++;
            i += 8;  // "security" 단어 스킵
        }
        else {
            i++;  // 단어가 없으면 다음 문자로 이동
        }
    }

    // 출력
    if (bigdata > security) {
        printf("bigdata?");
    }
    else if (bigdata < security) {
        printf("security!");
    }
    else {
        printf("bigdata? security!");
    }

    return 0;
    // 입력값보다 배열이 작으면 segfault 발생!!
    
}
