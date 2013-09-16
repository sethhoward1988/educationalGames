from ..BaseController import *
from google.appengine.api import mail

class PublicContact(BaseHandler):
    def get(self):
        self.route('/templates/public/publicContact.html', True)

    def post(self):
        body = re.escape(self.request.get('body'))
        mail.send_mail(sender= self.request.get('name') + " <" + self.request.get('sender_email') + ">",
              to="Seth Howard <smiles.seth@gmail.com>",
              subject="Learning Center Feedback",
              body= body)

        self.route('/templates/public/publicContactSuccess.html', True)