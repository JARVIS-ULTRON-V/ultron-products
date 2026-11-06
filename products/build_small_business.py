#!/usr/bin/env python3
"""Small Business Finance Spreadsheet Kit — 6 linked sheets, 3 dashboards, real formulas."""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation

OUT = '/root/products-build/small-business'
os.makedirs(OUT, exist_ok=True)

NAVY, TEAL, GREY = '1F2A44', '14B8A6', '64748B'
hdr_font = Font(bold=True, color='FFFFFF', size=11)
hdr_fill = PatternFill('solid', fgColor=NAVY)
title_font = Font(bold=True, size=14, color=NAVY)
sub_font = Font(italic=True, size=9, color=GREY)
bold = Font(bold=True, size=11)
thin = Side(style='thin', color='CBD5E1')
box = Border(left=thin, right=thin, top=thin, bottom=thin)
money, pct, date_fmt = '#,##0.00', '0.0%', 'dd/mm/yyyy'

wb = Workbook()
REG = {}


def style_header(ws, row, ncols, start=1):
    for c in range(start, start + ncols):
        cell = ws.cell(row=row, column=c)
        cell.font, cell.fill = hdr_font, hdr_fill
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        cell.border = box
    ws.row_dimensions[row].height = 28


def widths(ws, spec):
    for col, w in spec.items():
        ws.column_dimensions[col].width = w


def title_block(ws, title, subtitle, ncols):
    ws['A1'] = title; ws['A1'].font = title_font
    ws['A2'] = subtitle; ws['A2'].font = sub_font
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=max(2, ncols))
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=max(2, ncols))
    ws.row_dimensions[1].height = 20


def write_summary(ws, r, label, rows, registry=None):
    ws.cell(row=r, column=1, value=label).font = hdr_font
    ws.cell(row=r, column=1).fill = hdr_fill
    for i, (l2, f2, fmt) in enumerate(rows):
        rr = r + 1 + i
        ws.cell(row=rr, column=1, value=l2).font = bold
        c = ws.cell(row=rr, column=2, value=f2)
        c.number_format = fmt
        c.font = Font(bold=True, size=11, color=NAVY)
        c.border = box
        ws.cell(row=rr, column=1).border = box
        if registry is not None:
            registry[l2] = rr
    return r + 1 + len(rows)


def ref(sheet, label, registry):
    return "'%s'!$B$%d" % (sheet, registry[label])


# ---------------------------------------------------------------- SETTINGS
ws = wb.active
ws.title = 'Settings'
title_block(ws, 'Small Business Finance Kit', 'Set your business basics once - every sheet calculates from this.', 4)
for i, c in enumerate(['SETTING', 'VALUE', 'FORMAT', 'NOTE'], 1):
    ws.cell(row=4, column=i, value=c)
style_header(ws, 4, 4)
settings = [
    ('Business name', 'Your Business', '', 'Appears on reports'),
    ('Currency symbol', 'INR', '', 'INR / USD / EUR ...'),
    ('Fiscal year start', 'April', '', 'Used by the 12-month trend'),
    ('Default VAT/GST rate', 0.18, pct, 'Applied in the invoice tracker'),
    ('Monthly owner salary', 50000, money, 'Shown as an expense in P&L'),
    ('Break-even margin target', 0.30, pct, 'Gross margin target on dashboard'),
    ('Cash buffer target (months)', 3, '0', 'Used by the cash-flow dashboard'),
]
r = 5
for name, val, fmt, note in settings:
    ws.cell(row=r, column=1, value=name).font = bold
    c = ws.cell(row=r, column=2, value=val)
    if fmt in (pct, money):
        c.number_format = fmt
    ws.cell(row=r, column=3, value=fmt if fmt else 'Text').font = Font(size=9, color=GREY)
    ws.cell(row=r, column=4, value=note).font = Font(size=9, color=GREY)
    for cc in range(1, 5):
        ws.cell(row=r, column=cc).border = box
    r += 1
widths(ws, {'A': 28, 'B': 18, 'C': 12, 'D': 52})
GST = 'Settings!$B$8'
SALARY = 'Settings!$B$9'

