T = int(input()) 

for _ in range(T):
    h, l = map(int, input().split())#h층수 l컨베길이
    cust_order = []#손님번호 저장
    car_pos = {}#차번호 저장 딕셔너리

    for i in range(h):  #층마다 반복
        f = list(map(int, input().split()))  # 층마다 차번호입력
        for j in range(l):  # 컨베 돌아가는거
            if f[j] != -1:  # 차 있을때, -1==없음
                cust_order.append(f[j])  # 차번호 저장
                car_pos[f[j]] = (i + 1, j + 1)  # 차 위치 저장 1부터

    cust_order.sort()  # 선착순으로 정렬

    hh = [1] * (h + 1)  # 층마다 엘베위치 1번부터 start
    result = 0  # 결과값 누적변수

    for num in cust_order:  # 번호순으로 차꺼냄
        floor_num, pos = car_pos[num]  #차있는 층번호&위치

        result += abs(1 - floor_num) * 20  #층부터 차있는곳까지 걸리는 초(20)

        elevator_pos = hh[floor_num]  # 엘베위치
        clockwise = abs(elevator_pos - pos)  #시계방향
        clockwise2 = l - clockwise  # 반시계방향
        move_time = min(clockwise, clockwise2) * 5 #최소*5는 벨트 이동시간
        result += move_time  # 이동 시간 추가

        hh[floor_num] = pos  # 해당 층의 엘베 위치를 현재 차량 위치로 바꿈

    print(result)  #결과
