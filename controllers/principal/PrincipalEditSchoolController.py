from ..BaseController import *

class PrincipalEditSchool(BaseHandler):
    def get(self):
        user = users.get_current_user()
        role = self.getCurrentUserRole(user)
        try:
            self.goHome(role[0])
        except:
            self.route("/templates/public/publicHome.html", True)