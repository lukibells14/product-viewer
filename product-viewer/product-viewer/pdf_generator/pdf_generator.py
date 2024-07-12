# from fpdf import FPDF

# class PDF(FPDF):
#     def header(self):
#         self.set_font("Arial", "B", 12)
#         self.cell(0, 10, "Product Cart", 0, 1, "C")

#     def footer(self):
#         self.set_y(-15)
#         self.set_font("Arial", "I", 8)
#         self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

# def generate_pdf(product_data):
#     pdf = PDF()
#     pdf.set_auto_page_break(auto=True, margin=15)
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     for idx, item in enumerate(product_data, start=1):
#         if idx > 1:
#             pdf.add_page()  # Add new page for each new product

#         pdf.cell(0, 10, f"Product {idx} Details", ln=True, align='C')
#         pdf.cell(200, 10, txt=f"ID: {item['ID']}", ln=True)
#         pdf.cell(200, 10, txt=f"Database Name: {item['Database Name']}", ln=True)
#         pdf.cell(200, 10, txt=f"Product Code: {item['Product Code']}", ln=True)
#         pdf.cell(200, 10, txt=" ", ln=True)  # Add empty line for spacing

#     pdf_output = "/tmp/product_cart.pdf"
#     pdf.output(pdf_output)

#     return pdf_output

# from fpdf import FPDF

# class PDF(FPDF):
#     def header(self):
#         self.set_font("DejaVu", "B", 8)
#         self.cell(0, 10, "Product Cart", 0, 1, "C")

#     def footer(self):
#         self.set_y(-15)
#         self.set_font("DejaVu", "I", 8)
#         self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

# def generate_pdf(product_data):
#     pdf = PDF()
#     pdf.add_font('DejaVu', '', 'fonts/DejaVuSans.ttf', uni=True)
#     pdf.add_font('DejaVu', 'B', 'fonts/DejaVuSans-Bold.ttf', uni=True)
#     pdf.add_font('DejaVu', 'I', 'fonts/DejaVuSans-Oblique.ttf', uni=True)
#     pdf.add_font('DejaVu', 'BI', 'fonts/DejaVuSans-BoldOblique.ttf', uni=True)
#     pdf.set_auto_page_break(auto=True, margin=15)
#     pdf.add_page()
#     pdf.set_font("DejaVu", size=9)

#     for idx, item in enumerate(product_data, start=1):
#         if idx > 1:
#             pdf.add_page()  # Add new page for each new product

#         pdf.cell(0, 10, f"Product {idx} Details", ln=True, align='C')
#         pdf.cell(200, 10, txt=f"Product Code: {item['product_code']}", ln=True)
#         pdf.cell(200, 10, txt=f"Product Configuration: {item['product_configuration']}", ln=True)
#         pdf.cell(200, 10, txt=f"Technical Description: {item['technical_description']}", ln=True)
#         pdf.cell(200, 10, txt=f"Installation: {item['installation']}", ln=True)
#         pdf.cell(200, 10, txt=f"Colour: {item['colour']}", ln=True)
#         pdf.cell(200, 10, txt=f"Weight: {item['weight']}", ln=True)
#         pdf.cell(200, 10, txt=f"Mounting: {item['mounting']}", ln=True)
#         pdf.cell(200, 10, txt=f"Wiring: {item['wiring']}", ln=True)
#         pdf.cell(200, 10, txt=f"Notes: {item['notes']}", ln=True)
#         pdf.cell(200, 10, txt=f"Technical Data: {item['technical_data']}", ln=True)
#         pdf.cell(200, 10, txt=" ", ln=True)  # Add empty line for spacing

#     pdf_output = "/tmp/product_cart.pdf"
#     pdf.output(pdf_output)

#     return pdf_output

# from fpdf import FPDF

# class PDF(FPDF):
#     def header(self):
#         self.set_font("DejaVu", "B", 8)
#         self.cell(0, 10, "Product Cart", 0, 1, "C")

#     def footer(self):
#         self.set_y(-15)
#         self.set_font("DejaVu", "I", 8)
#         self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

# def generate_pdf(product_data, manufacturer_data):
#     pdf = PDF()
#     pdf.add_font('DejaVu', '', 'fonts/DejaVuSans.ttf', uni=True)
#     pdf.add_font('DejaVu', 'B', 'fonts/DejaVuSans-Bold.ttf', uni=True)
#     pdf.add_font('DejaVu', 'I', 'fonts/DejaVuSans-Oblique.ttf', uni=True)
#     pdf.add_font('DejaVu', 'BI', 'fonts/DejaVuSans-BoldOblique.ttf', uni=True)
#     pdf.set_auto_page_break(auto=True, margin=15)
#     pdf.add_page()
#     pdf.set_font("DejaVu", size=6)

