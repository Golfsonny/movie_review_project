# 리뷰 추가
def add_review(reviews):
    title = input("영화 제목을 입력하세요: ")
    try:
        rating = int(input("평점 (1-10): "))
        if not (1 <= rating <= 10):
            raise ValueError
            
    #범위밖 입력 예외처리
    except ValueError:
        print("평점은 1에서 10 사이의 정수여야 합니다.")
        return
    review_text = input("리뷰 내용을 입력하세요: ")
    reviews.append({"title": title, "rating": rating, "review": review_text})
    print(f"'{title}' 리뷰가 추가되었습니다.")

# 리뷰 삭제
def delete_review(reviews, title):
    for review in reviews:
        if review["title"].lower() == title.lower():
            reviews.remove(review)
            #리스트에서 첫 번째로 일치하는 항목을 제거
            print(f"'{title}' 리뷰가 삭제되었습니다.")
            return
    print(f"'{title}' 리뷰를 찾을 수 없습니다.")

# 리뷰 검색
def search_reviews(reviews, keyword):
    results = [review for review in reviews if keyword.lower() in review["title"].lower()]
    return results

# 리뷰 정렬 (평점순)
def sort_reviews_by_rating(reviews):
    return sorted(reviews, key=lambda x: x["rating"], reverse=True)
