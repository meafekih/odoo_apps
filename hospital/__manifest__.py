# -*- coding: utf-8 -*-
{
    'name': 'Hospital Managment',
    'version': '1.0.0',
    'category': 'Services/Hospital',
    'summary': 'Hospital managment system',
    'description': """ Hospital managment system """,
    'website':'www.hospital_odoo.com',
    'author': 'Fekih MA',
    'sequence':-100,
    'license':'LGPL-3',
    'depends': ['mail','product'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient.tag.csv',
        'views/menu.xml',
        'views/appoinemnts.xml',
        'views/patients.xml',
        'views/patient_tag.xml',
        'views/female_patients.xml'
    ],
    'demo': [],
    'images':['static/description/icon.png'],
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {},
}