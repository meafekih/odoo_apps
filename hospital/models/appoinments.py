from odoo import models, api, fields

class HospitalAppoinemnt(models.Model):
    _name = "hospital.appoinemnts"
    _description = "Hospital Appoinemnts"
    _inherit =['mail.thread','mail.activity.mixin']
    _rec_name='ref'

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    gender = fields.Selection(related='patient_id.gender', readonly=False)
    ref = fields.Char(string='Reference', help='This reference comes from patient ')
    appoinemnt_dt = fields.Datetime(string="Appoinment Date", default=fields.datetime.now())
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
        ('0', 'Normal'),('1', 'Low'),('2', 'High'),('3', 'Very high')
    ], string='Priority', help="Give the priority.")
    state = fields.Selection([
        ('draft', 'Draft'),('in_consultation', 'In Consultation'),('done', 'Done'),('cancel', 'Cancel')
    ], string='Status', required=True, default='draft')
    doctor_id = fields.Many2one('res.users', String='Doctor')
    appoinemnt_pharmacy_line_ids = fields.One2many('appoinemnt.pharmacy.lines', 'Appoinemnt_id', string="Appoinemnt Pharmacy Lines")
    hide_price_line = fields.Boolean(string="Hide Prices")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
     
    def object_test(self):
        self.prescription += "-New Text"
        return{
            'effect':{
                'fadeout':'slow',
                'message':'Bingoo',
                'type':'rainbow_man'
            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
    
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

class AppoinemntPharmacy(models.Model):
    _name = "appoinemnt.pharmacy.lines"
    _description ="Hospital Pharmacy Lines"

    product_id = fields.Many2one('product.template', string="product", required=True)
    price = fields.Float(string="Price", related='product_id.list_price')
    qts = fields.Integer(string="Quantity", default="1")
    Appoinemnt_id = fields.Many2one('hospital.appoinemnts', string="Appoinemnt")
