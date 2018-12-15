# -*- coding: utf-8 -*-
from odoo import http
# from escpos.printer import Usb
#from escpos.connections import getUSBPrinter
#
from odoo import api
#from dbfread import DBF

class Felino(http.Controller):
      @http.route('/felino', auth='public',website=True)
      def index(self, **kw):
         return http.request.render('felino.nino')

      @http.route('/felino/print', auth='public',website=True)
      def cetak(self, **kw):
          #conn = cups.Connection ()
          #printers = conn.getPrinters ()   
          #for printer in printers:
          #    print printer  
          #self.env.cr.execute("select * from product_product")
          return http.request.render('felino.cetak') 
      @http.route('/felino/syncron', auth='public',website=True)
      def syncron(self, **kw):
          #for item in DBF('/mnt/poserver/ics/DAT/INV018.DBF',encoding='iso-8859-1'):
          #    print "x"
          #return "http.request.render('felino.syncron')"     
          return 'data' 
       

      @http.route('/felino/felino/objects/', auth='public',website=True)
      def list(self, **kw):
          return http.request.render('felino.listing', {
             'root': '/felino/felino',
             'objects': http.request.env['felino.felino'].search([]),
          })

#     @http.route('/felino/felino/objects/<model("felino.felino"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('felino.object', {
#             'object': obj
#         })