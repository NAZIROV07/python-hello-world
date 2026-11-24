from db.db import SessionLocal
from db.crud import get_categories, get_books


def main():
    with SessionLocal() as db:
        categories = get_categories(db)
        books = get_books(db)
        print("КНИЖНЫЙ МАГАЗИН")
        for category in categories:
            print(f"\nКатегория: {category.title}")
            print("-" * 60)

            for book in books:
                if book.category_id == category.id:
                    print(f"Название: {book.title}")
                    print(f"Описание: {book.description}")
                    print(f"Цена: {book.price} руб.")
                    print()

        print(f"Всего категорий: {len(categories)}")
        print(f"Всего книг: {len(books)}")


if __name__ == "__main__":
    main()