# -*- coding: utf-8 -*-

from odoo import models, fields, api

class inv(models.Model):
     _name = 'felino.inv'

     name = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()


class felino(models.Model):
     _name = 'felino.felino'

     name = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

     @api.depends('value')
     def _value_pc(self):
         self.value2 = float(self.value) / 100

class contohsql(models.Model):
    _name = 'felino.contohsql'
    sql = ('SELECT country_id, array_agg(id) '
           'FROM res_partner '
           'WHERE active=true AND country_id IS NOT NULL '
           'GROUP BY country_id')
           