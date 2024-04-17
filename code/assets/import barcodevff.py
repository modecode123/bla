import barcode
from barcode.writer import ImageWriter

def generate_barcode(product_name, barcode_type='CODE39', output_filename='barcode'):
    """
    Generate a barcode image for a product.

    Args:
        product_name (str): Name of the product to encode in the barcode.
        barcode_type (str): Type of barcode to generate (default: 'code128').
        output_filename (str): Filename for the generated barcode image (without extension).

    Returns:
        str: Filename of the generated barcode image.
    """
    # Generate barcode
    barcode_class = barcode.get_barcode_class(barcode_type)
    barcode_instance = barcode_class(product_name, writer=ImageWriter)
    filename = f"{output_filename}_{barcode_type}"
    barcode_instance.save(filename)

    return filename + '.png'

# Example usage
product_name = "example Product"
barcode_type = 'CODE39'  # You can change this to other supported barcode types
output_filename = 'example_product_barcode'

barcode_image_filename = generate_barcode(product_name, barcode_type, output_filename)
print(f"Barcode image saved as {barcode_image_filename}")
