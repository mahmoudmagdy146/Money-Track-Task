# -*- coding: utf-8 -*-
from odoo import http

# class Mtracker(http.Controller):
#     @http.route('/mtracker/mtracker/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mtracker/mtracker/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mtracker.listing', {
#             'root': '/mtracker/mtracker',
#             'objects': http.request.env['mtracker.mtracker'].search([]),
#         })

#     @http.route('/mtracker/mtracker/objects/<model("mtracker.mtracker"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mtracker.object', {
#             'object': obj
#         })