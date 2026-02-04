"""
AUDITSENSE PRO - ENTERPRISE EDITION v5.4
-----------------------------------------
Sistem Otomasi Kertas Kerja Audit Internal
PT PAL Indonesia (Persero)

Fitur Utama:
1. UI Mewah (Glassmorphism, Animations, Gradients)
2. Smart Tooltip & Format Angka (Fix Visual)
3. Advanced AI Reporting (HTML render fix)
4. Logo Visibility Fix (Header & Sidebar solved)
5. Local Processing (Keamanan Data)
"""

import streamlit as st
import pandas as pd
import io
import datetime
import base64
import time
from pathlib import Path

# ============================================================================
# BAGIAN 1: KONFIGURASI HALAMAN UTAMA
# ============================================================================
st.set_page_config(
    page_title="AuditSense Pro - Enterprise", 
    layout="wide", 
    page_icon="🛡️",
    initial_sidebar_state="expanded"
)

# ============================================================================
# BAGIAN 2: MANAJEMEN TEMA (SESSION STATE)
# ============================================================================
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

def toggle_theme():
    """Fungsi untuk mengubah tema dengan efek transisi"""
    st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
    time.sleep(0.1)
    st.rerun()

# ============================================================================
# BAGIAN 3: PALET WARNA DINAMIS (THEME ENGINE)
# ============================================================================
def get_theme_colors(theme):
    if theme == 'dark':
        return {
            'bg_main': '#0f172a',
            'bg_overlay': '#1e293b',
            'bg_sidebar': '#020617',
            'bg_card': 'rgba(30, 41, 59, 0.7)',
            'bg_tooltip': '#000000',
            'text_title': '#f8fafc',
            'text_body': '#cbd5e1',
            'text_muted': '#94a3b8',
            'border': '1px solid rgba(255, 255, 255, 0.1)',
            'shadow_card': '0 10px 15px -3px rgba(0, 0, 0, 0.5), 0 4px 6px -2px rgba(0, 0, 0, 0.3)',
            'shadow_hover': '0 20px 50px 0 rgba(0, 0, 0, 0.5), 0 10px 10px -5px rgba(0, 0, 0, 0.4)',
            'accent_primary': '#3b82f6',
            'accent_secondary': '#8b5cf6',
            'gradient_hero': 'linear-gradient(135deg, #0f172a 0%, #172554 100%)',
            'success': '#10b981',
            'warning': '#f59e0b',
            'danger': '#ef4444',
            'info': '#06b6d4',
            # Logo Filter: Putih di header gelap, tapi Original di Sidebar
            'header_logo_filter': 'brightness(0) invert(1) drop-shadow(0 2px 4px rgba(0,0,0,0.3))', 
            'sidebar_logo_filter': 'drop-shadow(0 4px 6px rgba(0,0,0,0.5))' # Tetap warna asli tapi ada shadow
        }
    else:
        return {
            'bg_main': '#f8fafc',
            'bg_overlay': '#ffffff',
            'bg_sidebar': '#ffffff',
            'bg_card': 'rgba(255, 255, 255, 0.9)',
            'bg_tooltip': '#1e293b',
            'text_title': '#0f172a',
            'text_body': '#334155',
            'text_muted': '#64748b',
            'border': '1px solid rgba(0, 0, 0, 0.05)',
            'shadow_card': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
            'shadow_hover': '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
            'accent_primary': '#2563eb',
            'accent_secondary': '#7c3aed',
            'gradient_hero': 'linear-gradient(135deg, #eff6ff 0%, #f5f3ff 100%)',
            'success': '#059669',
            'warning': '#d97706',
            'danger': '#dc2626',
            'info': '#0891b2',
            # Logo Filter: Original di Light Mode
            'header_logo_filter': 'drop-shadow(0 2px 4px rgba(0,0,0,0.1))',
            'sidebar_logo_filter': 'drop-shadow(0 4px 6px rgba(0,0,0,0.1))'
        }

