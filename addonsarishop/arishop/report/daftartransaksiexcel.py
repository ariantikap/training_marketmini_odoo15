from odoo import models, fields

class PartnerXlsx(models.AbstractModel):
    _name = 'report.arishop.report_transaksi_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, transaksi):
        sheet = workbook.add_worksheet('Daftar Transaksi')
        bold = workbook.add_format({'bold': True})

        sheet.write(0, 0, 'Tanggal Laporan')
        sheet.write(0, 1, str(self.tgl_lap))
        sheet.write(2, 0, 'No Nota')
        sheet.write(2, 1, 'ID Pembeli')
        sheet.write(2, 2, 'Nama Pembeli')
        sheet.write(2, 3, 'Status')
        sheet.write(2, 4, 'Tgl Transaksi')
        sheet.write(2, 5, 'Total Pembayaran')
        sheet.write(2, 6, 'Quantity')
        sheet.write(2, 7, 'Detail Produk')

        row = 3
        col = 0
        for obj in transaksi:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.id_konsumen)
            sheet.write(row, col+2, obj.nama_pembeli.display_name)
            sheet.write(row, col+3, obj.state)
            sheet.write(row, col+4, str(obj.tgl_beli))
            sheet.write(row, col+5, obj.total_bayar)
            for quan in obj.detailjual_ids:
                sheet.write(row, col+6, quan.qty)
            for item in obj.detailjual_ids:
                sheet.write(row, col+7, item.produk_id.name)
                col += 1
            row += 1
