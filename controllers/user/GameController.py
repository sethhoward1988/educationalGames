from ..BaseController import *

class Game(BaseHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            scores = Score.query(Score.gameName == self.request.get('gameName'), Score.email == user.email()).fetch()
            print scores
            # self.response.out.write(json.dumps(scores))


    def post(self):
        user = users.get_current_user()
        score = Score()
        score.email = user.email()
        score.gameName = self.request.get('gameName')
        score.correct = float(self.request.get('correct'))
        score.peeked = float(self.request.get('peeked'))
        score.skipped = float(self.request.get('skipped'))
        score.put()

        self.response.headers['Content-Type'] = 'application/json'   
        obj = {
            'success': 'score saved'
        } 
        self.response.out.write(json.dumps(obj))