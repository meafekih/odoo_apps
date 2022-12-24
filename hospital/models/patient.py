from odoo import models, api, fields
from datetime import date

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    _inherit =['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    date_birth = fields.Date(string='Date of Birth')
    age =  fields.Integer(string='Age', compute='_compute_age', tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender')
    ref = fields.Char(string='Reference')
    active = fields.Boolean(string="Active", default=True)
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag', string="Tags")


    @api.depends('date_birth')
    def _compute_age(self):
        this_year = date.today().year
        for rec in self:
            if rec.date_birth:
                rec.age = this_year - rec.date_birth.year
            else:
                rec.age = 0






