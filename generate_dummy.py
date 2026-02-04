import pandas as pd
import numpy as np

# --- 1. MEMBUAT DATA ANGGARAN (BUDGET) ---
data_budget = {
    'Kode Akun': [
        '51001', '51002', '51003', '51004', '51005', 
        '61001', '61002', '61003', '61004', '61005'
    ],
    'Deskripsi': [
        'Beban Gaji', 'Beban Listrik', 'Beban Sewa', 'Beban Iklan', 'Beban Training',
        'Material Besi', 'Material Cat', 'Jasa Las', 'Suku Cadang', 'Transportasi'
    ],
    'Nilai PO (Commitment)': [
        100_000_000, 50_000_000, 200_000_000, 25_000_000, 10_000_000,
        500_000_000, 150_000_000, 75_000_000, 0, 15_000_000
    ],
    'Nilai Jurnal (Actual)': [
        100_000_000, 45_000_000, 200_000_000, 30_000_000, 0,
        450_000_000, 150_000_000, 80_000_000, 0, 20_000_000
    ]
}

df_budget = pd.DataFrame(data_budget)

# Hitung Sisa Anggaran (Total Pagu - Terpakai)
# Kita buat skenario Overbudget manual untuk akun tertentu
# Akun 51004 (Iklan) & 61003 (Jasa Las) & 61005 (Transport) kita buat Overbudget (Minus)
df_budget['Sisa Anggaran'] = [
    50_000_000, 5_000_000, 0, -5_000_000, 10_000_000,
    50_000_000, 0, -5_000_000, 100_000_000, -5_000_000
]

# Tambahkan baris "Total" (Untuk ngetes fitur filter sampah berjalan atau tidak)
row_total = pd.DataFrame([{
    'Kode Akun': 'Grand Total', 'Deskripsi': '', 
    'Nilai PO (Commitment)': 1_125_000_000, 'Nilai Jurnal (Actual)': 1_075_000_000, 
    'Sisa Anggaran': 200_000_000
}])
df_budget = pd.concat([df_budget, row_total], ignore_index=True)

# --- 2. MEMBUAT DATA REALISASI (PO) ---
data_po = {
    'Account Code': [
        # Match Sempurna
        '51001', '51002', '51003', 
        # Selisih (PO di data ini lebih besar/kecil dari anggaran)
        '51004', '61001', 
        # Ghost Expense (Kode Akun Aneh/Kosong/Strip)
        '-', '0', 'NAN',
        # Valid Account tapi tidak ada di Budget
        '99999' 
    ],
    'Line Description': [
        'Pembayaran Gaji Jan', 'Tagihan PLN', 'Sewa Gedung Thn 2026',
        'Iklan Instagram', 'Beli Plat Baja',
        'Pembelian Tanpa Akun 1', 'Pembelian Tanpa Akun 2', 'Error System',
        'Biaya Tak Terduga'
    ],
    'Subtotal Amount': [
        200_000_000, 95_000_000, 400_000_000, # Match (Total PO + Jurnal)
        60_000_000, 900_000_000, # Selisih Besar
        5_000_000, 2_500_000, 1_000_000, # Ghost Expense
        15_000_000 # Unregistered
    ]
}

df_po = pd.DataFrame(data_po)

# Tambahkan baris "Total" juga di sini
row_total_po = pd.DataFrame([{
    'Account Code': 'Total Report', 'Line Description': '', 'Subtotal Amount': 1_678_500_000
}])
df_po = pd.concat([df_po, row_total_po], ignore_index=True)

# --- 3. EXPORT KE EXCEL ---
print("Sedang membuat file dummy...")
df_budget.to_excel("budget_dummy.xlsx", index=False)
df_po.to_excel("po_dummy.xlsx", index=False)
print("✅ Berhasil! File 'budget_dummy.xlsx' dan 'po_dummy.xlsx' telah dibuat.")
print("   - Gunakan file ini untuk testing aplikasi.")
print("   - Cek fitur 'Over Budget' (ada 3 akun minus).")
print("   - Cek fitur 'Ghost Expense' (ada akun '-', '0', 'NAN').")