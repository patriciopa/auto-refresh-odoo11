# -*- coding: utf-8 -*-

from odoo import api, fields, models


class RefreshCRM(models.Model):
    _inherit = ['crm.lead']
     
    @api.model
    def create(self, vals):
        self.env['bus.bus'].sendone('auto_refresh_crm', 'refresh')
        return super(RefreshCRM, self).create(vals)
      
    @api.multi
    def write(self, vals):
        self.env['bus.bus'].sendone('auto_refresh_crm', 'refresh')
        return super(RefreshCRM, self).write(vals)
      
    @api.multi
    def unlink(self):
        self.env['bus.bus'].sendone('auto_refresh_crm', 'refresh')
        return super(RefreshCRM, self).unlink()
      

class RefreshCRMmessage(models.Model):
    _inherit = ['mail.message']
     
    @api.model
    def create(self, vals):
        if 'model' in vals:
            if vals['model'] == 'crm.lead':
                self.env['bus.bus'].sendone('auto_refresh_crm', 'refresh')
        return super(RefreshCRMmessage, self).create(vals)
      
    @api.multi
    def write(self, vals):
        if self.model == 'crm.lead':
            self.env['bus.bus'].sendone('auto_refresh_crm', 'refresh')
        return super(RefreshCRMmessage, self).write(vals)

class RefreshCRActivity(models.Model):
    _inherit = ['mail.activity']
     
    @api.model
    def create(self, vals):
        if 'res_model' in vals:
            if vals['res_model'] == 'crm.lead':
                self.env['bus.bus'].sendone('auto_refresh_crm', 'refresh')
        return super(RefreshCRActivity, self).create(vals)
      
    @api.multi
    def write(self, vals):
        if self.res_model == 'crm.lead':
            self.env['bus.bus'].sendone('auto_refresh_crm', 'refresh')
        return super(RefreshCRActivity, self).write(vals)      