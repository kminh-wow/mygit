def custom_replace(s, old, new):
    result = ""
    i = 0
    old_len = len(old)
    
    while i < len(s):
        # old 문자열이 현재 위치부터 일치하면 new로 변경
        if s[i:i+old_len] == old:
            result += new
            i += old_len  # old의 길이만큼 건너뛰기
        else:
            result += s[i]
            i += 1  # 한 글자씩 이동

    return result

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = custom_replace(word,i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))