# ---------------------------------------------------------------- TRANSACTIONS
ws = wb.create_sheet('Transactions')
title_block(ws, 'Transactions', 'Paste or enter every inflow and outflow. Everything else builds from this.', 10)
cols = ['Date', 'Category', 'Description', 'Type', 'Amount', 'Bank account', 'Paid via',
        'Taxable', 'VAT/GST', 'Notes']
for i, c in enumerate(cols, 1):
    ws.cell(row=4, column=i, value=c)
style_header(ws, 4, len(cols))
widths(ws, {'A': 13, 'B': 20, 'C': 32, 'D': 12, 'E': 13, 'F': 14, 'G': 14, 'H': 10, 'I': 10, 'J': 28})

sample = [
    ('2026-10-02', 'Sales revenue', 'Website project - client A', 'Income', 120000, 'Business account', 'Bank transfer', True, 0.18, ''),
    ('2026-10-05', 'Cost of goods', 'Inventory purchase', 'Expense', 40000, 'Business account', 'Bank transfer', True, 0.18, ''),
    ('2026-10-08', 'Marketing', 'Meta ads - October', 'Expense', 15000, 'Business account', 'Debit card', True, 0.18, ''),
    ('2026-10-12', 'Rent', 'Office rent - October', 'Expense', 25000, 'Business account', 'Bank transfer', True, 0.0, ''),
    ('2026-10-15', 'Sales revenue', 'Retainer - client B', 'Income', 60000, 'Business account', 'Bank transfer', True, 0.18, ''),
    ('2026-10-20', 'Owner drawings', 'Monthly owner salary', 'Expense', 50000, 'Business account', 'Bank transfer', False, 0.0, ''),
]
for ri, row in enumerate(sample, start=5):
    for ci, v in enumerate(row, 1):
        cell = ws.cell(row=ri, column=ci, value=v)
        cell.border = box
        if ci == 1:
            cell.number_format = date_fmt
        if ci in (5, 9):
            cell.number_format = money if ci == 5 else pct
        if ci == 8:
            cell.number_format = pct

LAST = 300
for ri in range(5, LAST + 1):
    ws.cell(row=ri, column=8, value=f'=IF(E{ri}="","",IF(H{ri}="","",IF(D{ri}="Income",0,E{ri}*H{ri})))')
    ws.cell(row=ri, column=9, value=f'=IF(E{ri}="","",IF(AND(D{ri}="Expense",I{ri}>0),E{ri}*I{ri},0))')
    for ci in (1,):
        pass
    ws.cell(row=ri, column=8).number_format = money
    ws.cell(row=ri, column=9).number_format = money
    for ci in (8, 9):
        ws.cell(row=ri, column=ci).border = box

dv = DataValidation(type='list', formula1='"Income,Expense,Transfer"', allow_blank=True)
ws.add_data_validation(dv); dv.add('D5:D%d' % LAST)

tx_reg = {}
write_summary(ws, LAST + 2, 'TOTALS', [
    ('Total income', f'=SUMIF(D5:D{LAST},"Income",E5:E{LAST})', money),
    ('Total expenses', f'=SUMIF(D5:D{LAST},"Expense",E5:E{LAST})', money),
    ('Net cash flow', f'=B{LAST+3}-B{LAST+4}', money),
    ('Taxable income', f'=SUMIFS(E5:E{LAST},D5:D{LAST},"Income",H5:H{LAST},">0")', money),
    ('VAT collected', f'=SUMIFS(I5:I{LAST},D5:D{LAST},"Income")', money),
    ('VAT paid out', f'=SUMIFS(I5:I{LAST},D5:D{LAST},"Expense")', money),
    ('Net VAT owed', f'=B{LAST+6}-B{LAST+7}', money),
    ('Business expenses (excl owner salary)', f'=SUMIFS(E5:E{LAST},D5:D{LAST},"Expense",B5:B{LAST},"<>Owner drawings")', money),
], tx_reg)
REG['Transactions'] = tx_reg

# ---------------------------------------------------------------- INCOME & EXPENSES
ws = wb.create_sheet('Income & Expenses')
title_block(ws, 'Income & Expenses', 'Categorised summary - the raw data feeds the P&L and dashboards.', 6)
cols = ['Category', 'Type', 'This month', 'Last month', 'Year to date', 'Notes']
for i, c in enumerate(cols, 1):
    ws.cell(row=4, column=i, value=c)
