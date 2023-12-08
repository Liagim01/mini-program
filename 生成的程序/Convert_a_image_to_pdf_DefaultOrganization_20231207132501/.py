def convert_to_pdf(self):
    if hasattr(self, 'directory'):
        images = [f for f in os.listdir(self.directory) if f.endswith('.jpg')]
        if images:
            output_pdf = os.path.join(self.directory, 'output.pdf')
            with open(output_pdf, "wb") as f:
                f.write(img2pdf.convert([os.path.join(self.directory, image) for image in images]))
            self.status_label.config(text="Conversion successful. PDF saved as output.pdf")
        else:
            self.status_label.config(text="No JPG images found in the directory.")
    else:
        self.status_label.config(text="Please select a directory first.")