from odoo import models, fields, api

class Cita(models.Model):
    _name = 'organizarcitas.cita'
    _description = 'Cita'

    nombre = fields.Char(string='Título', required=True, help='Escribe el nombre de la cita')
    descripcion = fields.Text(string='Descripción', help='Escribe la descripcion')
    fecha_cita = fields.Datetime(string='Fecha y Hora de la Cita', required=True , help='Escribe la fecha')
    duracion = fields.Float(string='Duración (horas)', default=1.0 , help='Selecciona la duración de la cita')
    
    estado = fields.Selection([
        ('abierta', 'Abierta'),
        ('en_progreso', 'En progreso'),
        ('por_aprobar', 'Por Aprobar'),
        ('cerrada', 'Cerrada'),
    ], string='Estado' , default='por_aprobar')
    
    usuario_id = fields.Many2one('res.users', string='Asignado a', required=True, help='se le asigna al usuario')    
    cliente_ids = fields.Many2many('organizarcitas.cliente', string='Cliente', help='id del cliente')
    servicio_ids = fields.Many2many('organizarcitas.servicio', string='Servicio', help='id del servicio')
    
    # Campo computado para mostrar los nombres de los clientes en la vista de lista
    cliente_nombres = fields.Char(string='Clientes', compute='_compute_cliente_nombres', store=True)
    
    nombre_cliente = fields.Char(string='Cliente(s)', compute='_compute_nombre_cliente', store=True, help='Escribe tu nombre...')

    @api.depends('cliente_ids')
    def _compute_cliente_nombres(self):
        for record in self:
            record.cliente_nombres = ', '.join(record.cliente_ids.mapped('nombre')) if record.cliente_ids else "Sin cliente"

class Cliente(models.Model):
    _name = 'organizarcitas.cliente'
    _description = 'Cliente'

    _rec_name = 'nombre' 
    nombre = fields.Char(string='Nombre', required=True , help='Escribe el nombre del cliente...')
    correo = fields.Char(string='Correo' , help='Escribe el correo...')
    direccion = fields.Char(string='Dirección', help='Escribe la dirección...')
    telefono = fields.Char(string='Teléfono', help='Escribe el telefono...')
    
class Servicio(models.Model):
    _name='organizarcitas.servicio'
    _description = 'Servicio'
    
    _rec_name = 'nombre' 
    nombre = fields.Char(string = 'Nombre', required=True , help='Escribe el nombre del servicio...')
    descripcion = fields.Text(string = 'Descripción' , help='Escribe la descripción...')
    precio = fields.Float(string = 'Precio', required=True , help='Escribe el precio...')
    cita_ids = fields.One2many('organizarcitas.cita', 'servicio_ids', string='Citas', help='indica el id de la cita')


