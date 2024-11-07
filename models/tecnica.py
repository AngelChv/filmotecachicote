# -*- coding: utf-8 -*-
from odoo import models, fields


class tecnica(models.Model):
    _name = "filmotecachicote.tecnica"
    _description = "filmotecachicote.tecnica"

    name = fields.Char(string="Nombre", read_only=False, required=True, help="Nombre de la técnica.")
    description = fields.Text(string="Descripción")

    peliculas_id = fields.Many2many(String="Películas", comodel_name="filmotecachicote.pelicula", ondelete="cascade",
                                    relation="tecnicas_pelicula",
                                    column1="peliculas_ids",
                                    column2="tecnicas_ids")
