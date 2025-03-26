import face_recognition
from PIL import Image


def main(count, identities):
    for i in range(count):
        create_identities(identities[i])

def create_identities(identity):
    # Find faces in image
    image = face_recognition.load_image_file(identity["image"])

    # Crop out faces 
    face_locations = face_recognition.face_locations(image)
    for face in face_locations:
        top, right, bottom, left = face
    face_image = image[top:bottom, left:right]

    # Display face
    pil_image = Image.fromarray(face_image)
    pil_image.show()
    # Create identity

identities = [
    {
        "image":"andrey.jpg",
        "name": "Veronica"
    },
    {
        "image":"clare.jpg",
        "name": "Clare"
    },
    {
        "image":"jakob2.jpg",
        "name": "Ledia" }
]

main(3,identities)
