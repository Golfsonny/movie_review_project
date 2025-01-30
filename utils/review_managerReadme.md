[초안]
1.영화 제목, 평점, 리뷰 내용을 입력받아서 리스트에 추가 필요

[초기 코드]
def add_review(reviews):
    title = input("영화 제목을 입력하세요: ")
    try:
        rating = int(input("평점 (1-10): "))
        if not (1 <= rating <= 10):
            raise ValueError
    except ValueError:
        print("평점은 1에서 10 사이의 정수여야 합니다.")
        return
    review_text = input("리뷰 내용을 입력하세요: ")
    reviews.append({"title": title, "rating": rating, "review": review_text})
    print(f"'{title}' 리뷰가 추가되었습니다.")
[문제점]
📌 이 코드의 문제점
❌ 사용자가 평점을 1~10이 아닌 다른 숫자로 입력해도 그대로 들어감.
❌ 사용자가 실수로 숫자가 아닌 문자열을 입력하면 에러 발생 (ValueError).
❌ 예외처리가 없음 → 프로그램이 갑자기 종료될 위험이 있음.

[2안]
1. 사용자가 실수로 숫자가 아닌 값을 입력하면 프로그램이 꺼질 수 있기에, 예외처리(try-except)를 추가
2. 평점이 1~10이 아닌 값이 입력될 시, 재입력 옵션 추가

[수정 코드]
def add_review(reviews):
    title = input("영화 제목을 입력하세요: ")

    try:
        rating = int(input("평점 (1-10): "))  # 숫자로 변환 시도
        if not (1 <= rating <= 10):  # 범위를 벗어나면 ValueError 발생시킴
            raise ValueError
    except ValueError:
        print("평점은 1에서 10 사이의 정수여야 합니다.")
        return  # 함수 종료 (리뷰 추가 안 됨)

    review_text = input("리뷰 내용을 입력하세요: ")

    # 리스트에 추가
    reviews.append({"title": title, "rating": rating, "review": review_text})
    print(f"'{title}' 리뷰가 추가되었습니다.")


