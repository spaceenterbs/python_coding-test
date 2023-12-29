print("coding")
print("test")
print("python")


def solution(n):
    count = 0

    # 반복문 1 : n^2번 연산 수행
    for i in range(n):
        for j in range(n):
            count += 1

    # 반복문 2 : n번 연산 수행
    for k in range(n):
        count += 1

    # 반복문 3 : 2n 연산 수행
    for i in range(2 * n):
        count += 1

    # 반복문 4 : 5번 연산 수행
    for i in range(5):
        count += 1

    print(count)  # 59(n이 6일 때, 6^2 + 6 + 2*6 + 5 = 59)


solution(6)  # 함수 호출

# 톺아보다(in-depth) '샅샅이 더듬어 살피다' || '틈이 있는 곳마다 모조리 더듬어 뒤지면서 찾다'

"""markdown
1. 기록하라
2. 시험 보듯 공부하라
3. 짧은 시간 공부해서는 절대 코딩 테스트를 통과할 수 없다.
4. 나만의 언어로 요약하라
"""

# framework and wix plus I'm web

"""Python
언어를 활용할 때는 다음 내용만 기억하면 된다.
- 변수 선언하기
- 함수 정의하기
- 컨테이너 자료형 다루기
- 조건문, 반복문 사용하기
"""