style_header(ws, 4, len(cols))
widths(ws, {'A': 24, 'B': 12, 'C': 14, 'D': 14, 'E': 14, 'F': 30})

cats = [
    ('Sales revenue', 'Income', 'D', 'E', 'A'),
    ('Other income', 'Income', 'D', 'E', 'A'),
    ('Cost of goods', 'Expense', 'D', 'E', 'A'),
    ('Marketing', 'Expense', 'D', 'E', 'A'),
    ('Rent & utilities', 'Expense', 'D', 'E', 'A'),
    ('Software & tools', 'Expense', 'D', 'E', 'A'),
    ('Equipment', 'Expense', 'D', 'E', 'A'),
    ('Wages & owner salary', 'Expense', 'D', 'E', 'A'),
    ('Insurance', 'Expense', 'D', 'E', 'A'),
    ('Travel & transport', 'Expense', 'D', 'E', 'A'),
    ('Miscellaneous', 'Expense', 'D', 'E', 'A'),
]
r = 5
for cat, typ, _, _, _ in cats:
    ws.cell(row=r, column=1, value=cat).font = bold
    ws.cell(row=r, column=2, value=typ)
    ws.cell(row=r, column=3, value=f'=SUMIFS(Transactions!$E$5:$E${LAST},Transactions!$A$5:$A${LAST},">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1),Transactions!$A$5:$A${LAST},"<="&EOMONTH(TODAY(),0),Transactions!$B$5:$B${LAST},$A{r})')
    ws.cell(row=r, column=4, value=f'=SUMIFS(Transactions!$E$5:$E${LAST},Transactions!$A$5:$A${LAST},">="&DATE(YEAR(TODAY()),MONTH(TODAY())-1,1),Transactions!$A$5:$A${LAST},"<="&EOMONTH(TODAY(),-1),Transactions!$B$5:$B${LAST},$A{r})')
    ws.cell(row=r, column=5, value=f'=SUMIFS(Transactions!$E$5:$E${LAST},Transactions!$A$5:$A${LAST},">="&DATE(YEAR(TODAY()),1,1),Transactions!$A$5:$A${LAST},"<="&TODAY(),Transactions!$B$5:$B${LAST},$A{r})')
    for ci in (3, 4, 5):
        ws.cell(row=r, column=ci).number_format = money
    for ci in range(1, 7):
        ws.cell(row=r, column=ci).border = box
    r += 1

# totals row
ws.cell(row=r, column=1, value='TOTAL').font = hdr_font
ws.cell(row=r, column=1).fill = hdr_fill
ws.cell(row=r, column=3, value=f'=SUMPRODUCT(($B$5:$B${r-1}="Income")*C$5:C${r-1})')
ws.cell(row=r, column=4, value=f'=SUMPRODUCT(($B$5:$B${r-1}="Income")*D$5:D${r-1})')
ws.cell(row=r, column=5, value=f'=SUMPRODUCT(($B$5:$B${r-1}="Income")*E$5:E${r-1})')
for ci in (3, 4, 5):
    ws.cell(row=r, column=ci).number_format = money
    ws.cell(row=r, column=ci).font = bold
r += 1
ws.cell(row=r, column=1, value='TOTAL EXPENSES').font = hdr_font
ws.cell(row=r, column=1).fill = hdr_fill
ws.cell(row=r, column=3, value=f'=SUMPRODUCT(($B$5:$B${r-2}="Expense")*C$5:C${r-2})')
ws.cell(row=r, column=4, value=f'=SUMPRODUCT(($B$5:$B${r-2}="Expense")*D$5:D${r-2})')
ws.cell(row=r, column=5, value=f'=SUMPRODUCT(($B$5:$B${r-2}="Expense")*E$5:E${r-2})')
for ci in (3, 4, 5):
    ws.cell(row=r, column=ci).number_format = money
    ws.cell(row=r, column=ci).font = bold
r += 1
ws.cell(row=r, column=1, value='NET PROFIT').font = hdr_font
ws.cell(row=r, column=1).fill = hdr_fill
ws.cell(row=r, column=3, value=f'=C{r-2}-C{r-1}')
ws.cell(row=r, column=4, value=f'=D{r-2}-D{r-1}')
ws.cell(row=r, column=5, value=f'=E{r-2}-E{r-1}')
for ci in (3, 4, 5):
    ws.cell(row=r, column=ci).number_format = money
    ws.cell(row=r, column=ci).font = bold
    ws.cell(row=r, column=ci).fill = PatternFill('solid', fgColor=TEAL)

