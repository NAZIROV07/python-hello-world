from .models import Category, Book


#CRUD для категорий

def create_category(db, title):
    category = Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def get_categories(db):
    return db.query(Category).all()


def get_category(db, category_id):
    return db.get(Category, category_id)


def update_category(db, category_id, title):
    category = get_category(db, category_id)

    if category:
        category.title = title
        db.commit()
        db.refresh(category)

    return category


def delete_category(db, category_id):
    category = get_category(db, category_id)

    if category:
        db.delete(category)
        db.commit()
        return True

    return False


#CRUD для книг

def create_book(db, title, description, price, category_id, url=None):
    book = Book(
        title=title,
        description=description,
        price=price,
        category_id=category_id,
        url=url
    )

    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_books(db):
    return db.query(Book).all()


def get_book(db, book_id):
    return db.get(Book, book_id)


def update_book(db, book_id, **kwargs):
    book = get_book(db, book_id)

    if book:
        for key, value in kwargs.items():
            if key in ("title", "description", "price", "url", "category_id"):
                setattr(book, key, value)

        db.commit()
        db.refresh(book)

    return book


def delete_book(db, book_id):
    book = get_book(db, book_id)

    if book:
        db.delete(book)
        db.commit()
        return True

    return False