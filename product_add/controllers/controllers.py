# -*- coding: utf-8 -*-
from odoo import http

# class ProductAdd(http.Controller):
#     @http.route('/product_add/product_add/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_add/product_add/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_add.listing', {
#             'root': '/product_add/product_add',
#             'objects': http.request.env['product_add.product_add'].search([]),
#         })

#     @http.route('/product_add/product_add/objects/<model("product_add.product_add"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_add.object', {
#             'object': obj
#         })