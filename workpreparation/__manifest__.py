# Workpreparation module FDSO

{
    'name': 'Workpreparation',
    'version': '0.1',
    'sequence': 12,
    'author': "FDSO",
    'category':"MRP and PLM",
    'summary': 'Prepares products for mass production',
    'description': "",
    'depends': [
         'base_setup',
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/prep_npi_views.xml',
        'views/prep_menu_views.xml',
    ],
}