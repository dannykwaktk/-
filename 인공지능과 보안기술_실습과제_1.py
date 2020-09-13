def comb_all(arr, length):

    res = []
    for i in arr:
        if i not in res:   
                res.append(i)
    
    for i in range(len(res)):
        if length==1:
            yield res[i]
        else:
            for next in comb_all(res[i+1:len(res)], length-1):
                yield res[i]+ "," +next


arr = input("숫자를 입력하세요 : ").split()     # 문자열 변수에 숫자를 입력
length = 1                                      # nCr 중 r에 해당
result_num = 0                                  # 총 경우의 수를 세기 위함



for length in range(len(arr)+1):
    result=list(comb_all(arr, length))
    
    for i in range(len(result)):
        print("[%s]" % result[i])
        result_num += 1

print("가능한 경우의 수는 모두 %d가지 입니다." % result_num)

