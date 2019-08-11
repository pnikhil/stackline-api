import json
class Product:

    def __init__(self):
        #product_id, title, brand_id, brand_name, category_id, category_name
        self.product_id = ""
        self.title = ""
        self.brand_id = ""
        self.brand_name = ""
        self.category_id = ""
        self.category_name = ""

    @property
    def title(self):
        return self.title

    @property
    def brand_id(self):
        return self.brand_id

    @property
    def brand_name(self):
        return self.brand_name

    @property
    def category_name(self):
        return self.category_name

    @property
    def category_id(self):
        return self.category_id

    @property
    def product_id(self):
        return self.product_id

    @title.setter
    def title(self, value):
        self._title = value

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value

    @category_name.setter
    def category_name(self, value):
        self._category_name = value

    @category_id.setter
    def category_id(self, value):
        self._category_id = value

    @product_id.setter
    def product_id(self, value):
        self._product_id = value




