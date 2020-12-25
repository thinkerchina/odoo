# -*- coding: utf-8 -*-
{
    'name': "test social测试用工",

    'summary': """
        test social,测试用工服务""",

    'description': """
        实现测试用工服务，目前设定三方面岗位：工人、工长、业主。
    """,

    'author': "Smart Orgnization",
    'website': "http://www.qingzuzhi.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'smartorg',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',], #依赖别的模型在此体现

    # always loaded
    'data': [
        'security/group.xml',
        #'security/security.xml',
        'security/ir.model.access.csv',                
        'views/views.xml',
        'views/hostview.xml',
        'views/headview.xml',
        'views/workerview.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