c = get_theme_colors(st.session_state.theme)

# ============================================================================
# BAGIAN 4: ADVANCED CSS INJECTION (FULL LUXURY STYLE)
# ============================================================================
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;500;700;800&family=JetBrains+Mono:wght@400&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
        scroll-behavior: smooth;
    }}
    
    .stApp {{
        background-color: {c['bg_main']} !important;
        background-image: 
            radial-gradient(at 0% 0%, {c['accent_primary']}10 0px, transparent 50%), 
            radial-gradient(at 100% 100%, {c['accent_secondary']}10 0px, transparent 50%);
        background-attachment: fixed;
    }}
    
    header {{visibility: hidden;}}
    
    /* Typography Colors */
    h1, h2, h3, h4, h5, h6 {{
        font-family: 'Outfit', sans-serif !important;
        color: {c['text_title']} !important;
        letter-spacing: -0.5px;
    }}
    
    p, span, label, div, .stMarkdown p {{
        color: {c['text_body']};
    }}

    /* Animations */
    @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes slideUp {{ from {{ opacity: 0; transform: translateY(20px); }} to {{ opacity: 1; transform: translateY(0); }} }}

    /* Sidebar Styling */
    [data-testid="stSidebar"] {{
        background-color: {c['bg_sidebar']} !important;
        border-right: 1px solid {c['bg_overlay']}; 
        box-shadow: 2px 0 10px rgba(0,0,0,0.05);
    }}
    
    [data-testid="stFileUploader"] {{
        background: {c['bg_overlay']};
        border-radius: 12px;
        padding: 15px;
        border: 1px dashed {c['accent_primary']};
        transition: all 0.3s ease;
    }}
    [data-testid="stFileUploader"]:hover {{
        border-color: {c['accent_secondary']};
        background: {c['bg_main']};
    }}
    
    .stFileUploader div, .stFileUploader span, .stFileUploader small {{
        color: {c['text_body']} !important;
    }}
    [data-testid="stFileUploaderFileName"] {{
        color: {c['text_title']} !important;
        font-weight: 600;
    }}

    /* Hero Section */
    .hero-container {{
        background: {c['gradient_hero']};
        border-radius: 24px;
        padding: 3.5rem 2rem;
        text-align: center;
        margin-bottom: 2.5rem;
        border: {c['border']};
        box-shadow: {c['shadow_card']};
        position: relative;
        overflow: hidden;
        animation: slideUp 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
    }}
    
    .hero-title {{
        font-size: 3.2rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, {c['accent_primary']}, {c['accent_secondary']});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem !important;
    }}
    
    .hero-subtitle {{
        font-size: 1.1rem;
        color: {c['text_muted']} !important;
        font-weight: 500;
    }}

    /* KPI Cards */
    .kpi-card {{
        background: {c['bg_card']};
        backdrop-filter: blur(12px);
        border: {c['border']};
        border-radius: 20px;
        padding: 1.5rem 1rem;
        height: 190px;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        box-shadow: {c['shadow_card']};
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        position: relative;
        overflow: visible; 
        z-index: 1;
    }}
    
    .kpi-card:hover {{
        transform: translateY(-8px) scale(1.02);
        box-shadow: {c['shadow_hover']};
        border-color: {c['accent_primary']};
        z-index: 10;
    }}
    
    .kpi-card::after {{
        content: '';
        position: absolute;
        top: 0;
        left: 30%;
        right: 30%;
        height: 4px;
        background: linear-gradient(90deg, transparent, {c['accent_primary']}, transparent);
        border-radius: 0 0 10px 10px;
        opacity: 0.7;
    }}

    .kpi-icon {{
        font-size: 2.5rem;
        margin-bottom: 12px;
        filter: drop-shadow(0 4px 4px rgba(0,0,0,0.1));
    }}
    
    .kpi-label {{
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 700;
        color: {c['text_muted']} !important;
        margin-bottom: 8px;
    }}
    
    .kpi-value {{
        font-family: 'Outfit', sans-serif;
        font-size: 1.8rem;
        font-weight: 800;
        color: {c['text_title']} !important;
        width: 100%;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        cursor: help;
        padding: 0 5px;
    }}

    /* Tooltip */
    .kpi-card .tooltip-box {{
        visibility: hidden;
        width: 250px;
        background-color: #0f172a !important; 
        color: #ffffff !important; 
        text-align: center;
        border-radius: 8px;
        padding: 10px 15px;
        position: absolute;
        z-index: 999999; 
        bottom: 105%;
        left: 50%;
        transform: translateX(-50%) translateY(10px);
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        font-weight: 500;
        opacity: 0;
        transition: opacity 0.2s;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        border: 1px solid {c['accent_primary']};
        pointer-events: none;
        white-space: normal; 
        word-wrap: break-word;
        line-height: 1.4;
    }}
    
    .kpi-card:hover .tooltip-box {{
        visibility: visible;
        opacity: 1;
        transform: translateX(-50%) translateY(0px);
    }}
    
    .kpi-card .tooltip-box::after {{
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -6px;
        border-width: 6px;
        border-style: solid;
        border-color: #0f172a transparent transparent transparent;
    }}

    /* Buttons */
    .stButton button, .stDownloadButton button {{
        background: linear-gradient(90deg, {c['accent_primary']}, {c['accent_secondary']});
        color: white !important;
        border: none;
        padding: 0.8rem 1.5rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.95rem;
        width: 100%;
        box-shadow: 0 4px 15px {c['accent_primary']}40;
        transition: all 0.3s ease;
    }}
    
    .stButton button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 8px 25px {c['accent_primary']}60;
        filter: brightness(1.1);
    }}

    /* Report & Tables */
    .report-box {{
        background: {c['bg_overlay']};
        border-left: 5px solid {c['warning']};
        border-radius: 16px;
        padding: 2rem;
        margin: 3rem 0;
        box-shadow: {c['shadow_card']};
        animation: fadeIn 1s ease;
        position: relative;
    }}
    
    .stDataFrame {{
        border-radius: 12px;
        border: {c['border']};
        box-shadow: {c['shadow_card']};
        overflow: hidden;
    }}

    /* Footer */
    .footer-container {{
        text-align: center;
        padding: 3rem 1rem;
        margin-top: 5rem;
        border-top: 1px solid {c['border']};
        color: {c['text_muted']};
        font-size: 0.85rem;
        background: {c['bg_overlay']};
        border-radius: 20px 20px 0 0;
    }}
