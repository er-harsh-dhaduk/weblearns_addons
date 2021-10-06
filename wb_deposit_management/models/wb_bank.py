from odoo import api, fields, models, _


class WbBank(models.Model):
    _name = "wb.bank"
    _description = "Weblearns Bank Model"

    name = fields.Char("Bank Name", required=True)
    code = fields.Char("Code", default="/", required=True)
    balance = fields.Float("Balance", compute="_get_final_bank_balance")
    partner_id = fields.Many2one("res.partner", string="Address")

    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code("wb.bank")
        #Auto generate sequence for the bank profile.
        return super(WbBank, self).create(vals)

    def _get_final_bank_balance(self):
        tran_obj = self.env['wb.bank.transactions']
        for record in self:
            all_transactions = tran_obj.search([('bank_id','=',record.id),('state','=','done')])
            all_deposit = sum(all_transactions.filtered(lambda lm:lm.tran_state == 'deposit').mapped("balance"))
            all_withdraw = sum(all_transactions.filtered(lambda lm:lm.tran_state == 'withdraw').mapped("balance"))
            record.balance = (all_deposit - all_withdraw) or 0.00

    _sql_constraints = [
        ('unique_weblearns_bank', 'unique(name)', 'Please provide unique bank name.'),
    ]