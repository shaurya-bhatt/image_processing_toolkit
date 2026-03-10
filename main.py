from utils import load_image, save_image
from grayscale import convert_to_grayscale
from blur import blur_image
from edge import detect_edges

def main():
    print("Loading Image...")
    img=load_image("image.jpeg")

    print("Converting to Gray Scale...")
    gray=convert_to_grayscale(img)

    print("Applying blurr...")
    blurred=blur_image(gray)

    print("Detecting Edges...")
    edge=detect_edges(blurred)

    print("Saving images...")
    save_image(gray,"gray.jpeg")
    save_image(blurred,"blur.jpeg")
    save_image(edge,"edges.jpeg")

    print("Processing Completed!")
    
if __name__ == "__main__":
    main()