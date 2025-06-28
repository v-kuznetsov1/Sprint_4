from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    # def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        # collector = BooksCollector()

        # добавляем две книги
        # collector.add_new_book('Гордость и предубеждение и зомби')
        # collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        # assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    
    def test_add_new_book_valid_name(self):
        book = BooksCollector()
        book.add_new_book('Война и мир') 
        
        assert book.books_genre == {'Война и мир': ''}


    
    def test_add_new_book_add_duplicate_book(self):
        book = BooksCollector()
        book.books_genre['Война и мир'] = ''
        book.add_new_book('Война и мир')
        
        assert book.books_genre == {'Война и мир': ''}


   
    @pytest.mark.parametrize('name', ['', 'аааааааааааааааааааааааааааааааааааааааааа'] )
    def test_add_new_book_ivalid_name_length(self, name):
        book = BooksCollector()
        book.add_new_book(name)

        assert book.books_genre == {}


    
    def test_set_book_genre_existing_name_and_genre(self):
        book = BooksCollector()
        book.books_genre['Война и мир'] = ''
        book.set_book_genre('Война и мир', 'Ужасы')
        
        assert book.books_genre == {'Война и мир': 'Ужасы'}


     
    @pytest.mark.parametrize('name, genre', [['Преступление и наказание', 'Ужасы'], ['Война и мир', 'Романы']])
    def test_set_book_genre_unknown_name_and_genre(self, name, genre):
        book = BooksCollector()
        book.books_genre['Война и мир'] = ''
        book.set_book_genre(name, genre)

        assert book.books_genre == {'Война и мир': ''}


    
    def test_get_book_genre_existing_name(self):
        book = BooksCollector()
        book.books_genre['Война и мир'] = ''
        book.set_book_genre('Война и мир', 'Ужасы')

        assert book.get_book_genre('Война и мир') == 'Ужасы'

    
    
    def test_get_book_genre_unknown_name(self):
        book = BooksCollector()
        book.books_genre['Оно'] = 'Ужасы'
        
        assert book.get_book_genre('Война и мир') == None

    
    
     
    def test_get_book_genre_book_without_genre(self):
        book = BooksCollector()
        book.books_genre['Война и мир'] = ''

        assert book.get_book_genre('Война и мир') == ''



    
    def test_get_books_with_specific_genre_existing_genre(self):
        book = BooksCollector()
        book.books_genre['Десять негретят'] = 'Детективы'
        
        assert book.get_books_with_specific_genre('Детективы') == ['Десять негретят']



    
    def test_get_books_with_specific_genre_unknown_genre(self):
        book = BooksCollector()
        book.books_genre['Война и мир'] = 'Романы'

        assert book.get_books_with_specific_genre('Романы') == []


    
    def test_get_books_genre_return_dict(self):
        book = BooksCollector()
        book.books_genre['Оно'] = 'Ужасы'

        assert book.get_books_genre() == {'Оно': 'Ужасы'}


    
    def test_get_books_for_children_return_books_accessible_for_children(self):
        book = BooksCollector()
        book.books_genre = {'Оно': 'Ужасы', 
                            'Дюна': 'Фантастика', 
                            'Десять негретят': 'Детективы',
                            'Трое в лодке, не считая собаки': 'Комедии',
                            'Мама для мамонтёнка': 'Мультфильмы'
                            }
        
        assert book.get_books_for_children() == ['Дюна', 'Трое в лодке, не считая собаки', 'Мама для мамонтёнка']


    
    def test_get_books_for_children_unknow_genre(self):
        book = BooksCollector()
        book.books_genre = {'Война и мир': 'Романы',
                            'Мама для мамонтёнка': 'Мультфильмы'
                            }

        assert book.get_books_for_children() == ['Мама для мамонтёнка']

    

    
    def test_add_book_in_favorites_existing_book_and_unknown_in_favorites(self):
        book = BooksCollector()
        book.books_genre = {'Оно': 'Ужасы', 
                            'Дюна': 'Фантастика'
                            }
        book.add_book_in_favorites('Дюна')

        assert book.favorites == ['Дюна']

    
    
    @pytest.mark.parametrize('name', ['Война и мир', 'Дюна'])
    def test_add_book_in_favorites_unknow_book_and_duplicate_book(self, name):
        book = BooksCollector()
        book.books_genre = {'Преступление и наказание': '', 'Дюна': ''}
        book.favorites = ['Дюна']
        book.add_book_in_favorites(name)

        assert book.favorites == ['Дюна']


    
    def test_delete_book_from_favorites_delete_existing_book(self):
         book = BooksCollector()
         book.favorites = ['Дюна']
         book.delete_book_from_favorites('Дюна')

         assert book.favorites == []

    
     
    def test_delete_book_from_favorites_delete_unknow_book(self):
        book = BooksCollector()
        book.favorites = ['Дюна']
        book.delete_book_from_favorites('Война и мир')

        assert book.favorites == ['Дюна']

        
    
    
    def test_get_list_of_favorites_books_return_favorites_books(self):
        book = BooksCollector()
        book.favorites = ['Дюна']

        assert book.get_list_of_favorites_books() == ['Дюна']