from odoo import models, fields, api


class Empleados(models.Model):
    _name = 'empresa.empleados'
    dni = fields.Char('DNI: ', required=True)
    nombre = fields.Char('Nombre Completo: ', required=True)
    departamento = fields.Many2one('empresa.departamentos','Departamento: ', required=False)
    salario = fields.Integer('Salario', required=False)


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

        #done_recs = self.search([('marca', '=', 'fender')])
        #done_recs.write({'marca': 'Fender'})
        return True
    
