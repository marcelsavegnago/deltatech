# -*- coding: utf-8 -*-
# ©  2015-2017 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details

{
    "name": "MRP Cost",
    "version": "2.0",
    "author" : "Terrabit, Dorin Hongu",
    "website": "www.terrabit.ro",
    "description": """
    
Functionalitati:
 - Calculeaza pretul de productie ca fiind pretul real al componentelor
 - Asigneaza un picking pentru materialele consumate si unul pentru cele receptionate
 - Inregistrare costuri de servicii prestate de terti

    """,

    "category": "Manufacturing",
    "depends": [
        "mrp",
        "stock",
        "sale",
        "product",
        "deltatech_warehouse"

    ],

    "data": [
        "views/mrp_view.xml",
        "data/mrp_data.xml"
    ],

    "installable": True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
