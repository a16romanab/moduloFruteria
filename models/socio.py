# -*- coding: utf-8 -*-

from odoo import models, fields

class FruteriaSocio(models.Model):
    _name = 'fruteria.socio'
    _description = 'Socio fruteria'
    _inherits = {'res.partner': 'partner_id'}

    imagen_socio = fields.Binary('Imagen', related='partner_id.image')
    id_socio = fields.Integer('Id_Socio',require=True)
    partner_id = fields.Many2one('res.partner',ondelete='cascade',require=True)
    ids_peticion = fields.One2many('fruteria.peticion',inverse_name='id_socio')