import streamlit as st

st.set_page_config(page_title="Pseudo Code Project", layout="wide")

st.title("📚 โปรเจคระบบคิดเงินร้านค้า")
st.write("โปรเจคนี้แสดงรหัสเทียม (Pseudo Code)")

# ===== รหัสเทียม =====
pseudo = """
BEGIN
    total = 0
    items = []

    WHILE TRUE
        INPUT ชื่อสินค้า
        IF ชื่อสินค้า = "จบ"
            BREAK

        INPUT ราคา
        INPUT จำนวน
        subtotal = ราคา * จำนวน
        total = total + subtotal
        ADD ลงรายการสินค้า
    END WHILE

    IF total >= 1000
        ลด 10%
    ELSE IF total >= 500
        ลด 5%
    ELSE
        ไม่ลด
    END IF

    VAT = 7%
    แสดงใบเสร็จ
END
"""

st.subheader("รหัสเทียม (Pseudo Code)")
st.code(pseudo, language='text')
