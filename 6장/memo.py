# memo.py
# 원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장

import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
    
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)