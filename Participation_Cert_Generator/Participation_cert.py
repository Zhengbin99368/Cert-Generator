import os
from PIL import Image, ImageDraw, ImageFont

def generate_certificates():
    # --- CONFIGURATION ---
    # Using 'r' before the string ensures Windows backslashes are read correctly
    template_path = r"C:\Cert_Generator\Participation_Cert_Generator\participation.jpeg"
    font_path = "C:\Cert_Generator\Participation_Cert_Generator\ARIAL.TTF"            
    names_file = r"C:\Cert_Generator\Participation_Cert_Generator\Participation_names.txt"
    output_dir = r"C:\Cert_Generator\Generated_Participation_JPEGs"
    
    # Font size and text color (RGB)
    font_size = 120
    text_color = (0, 0, 0)              # Black
    
    # Y-coordinate for the text (Adjust this based on your template design!)
    # X-coordinate is calculated automatically to center the text.
    y_position = 750                    
    # ---------------------

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load the font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print(f"Error: Could not load font '{font_path}'. Make sure the file exists or provide a full path like C:\\Windows\\Fonts\\arial.ttf")
        return

    # Read the names from the text file
    try:
        with open(names_file, 'r', encoding='utf-8') as f:
            # Strip whitespace ONLY at the very beginning and end of the line. 
            # This safely keeps all spaces between first and last names!
            names = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"Error: Could not find '{names_file}'.")
        return

    print(f"Starting generation for {len(names)} certificates...\n")

    # Generate a certificate for each name
    for name in names:
        # 1. Open the base template
        img = Image.open(template_path).convert('RGB') 
        draw = ImageDraw.Draw(img)
        image_width, image_height = img.size

        # 2. Calculate text size to perfectly center it
        bbox = draw.textbbox((0, 0), name, font=font)
        text_width = bbox[2] - bbox[0]
        
        x_position = (image_width - text_width) / 2

        # 3. Draw the text onto the image
        draw.text((x_position, y_position), name, fill=text_color, font=font)

        # 4. Save as JPEG (Spaces are now preserved in the file name)
        output_path = os.path.join(output_dir, f"{name}.jpeg")
        
        # Save with high quality to prevent text compression artifacts
        img.save(output_path, "JPEG", quality=95)
        print(f"Created: {output_path}")

    print("\nSuccess! All certificates have been generated.")

if __name__ == "__main__":
    generate_certificates()