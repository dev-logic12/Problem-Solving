def solution(id_pw, db):
    result = 'fail'
    if str(id_pw) in str(db):
        result = 'login'
    elif str(id_pw[0]) in str(db):
        if id_pw[0] in [i[0] for i in db]:
            result = 'wrong pw'
    else:
        result = 'fail'
    return result
