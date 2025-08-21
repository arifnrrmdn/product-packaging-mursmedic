{
    'name': 'Product Packaging Bundle',
    'version': '12.0.2.0.1',
    'summary': 'Gabungan modul: ageing report, combo pack, dan packaging delivery',
    'description': """
        Modul ini menggabungkan fitur:
        - Laporan umur produk (Product Ageing Report)
        - Pengelolaan paket produk (Product Combo Pack)
        - Pengaturan packaging dan delivery (Product Packaging Delivery)
    """,
    'images': ['static/description/icon.png'],
    'category': 'Product/Stock',
    'website': "https://fujicon-japan.com/",
    'company': 'Fujicon Priangan Perdana',
    'author': 'Arif',
    'depends': ['base', 'product', 'stock', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/action_manager.xml',
        'views/product_form_view.xml',
        'views/product_pack.xml',
        'views/product_template_view.xml',
        'wizard/select_product_pack_view.xml',
        'wizard/product_ageing.xml',
        'wizard/product_ageing.xml',
        'views/sale_order_view.xml',
        'report/report_ageing_products.xml',
        
    ],
    'installable': True,
    'application': False,
}