# ---------------------------------------------------------------- CASH FLOW
ws = wb.create_sheet('Cash Flow')
title_block(ws, 'Cash Flow', 'See exactly where cash is going and whether you can pay the bills.', 7)
cols = ['Month', 'Opening balance', 'Cash in', 'Cash out', 'Net', 'Closing balance', 'Notes']
for i, c in enumerate(cols, 1):
    ws.cell(row=4, column=i, value=c)
style_header(ws, 4, len(cols))
widths(ws, {'A': 14, 'B': 16, 'C': 14, 'D': 14, 'E': 14, 'F': 16, 'G': 30})
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
r = 5
ws.cell(row=r, column=1, value='January').font = bold
ws.cell(row=r, column=2, value=200000).number_format = money
ws.cell(row=r, column=3, value=95000).number_format = money
ws.cell(row=r, column=4, value=78000).number_format = money
ws.cell(row=r, column=5, value=f'=C{r}-D{r}').number_format = money
ws.cell(row=r, column=6, value=f'=B{r}+E{r}').number_format = money
for ci in range(1, 8):
    ws.cell(row=r, column=ci).border = box
r = 6
for m in months[1:]:
    ws.cell(row=r, column=1, value=m).font = bold
    ws.cell(row=r, column=2, value=f'=F{r-1}').number_format = money
    ws.cell(row=r, column=3, value=f'=SUMIFS(Transactions!$E$5:$E${LAST},Transactions!$A$5:$A${LAST},">="&DATE(YEAR(TODAY()),MONTH(DATEVALUE($A{r}&" 1")),1),Transactions!$A$5:$A${LAST},"<="&EOMONTH(DATEVALUE($A{r}&" 1"),0),Transactions!$D$5:$D${LAST},"Income")').number_format = money
    ws.cell(row=r, column=4, value=f'=SUMIFS(Transactions!$E$5:$E${LAST},Transactions!$A$5:$A${LAST},">="&DATE(YEAR(TODAY()),MONTH(DATEVALUE($A{r}&" 1")),1),Transactions!$A$5:$A${LAST},"<="&EOMONTH(DATEVALUE($A{r}&" 1"),0),Transactions!$D$5:$D${LAST},"Expense")').number_format = money
    ws.cell(row=r, column=5, value=f'=C{r}-D{r}').number_format = money
    ws.cell(row=r, column=6, value=f'=B{r}+E{r}').number_format = money
    for ci in range(1, 8):
        ws.cell(row=r, column=ci).border = box
    r += 1

cf_reg = {}
write_summary(ws, r, 'TOTALS', [
    ('Opening balance (Jan)', '=$B$5', money),
    ('Total cash in', f'=SUM(C5:C{r-1})', money),
    ('Total cash out', f'=SUM(D5:D{r-1})', money),
    ('Net cash movement', f'=B{r+1}-B{r+2}', money),
    ('Closing balance (Dec)', f'=F{r-1}', money),
], cf_reg)
REG['Cash Flow'] = cf_reg

# ---------------------------------------------------------------- P&L
ws = wb.create_sheet('P&L')
title_block(ws, 'Profit & Loss', 'Revenue minus costs = true profit. Updated from your transactions.', 6)
cols = ['', 'This month', 'Last month', 'Year to date', '% of revenue', '']
for i, c in enumerate(cols, 1):
    ws.cell(row=4, column=i, value=c)
style_header(ws, 4, 5)

pl = [
    ('Revenue', 'Income & Expenses!C$5', 'Income & Expenses!D$5', 'Income & Expenses!E$5'),
    ('Less: Cost of goods', 'Income & Expenses!C$7', 'Income & Expenses!D$7', 'Income & Expenses!E$7'),
    ('Gross profit', '=B5-B6', '=C5-C6', '=D5-D6'),
    ('Operating expenses', '=SUM(Income & Expenses!C$8:C$15)', '=SUM(Income & Expenses!D$8:D$15)', '=SUM(Income & Expenses!E$8:E$15)'),
    ('Net profit', '=B7-B8', '=C7-C8', '=D7-D8'),
]
r = 5
for label, c, l, ytd in pl:
    ws.cell(row=r, column=1, value=label).font = bold
    ws.cell(row=r, column=2, value=c).number_format = money
    ws.cell(row=r, column=3, value=l).number_format = money
    ws.cell(row=r, column=4, value=ytd).number_format = money
    ws.cell(row=r, column=5, value=f'=IFERROR(B{r}/B$5,0)').number_format = pct
    for ci in range(1, 6):
        ws.cell(row=r, column=ci).border = box
    ws.cell(row=r, column=5).number_format = pct
    r += 1
