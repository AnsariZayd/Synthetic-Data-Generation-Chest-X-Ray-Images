# Synthetic Chest X-Ray Image Generation System

## Overview

This repository contains the implementation of a synthetic chest X-ray image generation system using a diffusion-based generative model fine-tuned with Low-Rank Adaptation (LoRA). The system enables the generation of high-quality, clinically accurate synthetic chest X-ray images conditioned on textual prompts. It is designed for use in medical research, training AI diagnostic models, and augmenting datasets for medical education.

---

## Features

- **Text-Conditioned Image Generation**: Generate chest X-ray images based on user-defined clinical prompts, such as "A 55-year-old man with pneumonia."
- **Fine-Tuned Model**: A diffusion-based model fine-tuned using LoRA, optimized for medical imaging tasks with minimal computational overhead.
- **User-Friendly Interface**: An intuitive front-end built with Streamlit for seamless interaction, allowing users to customize parameters and visualize results in real time.
- **Batch Processing**: Generate multiple images at once with options for batch downloads in a compressed ZIP file.
- **Scalable Backend**: A robust architecture using Flask, pyngrok, PyTorch, and diffusers, ensuring secure, efficient, and scalable performance.

---

## System Components

### **Model Architecture**
- Built on Stable Diffusion, incorporating advanced components:
  - **Text Encoder**: Encodes prompts into high-dimensional embeddings using CLIP.
  - **UNet with LoRA**: Processes latent representations and refines noisy images using attention mechanisms.
  - **Variational Autoencoder (VAE)**: Compresses and reconstructs images while preserving fidelity.
  - **Denoising Diffusion Scheduler**: Manages noise addition and removal during the image generation process.
- LoRA integration ensures efficient fine-tuning by modifying only low-rank matrices within the UNet's attention layers.

### **Frontend**
- Developed using Streamlit for an interactive and user-friendly experience.
- Features include:
  - Text-based input for clinical descriptions.
  - Configurable parameters: seed values, inference steps, and the number of images.
  - Real-time visualization of generated images.
  - Batch download functionality for efficient data handling.

### **Backend**
- Flask-based API for handling requests and communicating with the model.
- Secure remote access enabled through pyngrok.
- PyTorch and diffusers library for managing the model's operations and diffusion process.

---

## Key Performance Metrics

- **FID (Fréchet Inception Distance)**: Measures alignment between generated and real images.
- **SSIM (Structural Similarity Index Measure)**: Assesses structural fidelity of generated images.
- **Prompt Fidelity**: Over 92%, reflecting the model's ability to align outputs with user-defined text prompts.
- **Batch Processing**: Capable of generating and exporting large numbers of images efficiently.
- **Low Error Rate**: Ensures reliability and consistency across multiple runs.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- Libraries: PyTorch, Flask, Streamlit, diffusers, pyngrok
- A GPU is recommended for efficient performance.

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/synthetic-chest-xray-generation.git
   cd synthetic-chest-xray-generation
   
2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate

4. Install Dependencies:

   ```bash
   pip install -r requirements.txt

5. Launch the Streamlit Interface:

   ```bash
   streamlit run GUI.py

  ## Usage
 - Enter a clinical description in the text box (e.g., "A 60-year-old woman with emphysema").
 - Configure parameters such as:
 - Seed value for reproducibility.
 - Number of inference steps for image quality refinement.
 - Number of images to be generated.
 - Generate and visualize synthetic chest X-rays in real time.
 - Download generated images as a ZIP file for further use.

   ## Future Enhancements
 - Pathology-Specific Improvements: Enhance fine-grained details for challenging conditions like Mass and Effusion.
 - Extended Dataset Support: Incorporate additional datasets for improved generalization.
 - Advanced Evaluation Metrics: Include new metrics to evaluate perceptual and diagnostic relevance more thoroughly.
 - Integration with Cloud Services: Add support for cloud deployment to improve accessibility and scalability.

   ## Contribution
 - Contributions are welcome! Please follow these steps:

 - Fork the repository.

 - Create a new branch:

  ```bash
  git checkout -b feature-name
 - Commit your changes and push them to your forked repository.

 - Open a pull request for review.
