from odoo import models, fields

class PartnerXlsx(models.AbstractModel):
    _name = 'report.arishop.report_jenisproduk_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, jenisproduk):
        sheet = workbook.add_worksheet('Daftar Jenis Produk')
        bold = workbook.add_format({'bold': True})

        sheet.write(0, 0, 'Tanggal Laporan')
        sheet.write(0, 1, str(self.tgl_lap))
        sheet.write(2, 0, 'Jenis Produk')
        sheet.write(2, 1, 'Kode Jenis')
        sheet.write(2, 2, 'Kode Rak')
        sheet.write(2, 3, 'Jumlah Produk')
        sheet.write(2, 4, 'List Produk')

        row = 3
        col = 0
        for obj in jenisproduk:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.kode_jenis)
            sheet.write(row, col+2, obj.kode_rak)
            sheet.write(row, col+3, obj.jml_produk)
            for item in obj.produk_ids:
                sheet.write(row, col+4, item.name)
                col += 1
            row += 1