</style>
""", unsafe_allow_html=True)

# ============================================================================
# BAGIAN 5: UTILITY FUNCTIONS (FUNGSI PINTAR)
# ============================================================================

@st.cache_data
def get_img_as_base64(file_path):
    try:
        possible_names = [file_path, file_path.replace("-", " "), file_path.replace(" ", "-")]
        for name in possible_names:
            full_path = Path(__file__).parent / "logo" / name
            if full_path.exists():
                with open(full_path, "rb") as f: data = f.read()
                return base64.b64encode(data).decode()
        return None
    except: return None

def clean_numeric(x):
    try:
        if pd.isna(x): return 0.0
        s = str(x).strip().replace('Rp', '').replace(' ', '')
        if s.startswith('(') and s.endswith(')'):
            s = '-' + s[1:-1]
        if ',' in s and '.' in s: 
            s = s.replace('.', '').replace(',', '.') 
        elif ',' in s: 
            s = s.replace(',', '.') 
        return float(s)
    except: return 0.0

def fmt_indo(x):
    try: 
        val = float(x)
        if val == 0: return "0"
        return f"{val:,.2f}".replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")
    except: return str(x)

def fmt_smart(x):
    try:
        val = float(x)
        abs_val = abs(val)
        if abs_val >= 1_000_000_000_000:
            formatted = f"{val/1_000_000_000_000:,.2f} T"
        elif abs_val >= 1_000_000_000:
            formatted = f"{val/1_000_000_000:,.2f} M"
        elif abs_val >= 1_000_000:
            formatted = f"{val/1_000_000:,.2f} Jt"
        else:
            return fmt_indo(val)
        return formatted.replace(".", ",") 
    except: return str(x)

def to_excel(df, sheet_name):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name=sheet_name)
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]
        header_fmt = workbook.add_format({
            'bold': True, 'fg_color': '#1e293b', 'font_color': 'white', 
            'border': 1, 'align': 'center', 'valign': 'vcenter'
        })
        num_fmt = workbook.add_format({'num_format': '#,##0.00'})
        for i, col in enumerate(df.columns):
            max_len = max(df[col].astype(str).str.len().max(), len(col)) + 4
            worksheet.set_column(i, i, min(max_len, 60))
            if pd.api.types.is_numeric_dtype(df[col]):
                 worksheet.set_column(i, i, min(max_len, 60), num_fmt)
    return output.getvalue()

# ============================================================================
# BAGIAN 6: SIDEBAR
# ============================================================================
with st.sidebar:
    logo_sistem = get_img_as_base64("icon-sistem.png")
    if logo_sistem:
        # LOGO SIDEBAR FIX: Menggunakan filter khusus yang tidak merusak warna
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 1.5rem; animation: fadeIn 1s;">
            <img src="data:image/png;base64,{logo_sistem}" style="height: 90px; filter: {c['sidebar_logo_filter']}; margin-bottom: 10px;">
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"<h3 style='text-align:center; margin-bottom:1.5rem; font-size:1.2rem;'>Panel Kontrol</h3>", unsafe_allow_html=True)
    
    col_t1, col_t2 = st.columns([1, 4])
    with col_t1: st.write("🌙" if st.session_state.theme == 'dark' else "☀️")
    with col_t2: 
        if st.button("Ubah Tampilan", key='theme_btn'): toggle_theme()

    st.divider()

    with st.expander("📂 1. Unggah Data", expanded=True):
        st.caption("Mendukung format .xlsx")
        file_b = st.file_uploader("📊 File Anggaran", type=['xlsx'], key='budget_up')
        file_p = st.file_uploader("🛒 File PO", type=['xlsx'], key='po_up')

    map_b, map_p = {}, {}
    if file_b and file_p:
        with st.expander("🔧 2. Konfigurasi Kolom", expanded=True):
            try:
                df_b_head = pd.read_excel(file_b, nrows=0)
                df_p_head = pd.read_excel(file_p, nrows=0)
                cols_b = df_b_head.columns.tolist()
                cols_p = df_p_head.columns.tolist()
                
                def find_col(cols, keys):
                    for i, c in enumerate(cols):
                        if any(k in c.lower() for k in keys): return i
                    return 0

                st.markdown("##### Mapping Anggaran")
                map_b['acc'] = st.selectbox("Account:", cols_b, index=find_col(cols_b, ['analytic', 'account', 'akun', 'kode']))
                map_b['po'] = st.selectbox("PO Amount:", cols_b, index=find_col(cols_b, ['po amount', 'po', 'nilai po']))
                map_b['jur'] = st.selectbox("Journal:", cols_b, index=find_col(cols_b, ['journal', 'jur', 'gl']))
                map_b['rem'] = st.selectbox("Remaining:", cols_b, index=find_col(cols_b, ['remain', 'sisa', 'left']))
                
                st.divider()
                st.markdown("##### Mapping Purchase Order")
                map_p['acc'] = st.selectbox("Account (PO):", cols_p, index=find_col(cols_p, ['account', 'akun', 'analytic']))
                map_p['sub'] = st.selectbox("Subtotal:", cols_p, index=find_col(cols_p, ['subtotal', 'total', 'amount', 'harga']))
            except Exception as e:
                st.error("Terjadi kesalahan membaca format file. Pastikan file tidak rusak.")

    st.divider()
    st.markdown(f"""
    <div style='text-align:center; font-size:0.8rem; color:{c['text_muted']};'>
        <strong>AuditSense Pro v5.4</strong><br>
        Ultimate Release<br>
        © 2026 SPI PT PAL Indonesia
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# BAGIAN 7: HEADER UTAMA
# ============================================================================
logo_pal = get_img_as_base64("logo-pal.png")
if logo_pal:
    st.markdown(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 30px; animation: slideUp 0.8s;">
        <img src="data:image/png;base64,{logo_pal}" style="height: 80px; object-fit: contain;">
    </div>
    """, unsafe_allow_html=True)

logo_detektif = get_img_as_base64("detektif.png")
# HEADER LOGO FIX: Menggunakan filter dinamis agar terlihat di Light Mode
detektif_html = f'<img src="data:image/png;base64,{logo_detektif}" style="height: 65px; filter: {c["header_logo_filter"]}; margin-right:15px; vertical-align: middle;">' if logo_detektif else '🛡️ '

st.markdown(f"""
<div class="hero-container">
    <div class="hero-title">
        {detektif_html} AuditSense Pro
    </div>
    <div class="hero-subtitle">
        Sistem Otomasi Kertas Kerja Audit Internal | PT PAL Indonesia
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# BAGIAN 8: LOGIKA APLIKASI
# ============================================================================

if not (file_b and file_p):
    st.markdown(f"""
    <div style="text-align: center; margin: 3rem 0; animation: fadeIn 1.5s;">
        <h2 style="font-size: 2.2rem; margin-bottom: 1rem;">Selamat Datang, Auditor! 👋</h2>
        <p style="font-size: 1.1rem; color: {c['text_muted']}; max-width: 750px; margin: 0 auto; line-height: 1.6;">
            Platform ini dirancang untuk mempercepat proses rekonsiliasi data anggaran dan PO.
            Silakan unggah file data Anda di sidebar.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    def feature(icon, title, text):
        st.markdown(f"""
        <div style="background:{c['bg_card']}; padding:25px; border-radius:16px; border:{c['border']}; text-align:center; height:100%; transition:transform 0.3s; box-shadow:{c['shadow_card']};">
            <div style="font-size:3.5rem; margin-bottom:15px;">{icon}</div>
            <div style="font-weight:700; font-size:1.3rem; color:{c['text_title']}; margin-bottom:10px;">{title}</div>
            <div style="color:{c['text_body']}; font-size:0.95rem;">{text}</div>
        </div>""", unsafe_allow_html=True)
    with c1: feature("⚡", "Proses Cepat", "Analisis ribuan data dalam hitungan detik.")
    with c2: feature("🎯", "Akurasi Tinggi", "Deteksi Budget Overrun dan Ghost Expense.")
    with c3: feature("🔒", "Data Aman", "Pemrosesan lokal di perangkat Anda.")

else:
    with st.spinner("🔄 Sedang memproses data..."):
        try:
            df_b = pd.read_excel(file_b, engine='openpyxl')
            df_p = pd.read_excel(file_p, engine='openpyxl')
            
            df_b = df_b[~df_b[map_b['acc']].astype(str).str.contains('Total|Jumlah|Grand', case=False, na=False)]
            df_p = df_p[~df_p[map_p['acc']].astype(str).str.contains('Total|Jumlah|Grand', case=False, na=False)]
            
            cols_num_b = [map_b['po'], map_b['jur'], map_b['rem']]
            for col in cols_num_b: 
                df_b[col] = df_b[col].apply(clean_numeric).astype(float)
            df_p[map_p['sub']] = df_p[map_p['sub']].apply(clean_numeric).astype(float)
            
            df_b['key'] = df_b[map_b['acc']].astype(str).str.strip().str.upper()
            df_p['key'] = df_p[map_p['acc']].astype(str).str.strip().str.upper()
            
            df_b['used'] = df_b[map_b['po']] + df_b[map_b['jur']]
            b_agg = df_b.groupby('key')[['used', map_b['po'], map_b['jur']]].sum().reset_index()
            p_agg = df_p.groupby('key')[map_p['sub']].sum().reset_index()
            
            merged = pd.merge(b_agg, p_agg, on='key', how='outer').fillna(0)
            merged = merged[~merged['key'].isin(['NAN', '0', '', 'NONE', 'NAN', 'TOTAL'])]
            merged['diff'] = merged['used'] - merged[map_p['sub']]
            
            kka2 = merged.rename(columns={
                'key': 'Kode Akun', map_b['po']: 'PO (Anggaran)', map_b['jur']: 'Jurnal (Anggaran)',
                'used': 'Anggaran Terpakai', map_p['sub']: 'Realisasi PO', 'diff': 'Selisih'
            })
            kka2 = kka2[['Kode Akun', 'PO (Anggaran)', 'Jurnal (Anggaran)', 'Anggaran Terpakai', 'Realisasi PO', 'Selisih']]
            kka1 = df_b[df_b[map_b['rem']] < 0].copy()
            kka2a = df_p[(df_p[map_p['sub']] > 0) & (df_p['key'].str.match(r'^(NAN|NONE|\s*|0|\-|RP)$', case=False))].copy()

            # --- KPI CARDS ---
            st.markdown("<br>", unsafe_allow_html=True)
            k1, k2, k3, k4 = st.columns(4)
            
            def kpi_html(icon, label, val_raw, color=c['text_title'], border_col=None, is_currency=False):
                border_style = f"border-bottom: 4px solid {border_col};" if border_col else ""
                if is_currency:
                    display_val = fmt_smart(val_raw)
                    tooltip_val = f"Rp {fmt_indo(val_raw)}"
                else:
                    display_val = str(int(val_raw))
                    tooltip_val = str(int(val_raw))
                    
                return f"""
                <div class="kpi-card" style="{border_style}">
                    <div class="kpi-icon">{icon}</div>
                    <div class="kpi-label">{label}</div>
                    <div class="kpi-value" style="color:{color} !important">
                        {display_val}
                        <span class="tooltip-box">{tooltip_val}</span>
                    </div>
                </div>
                """

            with k1: st.markdown(kpi_html("📋", "TOTAL AKUN", len(kka2), border_col=c['info'], is_currency=False), unsafe_allow_html=True)
            with k2: st.markdown(kpi_html("⚖️", "TOTAL SELISIH", kka2['Selisih'].sum(), c['success'] if kka2['Selisih'].sum() == 0 else c['danger'], c['danger'], is_currency=True), unsafe_allow_html=True)
            with k3: st.markdown(kpi_html("📉", "OVER BUDGET", len(kka1), c['warning'], is_currency=False), unsafe_allow_html=True)
            with k4: st.markdown(kpi_html("👻", "GHOST EXPENSE", len(kka2a), c['danger'], is_currency=False), unsafe_allow_html=True)

            # --- EXECUTIVE REPORT ---
            if not kka2.empty:
                top_diff = kka2.loc[kka2['Selisih'].abs().idxmax()]
                st.markdown(f"""
                <div class="report-box">
                    <h4 style="margin-top:0; color:{c['accent_secondary']}; display:flex; align-items:center; gap:10px;">
                        📢 Laporan Analisis Eksekutif
                    </h4>
                    <div style="color:{c['text_body']}; line-height: 1.6; font-size: 1rem;">
                        <p>
                            Analisis untuk periode <strong>{datetime.datetime.now().strftime('%B %Y')}</strong> telah selesai.
                            Berdasarkan data yang diunggah, sistem mendeteksi:
                        </p>
                        <ul style="margin-bottom:20px;">
                            <li>Terdapat <strong style="color:{c['warning']}">{len(kka1)} akun</strong> yang melebihi pagu anggaran (Overbudget).</li>
                            <li>Ditemukan <strong style="color:{c['danger']}">{len(kka2a)} transaksi anomali</strong> yang tidak memiliki kode akun valid (Ghost Expense).</li>
                        </ul>
                        <div style="padding:15px; background:{c['bg_main']}; border-radius:10px; border-left:4px solid {c['danger']};">
                            <strong style="color:{c['text_title']}">🔴 Temuan Prioritas:</strong><br>
                            Akun <span style="color:{c['accent_primary']}; font-weight:700;">{top_diff['Kode Akun']}</span> 
                            memiliki varians tertinggi sebesar <strong style="color:{c['danger']}">Rp {fmt_indo(abs(top_diff['Selisih']))}</strong>.
                            Disarankan untuk segera melakukan penelusuran pada akun tersebut.
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            # --- TABS ---
            t1, t2, t3 = st.tabs(["📊 KKA 2: Rekonsiliasi", "📉 KKA 1: Over Budget", "👻 KKA 2a: Ghost Expense"])
            
            def color_rows(val):
                try:
                    v = float(val)
                    if v < -1: return f'background-color: #fee2e2; color: #991b1b; font-weight: 600;'
                    elif v > 1: return f'background-color: #dcfce7; color: #166534; font-weight: 600;'
                    return ''
                except: return ''

            with t1:
                c1, c2 = st.columns([3, 1])
                with c1: st.caption("Rekonsiliasi Anggaran vs Realisasi Fisik")
                with c2: st.download_button("📥 Unduh Excel", to_excel(kka2, "KKA2_Recon"), "KKA2_Recon.xlsx", type="primary", use_container_width=True)
                fmt_dict = {col: fmt_indo for col in kka2.columns if col != 'Kode Akun'}
                st.dataframe(kka2.style.format(fmt_dict).map(color_rows, subset=['Selisih']), use_container_width=True, height=500)

            with t2:
                c1, c2 = st.columns([3, 1])
                with c1: 
                    if not kka1.empty: st.error(f"⚠️ {len(kka1)} Akun Melebihi Anggaran!")
                    else: st.success("✅ Aman")
                with c2: st.download_button("📥 Unduh Excel", to_excel(kka1, "KKA1"), "KKA1_Overbudget.xlsx", use_container_width=True)
                if not kka1.empty: st.dataframe(kka1.style.format({col: fmt_indo for col in kka1.select_dtypes(include=['number']).columns}), use_container_width=True)

            with t3:
                c1, c2 = st.columns([3, 1])
                with c1: 
                    if not kka2a.empty: st.error(f"⚠️ {len(kka2a)} Transaksi Tanpa Akun!")
                    else: st.success("✅ Aman")
                with c2: st.download_button("📥 Unduh Excel", to_excel(kka2a, "KKA2a"), "KKA2a_Ghost.xlsx", use_container_width=True)
                if not kka2a.empty: st.dataframe(kka2a.style.format({col: fmt_indo for col in kka2a.select_dtypes(include=['number']).columns}), use_container_width=True)

        except Exception as e:
            st.error(f"Terjadi kesalahan teknis: {e}")
            st.warning("Tips: Jika terjadi Memory Error, coba gunakan file Excel yang lebih kecil.")

# ============================================================================
# BAGIAN 9: FOOTER
# ============================================================================
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown(f"""
<div class="footer-container">
    <div style="font-weight: 600; margin-bottom: 10px; font-size:1rem; color: {c['text_title']};">
        AuditSense Pro v5.4 (Enterprise Edition)
    </div>
    <div style="font-size: 0.9rem;">
        Sistem Otomasi Audit Internal Terintegrasi<br>
        Dikembangkan oleh Satuan Pengawasan Intern (SPI)<br>
        <strong>PT PAL Indonesia (Persero)</strong>
    </div>
    <div style="margin-top: 20px; font-size: 0.8rem; opacity: 0.7;">
        🔒 Secure Local Processing Environment | ⚡ AI-Powered Analytics
    </div>
</div>
""", unsafe_allow_html=True)