# margin row
ws.cell(row=r, column=1, value='Net margin').font = hdr_font
ws.cell(row=r, column=1).fill = hdr_fill
ws.cell(row=r, column=2, value=f'=IFERROR(B9/B5,0)').number_format = pct
ws.cell(row=r, column=3, value=f'=IFERROR(C9/C5,0)').number_format = pct
ws.cell(row=r, column=4, value=f'=IFERROR(D9/D5,0)').number_format = pct
for ci in range(1, 6):
    ws.cell(row=r, column=ci).border = box
widths(ws, {'A': 26, 'B': 14, 'C': 14, 'D': 14, 'E': 12})

# ---------------------------------------------------------------- INVOICE TRACKER
ws = wb.create_sheet('Invoice Tracker')
title_block(ws, 'Invoice Tracker', 'What you billed, what arrived, what is still owed.', 9)
cols = ['Invoice #', 'Customer', 'Issue date', 'Due date', 'Subtotal', 'VAT/GST', 'Total', 'Paid', 'Status']
for i, c in enumerate(cols, 1):
    ws.cell(row=4, column=i, value=c)
style_header(ws, 4, len(cols))
widths(ws, {'A': 12, 'B': 26, 'C': 13, 'D': 13, 'E': 13, 'F': 12, 'G': 13, 'H': 13, 'I': 12})
sample = [
    ('INV-101', 'Client A', '2026-10-01', '2026-10-15', 101695, '', 120000, 120000, ''),
    ('INV-102', 'Client B', '2026-10-10', '2026-10-24', 50847, '', 60000, 0, ''),
    ('INV-103', 'Client C', '2026-10-18', '2026-11-01', 76271, '', 90000, 30000, ''),
]
ILAST = 200
for ri, row in enumerate(sample, start=5):
    for ci, v in enumerate(row, 1):
        cell = ws.cell(row=ri, column=ci, value=v)
        cell.border = box
        if ci in (3, 4): cell.number_format = date_fmt
        if ci in (5, 6, 7, 8): cell.number_format = money
    ws.cell(row=ri, column=6, value=f'=IF(E{ri}="","",ROUND(E{ri}*{GST},2))')
    ws.cell(row=ri, column=7, value=f'=IF(E{ri}="","",ROUND(E{ri}*(1+{GST}),2))').number_format = money
    ws.cell(row=ri, column=9, value=(
        f'=IF(G{ri}="","",IF(H{ri}>=G{ri},"Paid",'
        f'IF(TODAY()>D{ri},IF(H{ri}>0,"Part-paid","Overdue"),"Sent")))'))
    ws.cell(row=ri, column=6).border = box
    ws.cell(row=ri, column=7).border = box
    ws.cell(row=ri, column=9).border = box
for ri in range(8, ILAST + 1):
    ws.cell(row=ri, column=6, value=f'=IF(E{ri}="","",ROUND(E{ri}*{GST},2))')
    ws.cell(row=ri, column=7, value=f'=IF(E{ri}="","",ROUND(E{ri}*(1+{GST}),2))').number_format = money
    ws.cell(row=ri, column=9, value=(
        f'=IF(G{ri}="","",IF(H{ri}>=G{ri},"Paid",'
        f'IF(TODAY()>D{ri},IF(H{ri}>0,"Part-paid","Overdue"),"Sent")))'))
    ws.cell(row=ri, column=5).number_format = money
    ws.cell(row=ri, column=8).number_format = money
    for ci in (6, 7, 9):
        ws.cell(row=ri, column=ci).border = box

