from odoo import models, fields, api


class Departamentos(models.Model):
    _name = 'empresa.departamentos'
    cod = fields.Char('Codigo: ', required=True)
    nombre = fields.Char('Nombre: ', required=True)
    descripcion = fields.Char('Descripción: ', required=True)
    extensiontlf = fields.Integer('Extensión Telefonica: ', required=True)
    email = fields.Char('Email: ', required=True)


    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res

    @api.one
    def limpiar(self):
        self.cif = ""
        return True

    @api.multi
    def limpia_todo(self):

        #done_recs = self.search([('marca', '=', 'fender')])
        #done_recs.write({'marca': 'Fender'})
        return True
    
