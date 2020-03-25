# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime, timedelta

class FruteriaPeticion(models.Model):
    _name = 'fruteria.peticion'
    _description = 'Peticion fruteria'

    fecha = fields.Date('Fecha pedido',default=datetime.now().strftime('%Y-%m-%d'),index=True)
    cantidad = fields.Integer('Cantidad',required='True',index=True)