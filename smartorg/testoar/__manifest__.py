# -*- coding: utf-8 -*-
{
    'name': "Test OAR目标成果法",

    'summary': """
        SmartOAR的测试包软件
        """,

    'description': """
        OAR的测试包软件，借助odoo的python包来实现
    """,

    'author': "Smart Orgnization",
    'website': "http://www.qingzuzhi.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'smartorg',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','board'],

    # always loaded
    'data': [
        'demo/demo.xml', #示例数据
        'security/security.xml', #访问权限说明
        'security/ir.model.access.csv', #同上
        #'views/views.xml',
        #'views/templates.xml',
        'views/testoar.xml', #增加的testoar数据项
        #'views/partner.xml', #增加的partner数据项
        #'views/session_board.xml' #增加仪表盘
        # 'reports.xml'        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml', #示例数据
        
    ],
}
