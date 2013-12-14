#!/usr/bin/env python
#-*- coding: utf-8 -*-

import web

from url import urls

web.config.debug = False
app = web.application(urls, globals()).wsgifunc()

db = web.database(dbn = "mysql", user = "faye", pw = "wufeishizhu.", 
        db = "web_test");

store = web.session.DBStore(db, "sessions")
session = web.session.Session(app, store, initializer={'login': 0})
#web.config_session = session

#render_login = web.template.render("templates/", globals = {'context':session})
render = web.template.render("templates/", globals = {'context':session})
web.template.Template.globals['render'] = render
