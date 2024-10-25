# -*- coding: utf-8 -*-
# from odoo import http


# class Filmotecachicote(http.Controller):
#     @http.route('/filmotecachicote/filmotecachicote', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/filmotecachicote/filmotecachicote/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('filmotecachicote.listing', {
#             'root': '/filmotecachicote/filmotecachicote',
#             'objects': http.request.env['filmotecachicote.filmotecachicote'].search([]),
#         })

#     @http.route('/filmotecachicote/filmotecachicote/objects/<model("filmotecachicote.filmotecachicote"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('filmotecachicote.object', {
#             'object': obj
#         })
