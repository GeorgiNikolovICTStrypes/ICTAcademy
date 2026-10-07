from base_scraper import Scraper

class BookScraper(Scraper):
    def __init__(self):
        self.index_url = 'https://books.toscrape.com/'
        self.categories_and_nums = None
    def fetch_info_for_books_with_rating(self, rating):
        """
        Args:
          rating (int): Number in range 1-5.
        Fetches book info for all books with passed rating
        Output:
          (list of lists) book info in the format [book_title, book_url, book_pric , book_availability]
        """
        while not (1 <= rating <= 5):
            try:
                rating = int(input("Please enter a vaid number in the range 1-5. "))
            except:
                continue

        base_rating = ".star-rating."
        match rating:
            case 1:
                rating_tag = base_rating + 'One'
            case 2:
                rating_tag = base_rating + 'Two'
            case 3:
                rating_tag = base_rating + 'Three'
            case 4:
                rating_tag = base_rating + 'Four'
            case 5:
                rating_tag = base_rating + 'Five'
        
        books_info = []
        start_url = self.index_url
        curr_page = 1

        while start_url:
            print(start_url)
            data = self.fetch_data(start_url)
            books_in_page = data.select('article.product_pod')

            for book in books_in_page:
                if book.select(rating_tag)!=[]:
                    book_title =  book.select_one('h3>a')['title']
                    book_url = book.select_one('h3>a')['href']   
                    book_price = book.select_one('p.price_color').text
                    book_availability = book.select_one('p.instock.availability').text.strip()
                    books_info.append([book_title, book_url, book_price, book_availability])


            next = data.select_one('li.next>a')

            if next:
                if curr_page == 1:
                    start_url = self.index_url + next['href']
                else:
                    start_url = self.index_url + 'catalogue/' + next['href']
            else:
                start_url = None
            curr_page+=1
    
        return books_info
        
    def fetch_all_categories(self):
        """
        Fetches all book categrories, and fills the categories_and_nums dict for faster future queries.
        Output:
          (list of strings): Book categories
        """
        if self.categories_and_nums is not None:
            return self.categories_and_nums.keys()
        data = self.fetch_data(self.index_url)
        table = data.find('ul', {'class': 'nav nav-list'})
        categories = [x.text.strip() for x in table.select('a')]
        self.categories_and_nums = {category: i for category, i in list(zip(categories[1:], range(2,len(categories)+2)))}
        return categories
    
    def fetch_books_in_category(self, category):
        """
        Args:
          category (string): A book category to filter books by
        Fetches all books that are marked under category. If categories_and_nums is None, fetch_all_categories() is ran first.
        Output:
          (list of strings): Book titles under that category
        """
        if self.categories_and_nums is None:
            self.fetch_all_categories()
        num = self.categories_and_nums[category.title()]
        target_url = self.index_url + f'catalogue/category/books/{category.lower()}_{num}/index.html'
        data = self.fetch_data(target_url)
        
        books = data.select('.product_pod')
        titles = [book.select_one('h3 > a')['title'] for book in books]
        return titles
        
if __name__ == '__main__':
    with BookScraper() as scraper:
        print(scraper.fetch_info_for_books_with_rating(3))
        