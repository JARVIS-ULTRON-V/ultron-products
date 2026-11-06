#!/usr/bin/env python3
"""Build the Freelancer Finance Tracker .xlsx (linked sheets, real formulas).

Every cross-sheet reference is resolved from a registry of actual summary row
numbers captured while each sheet is written - no hardcoded row guesses.
"""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation

OUT = '/root/products-build/freelancer-finance'
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
REG = {}   # sheet -> {label: row}


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


def write_summary(ws, r, label, rows, registry=None, key=None):
    """Write a summary block; record each label's row in REG[sheet][label]."""
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
    """Return an absolute cross-sheet reference like Income!$B$203"""
    return "'%s'!$B$%d" % (sheet, registry[label])


# ------------------------------------------------------------------ SETTINGS
ws = wb.active
ws.title = 'Settings'
title_block(ws, 'Freelancer Finance Tracker',
            'Set your rates here once - every other sheet calculates from this.', 4)
for i, c in enumerate(['SETTING', 'VALUE', 'FORMAT', 'NOTE'], 1):
    ws.cell(row=4, column=i, value=c)
style_header(ws, 4, 4)
settings = [
    ('Business name', 'Your Freelance Co', '', 'Appears on invoices'),
    ('Currency symbol', 'INR', '', 'Change to USD, EUR etc.'),
    ('Tax / set-aside rate', 0.30, pct, 'Portion of every payment you set aside for tax'),
    ('Default hourly rate', 1500, money, 'Used by the rate calculator on the Income sheet'),
    ('Default project rate', 45000, money, 'Used by the rate calculator on the Income sheet'),
    ('Payment reminder day', 5, '', 'Day of month to chase overdue invoices'),
    ('Target monthly income', 120000, money, 'Used by the savings-goal and income-gap formulas'),
    ('Tax year starts', 'April', '', 'Your financial year start month'),
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
TAX_RATE = 'Settings!$B$7'
HOURLY = 'Settings!$B$8'
TARGET = 'Settings!$B$11'

# ------------------------------------------------------------------ INVOICES
ws = wb.create_sheet('Invoices')
title_block(ws, 'Invoices',
            'Every invoice you raise. Overdue days and status calculate automatically.', 9)
cols = ['Invoice #', 'Client', 'Issue date', 'Due date', 'Amount', 'Paid amount',
        'Status', 'Days overdue', 'Notes']
for i, c in enumerate(cols, 1):
    ws.cell(row=4, column=i, value=c)
style_header(ws, 4, len(cols))
widths(ws, {'A': 12, 'B': 24, 'C': 13, 'D': 13, 'E': 13, 'F': 13, 'G': 12, 'H': 13, 'I': 40})

sample = [
    ('INV-001', 'Acme Studios', '2026-10-01', '2026-10-15', 45000, 45000, '', '', 'Website retainer'),
    ('INV-002', 'Northwind Co', '2026-10-08', '2026-10-22', 28000, 0, '', '', 'Brand sprint'),
    ('INV-003', 'Globex', '2026-10-12', '2026-10-26', 62000, 20000, '', '', 'Partial paid'),
]
LAST = 200
for ri, row in enumerate(sample, start=5):
    for ci, v in enumerate(row, 1):
        cell = ws.cell(row=ri, column=ci, value=v)
        cell.border = box
        if ci in (3, 4):
            cell.number_format = date_fmt
        if ci in (5, 6):
            cell.number_format = money
for ri in range(5, LAST + 1):
    ws.cell(row=ri, column=7, value=(
        f'=IF(E{ri}="","",IF(F{ri}>=E{ri},"Paid",'
        f'IF(TODAY()>D{ri},IF(F{ri}>0,"Part-paid","Overdue"),'
        f'IF(TODAY()>=C{ri},"Sent","Draft"))))'))
    ws.cell(row=ri, column=8, value=(
        f'=IF(OR(E{ri}="",F{ri}>=E{ri}),"",IF(TODAY()>D{ri},TODAY()-D{ri},0))'))
    ws.cell(row=ri, column=5).number_format = money
    ws.cell(row=ri, column=6).number_format = money
    for ci in (7, 8):
        ws.cell(row=ri, column=ci).border = box
dv = DataValidation(type='list', formula1='"Draft,Sent,Paid,Part-paid,Overdue"', allow_blank=True)
ws.add_data_validation(dv); dv.add('G5:G%d' % LAST)

inv_reg = {}
write_summary(ws, LAST + 2, 'TOTALS', [
    ('Total invoiced', f'=SUM(E5:E{LAST})', money),
    ('Total received', f'=SUM(F5:F{LAST})', money),
    ('Outstanding', '=B%d-B%d' % (LAST + 3, LAST + 4), money),
    ('Overdue amount', f'=SUMIF(G5:G{LAST},"Overdue",E5:E{LAST})', money),
    ('Overdue count', f'=COUNTIF(G5:G{LAST},"Overdue")', '0'),
    ('Average days overdue', f'=IFERROR(AVERAGEIF(G5:G{LAST},"Overdue",H5:H{LAST}),0)', '0.0'),
], inv_reg)
REG['Invoices'] = inv_reg

# ------------------------------------------------------------------ INCOME
ws = wb.create_sheet('Income')
title_block(ws, 'Income Log',
            'Record what you were paid. Tax set-aside is calculated for you.', 9)
cols = ['Date received', 'Client', 'Invoice #', 'Project / description', 'Gross amount',
        'Tax set-aside', 'Net to you', 'Payment method', 'Notes']
for i, c in enumerate(cols, 1):
    ws.cell(row=4, column=i, value=c)
style_header(ws, 4, len(cols))
widths(ws, {'A': 14, 'B': 22, 'C': 12, 'D': 34, 'E': 14, 'F': 14, 'G': 14, 'H': 16, 'I': 30})
sample = [
    ('2026-10-02', 'Acme Studios', 'INV-001', 'Website retainer - October', 45000, '', '', 'Bank transfer', ''),
    ('2026-10-14', 'Globex', 'INV-003', 'Partial payment on deposit', 20000, '', '', 'Bank transfer', ''),
]
for ri, row in enumerate(sample, start=5):
    for ci, v in enumerate(row, 1):
        cell = ws.cell(row=ri, column=ci, value=v)
        cell.border = box
        if ci == 1:
            cell.number_format = date_fmt
        if ci in (5, 6, 7):
            cell.number_format = money
for ri in range(5, LAST + 1):
    ws.cell(row=ri, column=6, value=f'=IF(E{ri}="","",ROUND(E{ri}*{TAX_RATE},2))')
    ws.cell(row=ri, column=7, value=f'=IF(E{ri}="","",E{ri}-F{ri})')
    for ci in (5, 6, 7):
        ws.cell(row=ri, column=ci).number_format = money
    for ci in (6, 7):
        ws.cell(row=ri, column=ci).border = box
dv = DataValidation(type='list', formula1='"Bank transfer,UPI,PayPal,Card,Cash,Cheque"', allow_blank=True)
ws.add_data_validation(dv); dv.add('H5:H%d' % LAST)

inc_reg = {}
r2 = write_summary(ws, LAST + 2, 'TOTALS', [
    ('Gross income (all time)', f'=SUM(E5:E{LAST})', money),
    ('Total set aside for tax', f'=SUM(F5:F{LAST})', money),
    ('Net to you (all time)', f'=SUM(G5:G{LAST})', money),
    ('Gross this month', f'=SUMIFS(E5:E{LAST},A5:A{LAST},">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1),A5:A{LAST},"<="&EOMONTH(TODAY(),0))', money),
    ('Net this month', f'=SUMIFS(G5:G{LAST},A5:A{LAST},">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1),A5:A{LAST},"<="&EOMONTH(TODAY(),0))', money),
    ('Average monthly gross (last 6 months)', f'=IFERROR(AVERAGEIFS(E5:E{LAST},A5:A{LAST},">="&EDATE(TODAY(),-6),A5:A{LAST},"<="&TODAY()),0)', money),
    ('Income gap vs target this month', '=MAX(0,%s-B%d)' % (TARGET, LAST + 6), money),
], inc_reg)
REG['Income'] = inc_reg

# rate calculator
ws.cell(row=r2 + 1, column=1, value='RATE CALCULATOR').font = hdr_font
ws.cell(row=r2 + 1, column=1).fill = hdr_fill
rc = r2 + 1
calc = [
    ('Hours worked', 10, '0.0'),
    ('Rate used', '=' + HOURLY, money),
    ('Total billable', '=B%d*B%d' % (rc + 1, rc + 2), money),
    ('Tax set-aside on that', '=ROUND(B%d*%s,2)' % (rc + 3, TAX_RATE), money),
    ('You actually keep', '=B%d-B%d' % (rc + 3, rc + 4), money),
]
for i, (label, val, fmt) in enumerate(calc):
    rr = rc + 1 + i
    ws.cell(row=rr, column=1, value=label).font = bold
    c = ws.cell(row=rr, column=2, value=val)
    c.number_format = fmt
    c.border = box
    ws.cell(row=rr, column=1).border = box

# ------------------------------------------------------------------ EXPENSES
ws = wb.create_sheet('Expenses')
title_block(ws, 'Expenses',
            'Business costs and personal drawings, split so your real profit is honest.', 8)
cols = ['Date', 'Category', 'Description', 'Amount', 'Type', 'Deductible %',
        'Tax-deductible', 'Notes']
for i, c in enumerate(cols, 1):
    ws.cell(row=4, column=i, value=c)
style_header(ws, 4, len(cols))
widths(ws, {'A': 13, 'B': 18, 'C': 34, 'D': 13, 'E': 14, 'F': 14, 'G': 14, 'H': 28})
sample = [
    ('2026-10-03', 'Software', 'Figma annual plan', 12000, 'Business', 1.0, '', ''),
    ('2026-10-09', 'Equipment', 'Second monitor', 18000, 'Business', 0.5, '', 'Half work use'),
    ('2026-10-20', 'Personal', 'Owner draw', 30000, 'Personal', 0.0, '', 'Not an expense'),
]
for ri, row in enumerate(sample, start=5):
    for ci, v in enumerate(row, 1):
        cell = ws.cell(row=ri, column=ci, value=v)
        cell.border = box
        if ci == 1:
            cell.number_format = date_fmt
        if ci in (4, 7):
            cell.number_format = money
        if ci == 6:
            cell.number_format = pct
for ri in range(5, LAST + 1):
    ws.cell(row=ri, column=7, value=f'=IF(OR(D{ri}="",E{ri}<>"Business"),0,ROUND(D{ri}*F{ri},2))')
    for ci, fmt in ((4, money), (6, pct), (7, money)):
        ws.cell(row=ri, column=ci).number_format = fmt
    for ci in (6, 7):
        ws.cell(row=ri, column=ci).border = box
dv = DataValidation(type='list', formula1='"Business,Personal"', allow_blank=True)
ws.add_data_validation(dv); dv.add('E5:E%d' % LAST)
dv2 = DataValidation(type='decimal', operator='between', formula1='0', formula2='1', allow_blank=True)
ws.add_data_validation(dv2); dv2.add('F5:F%d' % LAST)

exp_reg = {}
write_summary(ws, LAST + 2, 'TOTALS', [
    ('Total expenses (all)', f'=SUM(D5:D{LAST})', money),
    ('Business expenses only', f'=SUMIF(E5:E{LAST},"Business",D5:D{LAST})', money),
    ('Personal drawings', f'=SUMIF(E5:E{LAST},"Personal",D5:D{LAST})', money),
    ('Tax-deductible total', f'=SUM(G5:G{LAST})', money),
    ('Business expenses this month', f'=SUMIFS(D5:D{LAST},E5:E{LAST},"Business",A5:A{LAST},">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1),A5:A{LAST},"<="&EOMONTH(TODAY(),0))', money),
], exp_reg)
REG['Expenses'] = exp_reg

# ------------------------------------------------------------------ TAX SET-ASIDE
ws = wb.create_sheet('Tax Set-Aside')
title_block(ws, 'Tax Set-Aside',
            'Where your tax money lives. Set aside on income, spend only from here.', 8)
cols = ['Date', 'Income source', 'Amount received', 'Set-aside rate', 'Set aside',
        'Moved to tax account?', 'Date moved', 'Notes']
for i, c in enumerate(cols, 1):
    ws.cell(row=4, column=i, value=c)
style_header(ws, 4, len(cols))
widths(ws, {'A': 13, 'B': 26, 'C': 15, 'D': 13, 'E': 14, 'F': 20, 'G': 13, 'H': 30})
TLAST = 150
for ri in range(5, TLAST + 1):
    ws.cell(row=ri, column=4, value=f'=IF(C{ri}="","",{TAX_RATE})')
    ws.cell(row=ri, column=5, value=f'=IF(C{ri}="","",ROUND(C{ri}*D{ri},2))')
    for ci, fmt in ((1, date_fmt), (3, money), (4, pct), (5, money), (7, date_fmt)):
        ws.cell(row=ri, column=ci).number_format = fmt
    for ci in range(1, 9):
        ws.cell(row=ri, column=ci).border = box
dv = DataValidation(type='list', formula1='"Yes,No,Not yet"', allow_blank=True)
ws.add_data_validation(dv); dv.add('F5:F%d' % TLAST)

tax_reg = {}
write_summary(ws, TLAST + 2, 'TAX POSITION', [
    ('Total set aside (all time)', f'=SUM(E5:E{TLAST})', money),
    ('Moved to tax account', f'=SUMIF(F5:F{TLAST},"Yes",E5:E{TLAST})', money),
    ('Still sitting in business account', f'=SUMIF(F5:F{TLAST},"Not yet",E5:E{TLAST})', money),
    ('Set aside this month', f'=SUMIFS(E5:E{TLAST},A5:A{TLAST},">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1),A5:A{TLAST},"<="&EOMONTH(TODAY(),0))', money),
    ('Months of average expenses covered', "=IFERROR(%s/%s,0)" % (
        "'Tax Set-Aside'!$B$%d" % (TLAST + 4),
        ref('Income', 'Average monthly gross (last 6 months)', inc_reg)), '0.0'),
], tax_reg)
REG['Tax Set-Aside'] = tax_reg

# ------------------------------------------------------------------ SAVINGS GOALS
ws = wb.create_sheet('Savings Goals')
title_block(ws, 'Savings Goals',
            'What you are saving for and how far along you are.', 7)
cols = ['Goal', 'Target amount', 'Current saved', 'Remaining', '% complete',
        'Target date', 'Monthly contribution needed']
for i, c in enumerate(cols, 1):
    ws.cell(row=4, column=i, value=c)
style_header(ws, 4, len(cols))
widths(ws, {'A': 30, 'B': 15, 'C': 15, 'D': 15, 'E': 13, 'F': 14, 'G': 26})
goals = [
    ('Tax buffer (6 months)', 180000, 90000, '2026-12-31'),
    ('Equipment upgrade', 60000, 15000, '2027-03-31'),
    ('Emergency fund', 250000, 40000, '2027-06-30'),
]
GLAST = 30
for ri, (name, target, saved, tdate) in enumerate(goals, start=5):
    ws.cell(row=ri, column=1, value=name).font = bold
    ws.cell(row=ri, column=2, value=target).number_format = money
    ws.cell(row=ri, column=3, value=saved).number_format = money
    for ci in range(1, 8):
        ws.cell(row=ri, column=ci).border = box
for ri in range(5, GLAST + 1):
    ws.cell(row=ri, column=4, value=f'=IF(OR(B{ri}="",C{ri}=""),"",MAX(0,B{ri}-C{ri}))').number_format = money
    ws.cell(row=ri, column=5, value=f'=IFERROR(C{ri}/B{ri},0)').number_format = pct
    ws.cell(row=ri, column=6).number_format = date_fmt
    ws.cell(row=ri, column=7, value=(
        f'=IF(OR(F{ri}="",D{ri}=""),"",IFERROR(ROUND(D{ri}/MAX(1,'
        f'(YEAR(F{ri})-YEAR(TODAY()))*12+MONTH(F{ri})-MONTH(TODAY())),0),0))')).number_format = money
    for ci in range(1, 8):
        ws.cell(row=ri, column=ci).border = box

goal_reg = {}
write_summary(ws, GLAST + 2, 'SUMMARY', [
    ('Total target', f'=SUM(B5:B{GLAST})', money),
    ('Total saved', f'=SUM(C5:C{GLAST})', money),
    ('Total remaining', f'=SUM(D5:D{GLAST})', money),
    ('Overall % complete', f'=IFERROR(SUM(C5:C{GLAST})/SUM(B5:B{GLAST}),0)', pct),
], goal_reg)
REG['Savings Goals'] = goal_reg

# ------------------------------------------------------------------ DASHBOARD
ws = wb.create_sheet('Dashboard', 0)
title_block(ws, 'Freelancer Finance Dashboard',
            'Your money at a glance. Change a number anywhere and this updates.', 6)
widths(ws, {'A': 34, 'B': 18, 'C': 4, 'D': 34, 'E': 18, 'F': 4})

# LEFT block: THIS MONTH  (cols A/B)   RIGHT block: ALL TIME (cols D/E)
ws.cell(row=4, column=1, value='THIS MONTH').font = hdr_font
ws.cell(row=4, column=1).fill = hdr_fill
ws.cell(row=4, column=2, value='Value').font = hdr_font
ws.cell(row=4, column=2).fill = hdr_fill
ws.cell(row=4, column=4, value='ALL TIME').font = hdr_font
ws.cell(row=4, column=4).fill = hdr_fill
ws.cell(row=4, column=5, value='Value').font = hdr_font
ws.cell(row=4, column=5).fill = hdr_fill

left = [
    ('Gross income', '=' + ref('Income', 'Gross this month', inc_reg), money),
    ('Business expenses', '=' + ref('Expenses', 'Business expenses this month', exp_reg), money),
    ('Net profit this month', '=B5-B6', money),
    ('Set aside for tax', '=' + ref('Income', 'Total set aside for tax', inc_reg) .replace('$B$%d' % inc_reg['Total set aside for tax'], '$B$%d' % inc_reg['Total set aside for tax']), money),
    ('Net to you this month', '=' + ref('Income', 'Net this month', inc_reg), money),
    ('Outstanding invoices', '=' + ref('Invoices', 'Outstanding', inv_reg), money),
    ('Overdue amount', '=' + ref('Invoices', 'Overdue amount', inv_reg), money),
]
# fix 'Set aside for tax' -> use 'Set aside this month' from Tax Set-Aside
left[3] = ('Set aside for tax', '=' + ref('Tax Set-Aside', 'Set aside this month', tax_reg), money)

right = [
    ('Gross income', '=' + ref('Income', 'Gross income (all time)', inc_reg), money),
    ('Total set aside for tax', '=' + ref('Income', 'Total set aside for tax', inc_reg), money),
    ('Net to you', '=' + ref('Income', 'Net to you (all time)', inc_reg), money),
    ('Tax-deductible expenses', '=' + ref('Expenses', 'Tax-deductible total', exp_reg), money),
    ('Savings goal progress', '=' + ref('Savings Goals', 'Overall % complete', goal_reg), pct),
    ('Overdue invoices count', '=' + ref('Invoices', 'Overdue count', inv_reg), '0'),
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

ws.cell(row=13, column=1, value='MONTHLY TREND').font = hdr_font
ws.cell(row=13, column=1).fill = hdr_fill
for i, c in enumerate(['Month', 'Gross income', 'Expenses', 'Net'], 1):
    ws.cell(row=14, column=i, value=c)
style_header(ws, 14, 4)
for ri in range(15, 27):
    ws.cell(row=ri, column=4, value=f'=IF(B{ri}="","",B{ri}-C{ri})').number_format = money
    ws.cell(row=ri, column=2).number_format = money
    ws.cell(row=ri, column=3).number_format = money
    for ci in range(1, 5):
        ws.cell(row=ri, column=ci).border = box

ws.cell(row=29, column=1, value='HOW TO USE THIS FILE').font = hdr_font
ws.cell(row=29, column=1).fill = hdr_fill
steps = [
    '1. Settings: enter your business name, tax rate and monthly income target. Everything else keys off this.',
    '2. Invoices: add each invoice you raise. Status and days overdue calculate themselves.',
    '3. Income: log only what actually landed in your account. Tax set-aside calculates per row.',
    '4. Expenses: mark each row Business or Personal, and set the deductible percentage.',
    '5. Tax Set-Aside: copy the set-aside figure from Income and tick it off when you move it.',
    '6. Savings Goals: set a target and a date - monthly contribution is worked out for you.',
    '7. Dashboard: open this one first every morning. It is the only sheet you need daily.',
]
for i, s in enumerate(steps):
    ws.cell(row=30 + i, column=1, value=s).font = Font(size=10)
    ws.merge_cells(start_row=30 + i, start_column=1, end_row=30 + i, end_column=5)

path = os.path.join(OUT, 'Freelancer Finance Tracker.xlsx')
wb.save(path)
print('OK ->', path)
print('sheets:', wb.sheetnames)
for sheet, reg in REG.items():
    print(' ', sheet, {k: v for k, v in list(reg.items())[:3]})
