
from odoo import models, fields, api

class mtracker(models.Model):
    _name = 'mtracker.mtracker'
    _description = 'Money Tracker'
    _rec_name = 'sequence'

    sequence = fields.Char(string="Balance Code", required=False, readonly=True,
                           track_visibility="onchange", )
    money_amount = fields.Integer(string="Amount Of Money", required=True,)
    description = fields.Text(string='Source Of Money', required=True)
    date_money = fields.Datetime(string="Date And Time OF Money", required=True, default=fields.Datetime.now())
    type = fields.Text(compute='_Type_of_money', store=False,)

    @api.model
    def create(self, values):
        # Add code here
        values['sequence'] = self.env['ir.sequence'].next_by_code('mtracker.mtracker')
        return super(mtracker, self).create(values)

    @api.one
    @api.depends('money_amount')
    def _Type_of_money(self):
        """
        @api.depends() should contain all fields that will be used in the calculations.
        """
        if self.money_amount >0:
            self.type = 'Income'
        else:
            self.type='Expense'
