# -*- coding: utf-8 -*-

from odoo import models, fields, api

class product_add(models.Model):
    _inherit = 'product.template'

    brand_ingredient_memo = fields.Text(string="品牌方辅料费用说明")
    brand_ingredient_price = fields.Float(string="品牌方辅料费用")
    brand_untaxed_cost_price = fields.Float(string="品牌方成本价-不含税")
    brand_taxed_cost_price = fields.Float(string="品牌方成本价-含税")
    brand_add_percent = fields.Float(string="品牌方加价率")
    brand_fixed_fee = fields.Float(string="品牌方固定标费")
    brand_fixed_fee = fields.Float(string="品牌方比例标费")

class ProductProductAdd(models.Model):
    _inherit = 'product.product'

    barcode = fields.Char(
        'Barcode', copy=False, oldname='ean13',default='New',
        help="International Article Number used for product identification.")


    @api.model
    def create(self, vals):
        if vals.get('barcode', 'New') == 'New':
            vals['barcode'] = self.env['ir.sequence'].next_by_code('product.product.barcode')
        return super(ProductProductAdd, self).create(vals)

class product_vendor_pricelist(models.Model):
    _inherit = 'product.supplierinfo'

    vendor_ingredient_memo = fields.Text(string="供应辅料费用说明")
    vendor_ingredient_price = fields.Float(string="供应商辅料费用")
    vendor_taxed_percent = fields.Float(string="供应商税点")
    vendor_untaxed_price = fields.Float(string="供应商出厂价-不含税")
    vendor_taxed_price = fields.Float(string="供应商出厂价-含税")

