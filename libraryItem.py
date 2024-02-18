from abc import abstractmethod
import library

class LibraryItem(library.Library):

    def __init__(self):
        super().__init__()
        self.stockQuantity = 'none'
        self.shelfQuantity = 'none'

    
    @abstractmethod
    def borrowItem(self,*args):
        pass

    @abstractmethod
    def returnItem(self,*args):
        pass
