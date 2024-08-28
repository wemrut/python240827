# ChatGpt로 생성한 이메일주소체크.py

import re

def is_valid_email(email):
    """
    주어진 이메일 주소가 유효한지 검사하는 함수.
    :param email: 검사할 이메일 주소.
    :return: 유효한 이메일이면 True, 그렇지 않으면 False.
    """
    # 이메일 주소의 유효성을 검사하기 위한 정규식 패턴
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # 정규식 패턴에 매칭되는지 확인
    if re.match(email_regex, email):
        return True
    else:
        return False

# 샘플 이메일 주소 리스트
email_samples = [
    "valid.email@example.com",    # 올바른 이메일 형식
    "another.valid-email@example.co.uk",  # 올바른 이메일 형식
    "invalid-email@example",      # 도메인에 .이 없음 (잘못된 형식)
    "missing_at_symbol.com",      # @ 기호가 없음 (잘못된 형식)
    "user@domain_with_underscore.com",  # 도메인에 언더스코어가 있음 (잘못된 형식)
    "user.name@domain.com",       # 올바른 이메일 형식
    "user+name@domain.com",       # 올바른 이메일 형식 (플러스 기호 허용)
    "user@sub.domain.com",        # 올바른 이메일 형식 (서브 도메인 포함)
    "user@domain.c",              # 도메인 끝이 너무 짧음 (잘못된 형식)
    "plainaddress",               # 이메일 형식이 아님 (잘못된 형식)
]

# 이메일 유효성 검사 결과 출력
for email in email_samples:
    print(f"{email}: {is_valid_email(email)}")
