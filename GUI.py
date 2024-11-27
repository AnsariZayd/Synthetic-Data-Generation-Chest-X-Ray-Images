import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO
import zipfile


backend_url = "https://163e-34-31-102-43.ngrok-free.app/generate"


def create_zip(images, filenames):
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, "w") as zf:
        for image, filename in zip(images, filenames):
            img_buffer = BytesIO()
            image.save(img_buffer, format="PNG")
            zf.writestr(filename, img_buffer.getvalue())
    buffer.seek(0)
    return buffer


st.title("Medical Chest X-ray Image Generation")


prompt = st.text_input("Enter the description for chest X-ray generation (e.g., 'A 55-year-old man with pneumonia'): ")


seed = st.number_input("Enter a seed value for image generation (optional, default=42):", value=42)


num_inference_steps = st.number_input(
    "Enter the number of inference steps (default=35):",
    min_value=1,
    max_value=100,
    value=35
)


num_images = st.number_input(
    "Enter the number of images to generate (default=1):",
    min_value=1,
    max_value=50,
    value=1
)


if st.button("Generate X-ray"):
    if prompt:
        st.write("Generating images, please wait...")


        try:
            response = requests.post(
                backend_url,
                json={
                    "prompt": prompt,
                    "seed": int(seed),
                    "num_inference_steps": int(num_inference_steps),
                    "num_images": int(num_images)
                }
            )

            if response.status_code == 200:
                data = response.json()
                images_base64 = data["images"]


                images = [Image.open(BytesIO(base64.b64decode(img))) for img in images_base64]


                st.write("Generated Images (Showing the First 5):")
                for idx, image in enumerate(images[:5]):
                    st.image(image, caption=f"Generated Image {idx + 1}", use_column_width=True)

                # Provide a download button for all images
                st.write("Download all generated images as a zip file:")
                zip_buffer = create_zip(images, [f"image_{i+1}.png" for i in range(len(images))])
                st.download_button(
                    label="Download Images as ZIP",
                    data=zip_buffer,
                    file_name="generated_images.zip",
                    mime="application/zip"
                )
            else:
                st.error(f"Failed to generate images: {response.status_code}")
        except Exception as e:
            st.error(f"Error connecting to backend: {e}")
    else:
        st.error("Please enter a valid prompt.")
