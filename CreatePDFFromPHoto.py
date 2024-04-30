import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from PIL import Image

def create_pdf(image_path, output_path):
    image_files = [f for f in os.listdir(image_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

    pdf_file = output_path
    c = canvas.Canvas(pdf_file, pagesize=letter)

    for image_file in image_files:
        print(image_file)
        image_path2 = os.path.join(image_path,image_file)
        img = Image.open(image_path+"\\"+image_file)

        # Calculate the aspect ratio to maintain the image's original proportions
        aspect_ratio = img.width / img.height
        width = 300

        # Calculate the corresponding height based on the aspect ratio
        height = width / aspect_ratio

        # 
        c.drawInlineImage(image_path+"\\"+image_file, 5,5, width=width, height=height)

        # Add a new page for each image (optional)
        c.showPage()

    c.save()

if __name__ == "__main__":
    # Get the image path from the user
    image_path = input("Enter the path to the images: ")

    # Ensure the path exists
    if not os.path.exists(image_path):
        print("Path does not exist. Exiting.")
        exit()

    # Get the output PDF path from the user
    output_path = input("Enter the output PDF path (including filename): ")

    # Create the PDF
    create_pdf(image_path, output_path)

    print(f"PDF created successfully at: {output_path}")
