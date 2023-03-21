'''
각 유저는 한번 한명 신고 
서로 다른 유저 신고 가능 
동일 유저 신고 횟수 1회처리 
k번 이상 신고받으면 게시판 이용 정지 
해당 신고한 유저에게 메일 발송 

신고한 것을 모음 (여러개이면 1개로 처리 )
k번 이상이면 정지처리
메일 발송 
각 유저별로 신고를 한 사람이 받은 신고 횟수를 출력 
'''
from collections import defaultdict

def solution(id_list, report,k):
    answer = []
    # 중복 신고 제거
    report = list(set(report))
    # user별 신고한 id 저장
    user = defaultdict(set)
    # user별 신고당한 횟수 저장
    cnt = defaultdict(int)
	
    for r in report:
        # report의 첫번째 값은 신고자id, 두번째 값은 신고당한 id
        a,b = r.split()
        # 신고자가 신고한 id 추가
        user[a].add(b)
        # 신고당한 id의 신고 횟수 추가
        cnt[b] += 1
    
    for i in id_list:
        result = 0
        # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        for u in user[i]:
            if cnt[u]>=k:
                result +=1
        answer.append(result)
    return answer