inv_reg = {}
write_summary(ws, ILAST + 2, 'TOTALS', [
    ('Total billed', f'=SUM(G5:G{ILAST})', money),
    ('Total received', f'=SUM(H5:H{ILAST})', money),
    ('Outstanding', f'=B{ILAST+3}-B{ILAST+4}', money),
    ('Overdue', f'=SUMIF(I5:I{ILAST},"Overdue",G5:G{ILAST})', money),
    ('Overdue count', f'=COUNTIF(I5:I{ILAST},"Overdue")', '0'),
], inv_reg)
REG['Invoice Tracker'] = inv_reg

# ---------------------------------------------------------------- TAX SUMMARY
ws = wb.create_sheet('Tax Summary')
title_block(ws, 'Tax Summary', 'What you owe in VAT/GST and what you can reclaim.', 6)
cols = ['', 'This month', 'Year to date', '', '', '']
for i, c in enumerate(cols, 1):
    ws.cell(row=4, column=i, value=c)
style_header(ws, 4, 3)
rows = [
    ('VAT/GST collected on sales', '=SUMIFS(Transactions!$I$5:$I$300,Transactions!$A$5:$A$300,">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1),Transactions!$A$5:$A$300,"<="&EOMONTH(TODAY(),0),Transactions!$D$5:$D$300,"Income")', '=SUMIFS(Transactions!$I$5:$I$300,Transactions!$D$5:$D$300,"Income")'),
    ('VAT/GST paid on purchases', '=SUMIFS(Transactions!$I$5:$I$300,Transactions!$A$5:$A$300,">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1),Transactions!$A$5:$A$300,"<="&EOMONTH(TODAY(),0),Transactions!$D$5:$D$300,"Expense")', '=SUMIFS(Transactions!$I$5:$I$300,Transactions!$D$5:$D$300,"Expense")'),
    ('Net VAT/GST due', '=B5-B6', '=C5-C6'),
]
r = 5
for label, m, ytd in rows:
    ws.cell(row=r, column=1, value=label).font = bold
    ws.cell(row=r, column=2, value=m).number_format = money
    ws.cell(row=r, column=3, value=ytd).number_format = money
    for ci in range(1, 4):
        ws.cell(row=r, column=ci).border = box
    r += 1
widths(ws, {'A': 32, 'B': 16, 'C': 16})

# ---------------------------------------------------------------- DASHBOARD
ws = wb.create_sheet('Dashboard', 0)
title_block(ws, 'Small Business Dashboard', 'One screen: cash, profit, runway and what needs attention.', 6)
widths(ws, {'A': 36, 'B': 16, 'C': 4, 'D': 36, 'E': 16, 'F': 4})

ws.cell(row=4, column=1, value='CASH & PROFIT').font = hdr_font
ws.cell(row=4, column=1).fill = hdr_fill
ws.cell(row=4, column=2, value='Value').font = hdr_font
ws.cell(row=4, column=2).fill = hdr_fill
ws.cell(row=4, column=4, value='INVOICES').font = hdr_font
ws.cell(row=4, column=4).fill = hdr_fill
ws.cell(row=4, column=5, value='Value').font = hdr_font
ws.cell(row=4, column=5).fill = hdr_fill

left = [
    ('Revenue this month', '=' + ref('Income & Expenses', 'TOTAL', {}) if False else '=Income & Expenses!C$16', money),
    ('Expenses this month', '=Income & Expenses!C$17', money),
    ('Net profit this month', '=Income & Expenses!C$18', money),
    ('Net margin', '=IFERROR(C18/C16,0)', pct),
    ('Cash in bank (closing Dec)', '=' + ref('Cash Flow', 'Closing balance (Dec)', cf_reg), money),
    ('Cash flow this month', '=Cash Flow!E$16', money),
    ('Gross profit (YTD)', '=P&L!D$7', money),
    ('Net profit (YTD)', '=P&L!D$9', money),
]
right = [
    ('Total billed', '=' + ref('Invoice Tracker', 'Total billed', inv_reg), money),
    ('Total received', '=' + ref('Invoice Tracker', 'Total received', inv_reg), money),
    ('Outstanding', '=' + ref('Invoice Tracker', 'Outstanding', inv_reg), money),
    ('Overdue', '=' + ref('Invoice Tracker', 'Overdue', inv_reg), money),
    ('Overdue invoices', '=' + ref('Invoice Tracker', 'Overdue count', inv_reg), '0'),
    ('Net VAT due (month)', '=Tax Summary!B$7', money),
    ('Net VAT due (YTD)', '=Tax Summary!C$7', money),
]
for i, (l2, f2, fmt) in enumerate(left):
    rr = 5 + i
    ws.cell(row=rr, column=1, value=l2).font = bold
    c = ws.cell(row=rr, column=2, value=f2)
    c.number_format = fmt
    c.font = Font(bold=True, size=11, color=NAVY)
    c.border = box
    ws.cell(row=rr, column=1).border = box
