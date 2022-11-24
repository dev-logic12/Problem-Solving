def solution(score):
    평균 = [(i + j)/2 for i, j in score]
    정렬된점수 = sorted(평균, reverse=True)
    return [i+1 for i in list(map(정렬된점수.index, 평균))]