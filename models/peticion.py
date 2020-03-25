# -*- coding: utf-8 -*-

from odoo import models, fields,api
from datetime import datetime, timedelta

class FruteriaPeticion(models.Model):
    _name = 'fruteria.peticion'
    _description = 'Peticion fruteria'

    id_socio = fields.Many2one('fruteria.socio', string='ID Socio')
    fecha = fields.Date('Fecha pedido',default=datetime.now().strftime('%Y-%m-%d'),index=True)
    importeTotal = fields.Float('Importe total',compute='_calcular_importeTotal',readOnly=True)
    id_lineaPeticion = fields.One2many('fruteria.lineapeticion', ondelete="cascade", inverse_name='id_peticion')

    @api.multi
    def _calcular_importeTotal(self):
        for record in self:
            record.importeTotal=0
            for linea in record.id_lineaPeticion:
                record.importeTotal=record.importeTotal+linea.importe