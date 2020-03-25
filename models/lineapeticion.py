from odoo import models, fields, api
from datetime import datetime, timedelta

class FruteriaLineaPeticion(models.Model):
    _name = 'fruteria.lineapeticion'
    _description = 'Linea Peticion fruteria'

    id_fruta = fields.Many2one('fruteria.fruta')
    id_peticion = fields.Many2one('fruteria.peticion')
    kilos = fields.Integer('Kilos',required='True',index=True)
    importe = fields.Float('Importe', compute='_calcular_importe',readOnly=True)
    nombre_fruta = fields.Char('Fruta',related='id_fruta.nombre')

    @api.multi
    def _calcular_importe(self):
        for record in self:
            record.importe = record.kilos*record.id_fruta.preciokg