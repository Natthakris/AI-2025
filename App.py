import streamlit as st
import pandas as pd
import numpy as np

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="ระบบทำนายเห็ดพิษ 2025", page_icon="🍄")

st.title("🍄 Mushroom Classification Input")
st.write("กรุณาเลือกลักษณะของเห็ดเพื่อจัดเก็บข้อมูลลงใน `new_data` สำหรับการทำนาย")

# สร้าง Dictionary เก็บตัวเลือกทั้งหมดตาม Dataset (Mapping อักษรย่อเป็นคำเต็มเพื่อให้ใช้ง่าย)
options_map = {
    'cap-shape': {'b': 'bell (ระฆัง)', 'c': 'conical (กรวย)', 'x': 'convex (นูน)', 'f': 'flat (แบน)', 'k': 'knobbed (ปุ่ม)', 's': 'sunken (แอ่ง)'},
    'cap-surface': {'f': 'fibrous', 'g': 'grooves', 'y': 'scaly', 's': 'smooth'},
    'cap-color': {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'r': 'green', 'p': 'pink', 'u': 'purple', 'e': 'red', 'w': 'white', 'y': 'yellow'},
    'bruises': {'t': 'bruises (มีรอยช้ำ)', 'f': 'no (ไม่มี)'},
    'odor': {'a': 'almond', 'l': 'anise', 'c': 'creosote', 'y': 'fishy', 'f': 'foul', 'm': 'musty', 'n': 'none', 'p': 'pungent', 's': 'spicy'},
    'gill-attachment': {'a': 'attached', 'd': 'descending', 'f': 'free', 'n': 'notched'},
    'gill-spacing': {'c': 'close', 'w': 'crowded', 'd': 'distant'},
    'gill-size': {'b': 'broad (กว้าง)', 'n': 'narrow (แคบ)'},
    'gill-color': {'k': 'black', 'n': 'brown', 'b': 'buff', 'h': 'chocolate', 'g': 'gray', 'r': 'green', 'o': 'orange', 'p': 'pink', 'u': 'purple', 'e': 'red', 'w': 'white', 'y': 'yellow'},
    'stalk-shape': {'e': 'enlarging', 't': 'tapering'},
    'stalk-root': {'b': 'bulbous', 'c': 'club', 'u': 'cup', 'e': 'equal', 'z': 'rhizomorphs', 'r': 'rooted', '?': 'missing'},
    'stalk-surface-above-ring': {'f': 'fibrous', 'y': 'scaly', 'k': 'silky', 's': 'smooth'},
    'stalk-surface-below-ring': {'f': 'fibrous', 'y': 'scaly', 'k': 'silky', 's': 'smooth'},
    'stalk-color-above-ring': {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'o': 'orange', 'p': 'pink', 'e': 'red', 'w': 'white', 'y': 'yellow'},
    'stalk-color-below-ring': {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'o': 'orange', 'p': 'pink', 'e': 'red', 'w': 'white', 'y': 'yellow'},
    'veil-type': {'p': 'partial', 'u': 'universal'},
    'veil-color': {'n': 'brown', 'o': 'orange', 'w': 'white', 'y': 'yellow'},
    'ring-number': {'n': 'none', 'o': 'one', 't': 'two'},
    'ring-type': {'c': 'cobwebby', 'e': 'evanescent', 'f': 'flaring', 'l': 'large', 'n': 'none', 'p': 'pendant', 's': 'sheathing', 'z': 'zone'},
    'spore-print-color': {'k': 'black', 'n': 'brown', 'b': 'buff', 'h': 'chocolate', 'r': 'green', 'o': 'orange', 'u': 'purple', 'w': 'white', 'y': 'yellow'},
    'population': {'a': 'abundant', 'c': 'clustered', 'n': 'numerous', 's': 'scattered', 'v': 'several', 'y': 'solitary'},
    'habitat': {'g': 'grasses', 'l': 'leaves', 'm': 'meadows', 'p': 'paths', 'u': 'urban', 'w': 'waste', 'd': 'woods'}
}

# สร้างฟอร์มสำหรับกรอกข้อมูล
with st.form("mushroom_input_form"):
    st.subheader("กรอกข้อมูลลักษณะเห็ด")
    
    # แบ่งหน้าจอเป็น 3 คอลัมน์เพื่อความสวยงาม
    cols = st.columns(3)
    user_data = {}

    for i, (col_name, choices) in enumerate(options_map.items()):
        with cols[i % 3]:
            # แสดงชื่อเต็มใน UI แต่เก็บค่าเป็นอักษรย่อ (Key) ลงใน dict
            selected_label = st.selectbox(f"{col_name}", list(choices.values()))
            # หา Key จาก Value ที่เลือก
            short_code = [k for k, v in choices.items() if v == selected_label][0]
            user_data[col_name] = [short_code]

    submit_button = st.form_submit_button(label='บันทึกข้อมูลลง new_data')

# เมื่อกดปุ่ม Submit
if submit_button:
    # สร้าง DataFrame ชื่อ new_data ตามที่ต้องการ
    new_data = pd.DataFrame(user_data)
    
    st.success("บันทึกข้อมูลสำเร็จ!")
    st.subheader("ข้อมูลใน `new_data`:")
    st.dataframe(new_data)
    
    # ส่วนนี้คือการเตรียมข้อมูลก่อนส่งเข้า Model (One-Hot Encoding)
    st.info("ขั้นตอนถัดไป: นำ `new_data` ไปเข้ากระบวนการ pd.get_dummies() และ reindex ให้ตรงกับ X_columns")
