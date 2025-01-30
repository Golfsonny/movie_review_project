from utils.file_handler import load_reviews_from_csv, save_reviews_to_csv
from utils.review_manager import add_review, delete_review, search_reviews, sort_reviews_by_rating

FILE_PATH = "data/reviews.csv"

def main():
    reviews = load_reviews_from_csv(FILE_PATH)

    while True:
        print("\n영화 리뷰 관리 프로그램")
        print("1. 리뷰 추가")
        print("2. 리뷰 삭제")
        print("3. 리뷰 검색")
        print("4. 리뷰 정렬 (평점순)")
        print("5. 리뷰 저장 및 종료")
        
        choice = input("선택: ")
        
        if choice == "1":
            add_review(reviews)
        elif choice == "2":
            title = input("삭제할 영화 제목: ")
            delete_review(reviews, title)
        elif choice == "3":
            keyword = input("검색 키워드: ")
            results = search_reviews(reviews, keyword)
            print("검색 결과:")
            for r in results:
                print(f"- {r['title']} ({r['rating']}점): {r['review']}")
        elif choice == "4":
            sorted_reviews = sort_reviews_by_rating(reviews)
            print("평점순 정렬:")
            for r in sorted_reviews:
                print(f"- {r['title']} ({r['rating']}점): {r['review']}")
        elif choice == "5":
            save_reviews_to_csv(FILE_PATH, reviews)
            print("리뷰가 저장되었습니다. 프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택하세요.")

if __name__ == "__main__":
    main()
