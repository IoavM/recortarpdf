import streamlit as st
from pypdf import PdfReader, PdfWriter
from io import BytesIO

st.set_page_config(page_title="Recortar PDF", page_icon="✂️")

st.title("✂️ Recortar un PDF por páginas")
st.write("Carga un archivo PDF y selecciona el rango de páginas que quieres extraer.")

uploaded_file = st.file_uploader("📄 Cargar PDF", type="pdf")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    total_pages = len(reader.pages)
    st.info(f"Este PDF tiene {total_pages} páginas.")

    start_page = st.number_input("Página inicial", min_value=1, max_value=total_pages, value=1)
    end_page = st.number_input("Página final", min_value=1, max_value=total_pages, value=total_pages)

    if start_page > end_page:
        st.error("⚠️ La página inicial no puede ser mayor que la final.")
    else:
        if st.button("Recortar PDF"):
            writer = PdfWriter()
            for i in range(start_page - 1, end_page):
                writer.add_page(reader.pages[i])

            output = BytesIO()
            writer.write(output)
            output.seek(0)

            st.success("✅ PDF recortado listo para descargar")
            st.download_button(
                label="📥 Descargar PDF recortado",
                data=output,
                file_name="pdf_recortado.pdf",
                mime="application/pdf"
            )
