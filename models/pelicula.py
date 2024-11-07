# -*- coding: utf-8 -*-
from odoo import models, fields


class pelicula(models.Model):
    # Los nombres de los modelos son: "nombre módulo"."nombre clase"
    # Es un campo obligatorio.
    _name = "filmotecachicote.pelicula"
    _description = "filmotecachicote.pelicula"

    # Campos:
    code = fields.Char(string="Código", compute="_get_code")
    name = fields.Char(string="Nombre", read_only=False, required=True, help="Nombre de la película")
    description = fields.Text(string="Descripción")
    film_date = fields.Date(string="Fecha")
    start_date = fields.Datetime()
    end_date = fields.Datetime(compute="_get_end_date", store=True)
    is_spanish = fields.Boolean(string="Española")
    image = fields.Image(string="Cartel", help="Cartel de la película", widget="image")
    language = fields.Selection(
        selection=[
            ('en', 'Inglés'),
            ('es', 'Español'),
            ('fr', 'Francés'),
            ('de', 'Alemán'),
        ],
        string="Idioma",
        help="Idioma de la película",
        default="es",
    )
    opinion = fields.Selection(
        selection=[
            ("0", "mala"),
            ("1", "regular"),
            ("2", "buena"),
        ],
        string="Opinión",
        help="Opinión de la película",
        default="1",
    )
    color = fields.Boolean(string="Color", default=True)

    # Relaciones:
    genero_id = fields.Many2one("filmotecachicote.genero", string="Género", required=True, ondelete="cascade")
    tecnicas_id = fields.Many2many("filmotecachicote.tecnica", string="Técnica", ondelete="cascade",
                                   relation="tecnicas_pelicula",
                                   column1="tecnicas_ids",
                                   column2="peliculas_ids")


    # Métodos:
    # self en este caso no se refiere a sí mismo (una película) sino a toda la lista de películas.
    def _get_code(self):
        for pelicula in self:
            if len(pelicula.genero_id) == 0:
                pelicula.code = f"FILM_{pelicula.id}"
            else:
                pelicula.code = f"{pelicula.genero_id.name.upper()}_{pelicula.id}"