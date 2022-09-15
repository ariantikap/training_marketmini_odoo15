from odoo import models, fields

class PartnerXlsx(models.AbstractModel):
    _name = 'report.arimart.report_penjualan_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, penjualan):
        sheet = workbook.add_worksheet('Daftar Penjualan')
        bold = workbook.add_format({'bold': True})

        sheet.write(0, 0, 'Tanggal Laporan')
        sheet.write(0, 1, str(self.tgl_lap))
        sheet.write(2, 0, 'No Nota')
        sheet.write(2, 1, 'Nama Pembeli')
        sheet.write(2, 2, 'Tgl Transaksi')
        sheet.write(2, 3, 'Total Pembayaran')

        row = 3
        col = 0
        for obj in penjualan:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.nama_pembeli)
            sheet.write(row, col+2, str(obj.tgl_penjualan))
            sheet.write(row, col+3, obj.total_bayar)
            row += 1