#     # Calculate full page width
#     full_page_width = pdf.w - 2 * pdf.l_margin
#     row_height = 10

#     # Data rows
#     for idx, item in enumerate(product_data, start=1):
#         if idx > 1:
#             pdf.add_page()

#         # First row: Product Code spanning full width
#         pdf.set_fill_color(255, 255, 255)
#         pdf.cell(full_page_width, 5, "Luminaire Reference", border= 1 ,ln=1, align='C', fill=True)

#         pdf.cell(full_page_width, 5, "LOCATION:", border='RLT', ln=1, align='L', fill=True)
#         pdf.cell(full_page_width, 5, f"PRODUCT CODE: {item['product_code']}", border='RLB', ln=1, align='L', fill=True)

#         # Second row: Product Configuration
#         pdf.cell(full_page_width, 5, f"Product Configuration {item['product_configuration']}", border=1, ln=1, align='L', fill=True)

#         # Third row: Technical Description
#         pdf.cell(full_page_width, 5, "Technical Description", border=1, ln=1, align='L', fill=True)
#         pdf.set_font_size(5)  # Adjust font size for technical description
#         pdf.multi_cell(full_page_width, 3, item['technical_description'], border=1, align="L", fill=True)
#         pdf.set_font_size(6)  # Restore font size for subsequent cells

#         # Space between products
#         pdf.ln(10)

#     # Output PDF
#     pdf_output = "/tmp/product_cart.pdf"
#     pdf.output(pdf_output)

#     return pdf_output

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("DejaVu", "B", 8)
        self.cell(0, 10, "Product Cart", 0, 1, "C")

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

def generate_pdf(product_data, manufacturer_data):
    pdf = PDF()
    pdf.add_font('DejaVu', '', 'fonts/DejaVuSans.ttf', uni=True)
    pdf.add_font('DejaVu', 'B', 'fonts/DejaVuSans-Bold.ttf', uni=True)
    pdf.add_font('DejaVu', 'I', 'fonts/DejaVuSans-Oblique.ttf', uni=True)
    pdf.add_font('DejaVu', 'BI', 'fonts/DejaVuSans-BoldOblique.ttf', uni=True)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("DejaVu", size=10)

    # Calculate full page width
    full_page_width = pdf.w - 2 * pdf.l_margin
    row_height = 10

    # Add table for manufacturer data
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(full_page_width, 10, "Manufacturer Data", border=1, ln=1, align='C', fill=True)
    pdf.set_font("DejaVu", style='B', size=8)
    
    # Define table columns
    col_widths = [20, 85, 85]  # Adjust widths as needed
    
    # Column headers
    pdf.cell(col_widths[0], 10, " ", border=1, align='C')
    pdf.cell(col_widths[1], 10, "Manufacturer", border=1, align='C')
    pdf.cell(col_widths[2], 10, "Product Code", border=1, align='C')
    pdf.ln()

    # Add rows from manufacturer_data
    pdf.set_font("DejaVu", size=8)
    for index, row in enumerate(manufacturer_data, start=1):
        pdf.cell(col_widths[0], 10, str(index), border=1, align='C')
        pdf.cell(col_widths[1], 10, row['Database Name'], border=1, align='L')
        pdf.cell(col_widths[2], 10, row['Product Code'], border=1, align='L')
        pdf.ln()

    pdf.ln(10)  # Space after table

    # Data rows for products
    for idx, item in enumerate(product_data, start=3):
        if idx > 1:
            pdf.add_page()

        # First row: Product Code spanning full width
        pdf.set_fill_color(255, 255, 255)
        pdf.cell(full_page_width, 5, "Luminaire Reference", border= 1 ,ln=1, align='C', fill=True)

        pdf.cell(full_page_width, 5, "LOCATION:", border='RLT', ln=1, align='L', fill=True)
        pdf.cell(full_page_width, 5, f"PRODUCT CODE: {item['product_code']}", border='RLB', ln=1, align='L', fill=True)

        # Second row: Product Configuration
        pdf.cell(full_page_width, 5, f"Product Configuration {item['product_configuration']}", border=1, ln=1, align='L', fill=True)

        # Third row: Technical Description
        pdf.cell(full_page_width, 5, "Technical Description", border=1, ln=1, align='L', fill=True)
        pdf.set_font_size(6)  # Adjust font size for technical description
        pdf.multi_cell(full_page_width, 4, item['technical_description'], border=1, align="L", fill=True)
        pdf.set_font_size(10)  # Restore font size for subsequent cells

        # Space between products
        pdf.ln(10)

    # Output PDF
    pdf_output = "/tmp/product_cart.pdf"
    pdf.output(pdf_output)

    return pdf_output











