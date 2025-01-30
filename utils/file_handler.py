import csv

# CSV 파일에서 리뷰 로드
def load_reviews_from_csv(file_path):
    reviews = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    reviews.append({
                        "title": row["title"],
                        "rating": int(row["rating"]),
                        "review": row["review"]
                    })
                except ValueError:
                    print(f"잘못된 데이터 형식: {row}")
    except FileNotFoundError:
        print(f"'{file_path}' 파일을 찾을 수 없습니다. 새로 생성합니다.")
    return reviews

# 리뷰 데이터를 CSV 파일에 저장
def save_reviews_to_csv(file_path, reviews):
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "rating", "review"])
        writer.writeheader()
        writer.writerows(reviews)
