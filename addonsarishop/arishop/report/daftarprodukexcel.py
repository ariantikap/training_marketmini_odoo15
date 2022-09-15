from odoo import models, fields

class PartnerXlsx(models.AbstractModel):
    _name = 'report.arishop.report_produk_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, produk):
        sheet = workbook.add_worksheet('Daftar Produk')
        bold = workbook.add_format({'bold': True})

        sheet.write(0, 0, 'Tanggal Laporan')
        sheet.write(0, 1, str(self.tgl_lap))
        sheet.write(2, 0, 'Nama Produk')
        sheet.write(2, 1, 'Stok')
        sheet.write(2, 2, 'Harga Jual')
        sheet.write(2, 3, 'Harga Beli')
        sheet.write(2, 4, 'Jenis Produk')
        sheet.write(2, 5, 'Supplier')

        row = 3
        col = 0
        for obj in produk:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.stok)
            sheet.write(row, col+2, obj.harga_jual)
            sheet.write(row, col+3, obj.harga_beli)
            for a in obj.jenisproduk_id:
                sheet.write(row, col+4, a.name)
            for item in obj.supplier_id:
                sheet.write(row, col+5, item.name)
                col += 1
            row += 1
