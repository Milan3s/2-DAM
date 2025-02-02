{
    'name': 'organizarcitas',
    'version': '1.0',
    'category': 'Servicios',
    'author': 'David Milanés Moreno',
    'website': 'https://www.tusitio.com',
    # dependencia base 
    'depends': ['base'],
    # datos predefinidos
    'data': [
        'views/reportes.xml',
        'security/groups.xml',
        'views/cita_vistas.xml',
        'security/ir.model.access.csv',
        'demo/demo.xml',
    ],
    # cargar datos de ejemplo
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
