from odoo import models, api, fields

class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active")
    color = fields.Integer(string="Color")
    color2 = fields.Char(string="Color2")
