
import web
from gothonweb import gothon_map
from zombie import zombie_map

urls = (
  '/', 'Home',
  '/zombie', 'Zombie',
  '/zombie_game', 'ZombieGameEngine',
  '/gothon_game', 'GothonGameEngine',
  '/gothon', 'Gothon',
)

app = web.application(urls, globals())

if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store,
                                  initializer={'room': None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="layout")


class Home(object):
    def GET(self):
        return render.home()


class Zombie(object):
    def GET(self):
        session.room = zombie_map.START
        web.seeother("/zombie_game")


class ZombieGameEngine(object):
    def GET(self):
        if session.room:
            return render.zombie.zombie_theme(render.zombie.show_room
                                              (room=session.room))

        return render.zombie.zombie_theme(render.zombie.you_died())

    def POST(self):
        form = web.input(action=None)
        form.action = form.action.lower()

        if session.room or form.action:
            session.room = session.room.go(form.action)

        web.seeother("/zombie_game")


class Gothon(object):
    def GET(self):
        session.room = gothon_map.START
        web.seeother("/gothon_game")


class GothonGameEngine(object):
    def GET(self):
        if session.room:
            return render.gothon.gothon_theme(render.gothon.show_room
                                              (room=session.room))

        return render.gothon.gothon_theme(render.gothon.you_died())

    def POST(self):
        form = web.input(action=None)
        form.action = form.action.lower()

        if session.room or form.action:
            session.room = session.room.go(form.action)

        web.seeother("/gothon_game")

if __name__ == "__main__":
    app.run()
