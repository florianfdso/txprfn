from importlib.metadata import files
from odoo import fields, models

class NpiModel(models.Model):
    _name = "prep.npi"
    _description = "Workpreparation new product introduction"

    name = fields.Char()
    description = fields.Char()