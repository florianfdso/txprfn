from importlib.metadata import files
from itertools import product
import string
from odoo import fields, models

class PrepModel(models.Model):
    _name = "prep.product"
    _description = "Workpreparation model"

    name = fields.Char()
    description = fields.Char()
    product_id = fields.Many2one("product.template", string="Product")
    drawing_pdf = fields.Binary('ir.attachment', string="Drawing")