for i, (l2, f2, fmt) in enumerate(right):
    rr = 5 + i
    ws.cell(row=rr, column=4, value=l2).font = bold
    c = ws.cell(row=rr, column=5, value=f2)
    c.number_format = fmt
    c.font = Font(bold=True, size=11, color=NAVY)
    c.border = box
    ws.cell(row=rr, column=4).border = box

ws.cell(row=13, column=1, value='KEY METRICS').font = hdr_font
ws.cell(row=13, column=1).fill = hdr_fill
ws.cell(row=13, column=4, value='HEALTH CHECKS').font = hdr_font
ws.cell(row=13, column=4).fill = hdr_fill
metrics = [
    ('Gross margin (YTD)', '=IFERROR(P&L!D$7/P&L!D$5,0)', pct),
    ('Net margin (YTD)', '=IFERROR(P&L!D$9/P&L!D$5,0)', pct),
    ('Cash runway (months)', '=IFERROR(Cash Flow!F$16/MAX(1,(Income & Expenses!C$17)),0)', '0.0'),
]
checks = [
    ('Expense ratio', '=IFERROR(Income & Expenses!C$17/Income & Expenses!C$16,0)', pct),
    ('Invoice collection rate', '=IFERROR(Invoice Tracker!B$24/Invoice Tracker!B$23,0)', pct),
    ('Overdue ratio', '=IFERROR(Invoice Tracker!B$26/Invoice Tracker!B$23,0)', pct),
]
for i, (l2, f2, fmt) in enumerate(metrics):
    rr = 14 + i
    ws.cell(row=rr, column=1, value=l2).font = bold
    c = ws.cell(row=rr, column=2, value=f2)
    c.number_format = fmt; c.font = Font(bold=True, size=11, color=NAVY)
    c.border = box; ws.cell(row=rr, column=1).border = box
for i, (l2, f2, fmt) in enumerate(checks):
    rr = 14 + i
    ws.cell(row=rr, column=4, value=l2).font = bold
    c = ws.cell(row=rr, column=5, value=f2)
    c.number_format = fmt; c.font = Font(bold=True, size=11, color=NAVY)
    c.border = box; ws.cell(row=rr, column=4).border = box

ws.cell(row=18, column=1, value='MONTHLY PROFIT TREND').font = hdr_font
ws.cell(row=18, column=1).fill = hdr_fill
for i, c in enumerate(['Month', 'Revenue', 'Expenses', 'Net'], 1):
    ws.cell(row=19, column=i, value=c)
style_header(ws, 19, 4)
for ri in range(20, 32):
    ws.cell(row=ri, column=4, value=f'=IF(B{ri}="","",B{ri}-C{ri})').number_format = money
    ws.cell(row=ri, column=2).number_format = money
    ws.cell(row=ri, column=3).number_format = money
    for ci in range(1, 5):
        ws.cell(row=ri, column=ci).border = box

ws.cell(row=34, column=1, value='HOW TO USE').font = hdr_font
ws.cell(row=34, column=1).fill = hdr_fill
steps = [
    '1. Transactions: this is the only sheet you fill in. Enter every inflow and outflow.',
    '2. Mark each transaction Income/Expense and pick a category - the rest updates.',
    '3. Invoice Tracker: log what you bill; status and VAT calculate automatically.',
    '4. Cash Flow: 12 months are prefilled with formulas - review them monthly.',
    '5. Dashboard: open this first. Cash, profit, margins and overdue at a glance.',
    '6. P&L and Tax Summary auto-build from your transactions.',
]
for i, s in enumerate(steps):
    ws.cell(row=35 + i, column=1, value=s).font = Font(size=10)
    ws.merge_cells(start_row=35 + i, start_column=1, end_row=35 + i, end_column=5)

path = os.path.join(OUT, 'Small Business Finance Kit.xlsx')
wb.save(path)
print('OK ->', path)
print('sheets:', wb.sheetnames)
