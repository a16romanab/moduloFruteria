# -*- coding: utf-8 -*-

from odoo import models, fields

class FruteriaSocio(models.Model):
    _name = 'fruteria.socio'
    _description = 'Socio fruteria'

    nombre = fields.Char('Nombre', required=True,index=True)
    dni = fields.Char('DNI',required=True,index=True) 