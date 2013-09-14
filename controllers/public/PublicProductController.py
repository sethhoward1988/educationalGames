from ..BaseController import *

class PublicProduct(BaseHandler):
    def get(self):
        self.route('/templates/public/publicProduct.html', True)