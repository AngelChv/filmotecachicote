# -*- coding: utf-8 -*-
from odoo import models, fields


class genero(models.Model):
    _name = "filmotecachicote.genero"
    _description = "filmotecachicote.genero"

    name = fields.Char(string="Nombre", read_only=False, required=True, help="Nombre del género.")
    description = fields.Text(string="Descripción")

    peliculas_id = fields.One2many(String = "Películas", comodel_name="filmotecachicote.pelicula", inverse_name="genero_id")