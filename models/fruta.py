# -*- coding: utf-8 -*-

from odoo import models, fields

class FruteriaFruta(models.Model):
    _name = 'fruteria.fruta'
    _description = 'Fruta fruteria'

    nombre = fields.Char('Nombre', required=True)
    preciokg = fields.Float('Precio kg',required=True)