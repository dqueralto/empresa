from odoo import models, fields, api


class Proyectos(models.Model):
    _name = 'empresa.proyectos'
    cod = fields.Char('Codigo: ', required=True)
    nombre = fields.Char('Nombre: ', required=True)

    descripcion = fields.Char('Descripción: ', required=True)
    fechaini = fields.Date('Fecha de Inicio: ', required=True)
    fechafin = fields.Date('Fecha de Finalización: ', required=False)

    departamento = fields.Many2one('empresa.departamentos','Departamento: ', required=True)
    encargado = fields.Many2one('empresa.empleados','Encargado: ', required=True)

    presupuesto = fields.Integer('Presupuesto: ', required=False)



    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res

    @api.one
    def limpiar(self):
        self.cod = ""
        return True

    @api.multi

    def limpia_todo(self):
        self.cod = ""
        self.articulo = ""
        self.proveedor = ""


        done_recs = self.search([('marca', '=', 'fender')])
        done_recs.write({'marca': 'Fender'})
        return True

