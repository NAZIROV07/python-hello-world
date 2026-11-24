from db.db import Base, engine, SessionLocal
from db.crud import (
    create_category,
    create_book,
    get_categories,
    get_books
)


def init_db():
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        categories = {
            "Программирование": [
                ("Изучаем Python", "Основы языка Python", 1500),
                ("Чистый код", "Принципы написания кода", 1800),
                ("Совершенный код", "Разработка программ", 2200),
                ("Грокаем алгоритмы", "Алгоритмы и структуры данных", 1300)
            ],
            "Художественная литература": [
                ("1984", "Роман-антиутопия", 700),
                ("Мастер и Маргарита", "Роман Михаила Булгакова", 900),
                ("Маленький принц", "Философская сказка", 500),
                ("Алхимик", "Роман Пауло Коэльо", 650)
            ]
        }

        existing_categories = {
            category.title: category
            for category in get_categories(db)
        }

        existing_books = {
            (book.title, book.category_id)
            for book in get_books(db)
        }

        for category_title, books in categories.items():
            category = existing_categories.get(category_title)

            if category is None:
                category = create_category(db, category_title)

            for title, description, price in books:
                if (title, category.id) not in existing_books:
                    create_book(
                        db,
                        title=title,
                        description=description,
                        price=price,
                        category_id=category.id
                    )

        print("База данных успешно заполнена")


if __name__ == "__main__":
    init_db()