# qa_python

## Описание тестов:
1. `test_add_new_book_valid_name` - тест метода add_new_book посредством добавления в словарь self.books_genre одной книги
2. `test_add_new_book_add_duplicate_book` - тест метода add_new_book на недопустимость добавление дубля книги
3. `test_add_new_book_ivalid_name_length` - тест метода add_new_book с невалидными данными: уже существующее название, 0 символов, больше 41 символа
4. `test_set_book_genre_existing_name_and_genre` - тест метода set_book_genre с имемеющимися именем и жанром
5. `test_set_book_genre_unknown_name_and_genre` - тест метода set_book_genre с невалидными именем и жанром
6. `test_get_book_genre_existing_name` - тест метода get_book_genre с книгой, которой был присвоен жанр
7. `test_get_book_genre_unknown_name` - тест метода get_book_genre, когда передают название отсутвутсвующей в book_genre книги
8. `test_get_book_genre_book_without_genre` - тест метода get_book_genre, когда передают название книги, которой не был присвоен жанр
9. `test_get_books_with_specific_genre_existing_genre` - тест метода get_books_with_specific_genre с валидным жанром, т.е. с жанром, который есть в списке self.genre
10. `test_get_books_with_specific_genre_unknown_genre` - тест метода get_books_with_specific_genre с невалидным жанром - жанром отсутствуеющем в списке self.genre
11. `test_get_books_genre_return_dict` - тест метода get_books_genre, возвращающего словарь self.books_genre
12. `test_get_books_for_children_return_books_accessible_for_children` - тест метода get_books_for_children на возвращение книг, который доступны для детей
13. `test_get_books_for_children_unknow_genre` - тест метода get_books_for_children на невозвращении книги с жанром, отсутсвующим в self.genre
14. `test_add_book_in_favorites_existing_book_and_unknown_in_favorites` - тест метода add_book_in_favorites на добавление книги из словаря self.book_genre и отсутствующей в списке self.favorites
15. `test_add_book_in_favorites_unknow_book_and_duplicate_book` - тест метода add_book_in_favorites на недопустимость дублирования книг в списке self.favorites и включение в список книги, отсутствующей в словаре self.book_genre
16. `test_delete_book_from_favorites_delete_existing_book` - тест метода delete_book_from_favorites на удаление книги, находящейся в списке self.favorites
17. `test_delete_book_from_favorites_delete_unknow_book` - тест метода delete_book_from_favorites на невозможность удаления книги, отсутствующей в списке self.favorites
18. `test_get_list_of_favorites_books_return_favorites_books` - тест метода get_list_of_favorites_books на возврат списка self.favorites