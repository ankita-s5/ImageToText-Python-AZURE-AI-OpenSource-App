from dotenv import load_dotenv
import os

from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import visualfeatures
from azure.core.credentials import AzureKeyCredential


def main():
    load_dotenv()  # Load environment variables from .env file
    endpoint = os.getenv("AZURE_VISION_ENDPOINT")
    key = os.getenv("AZURE_VISION_KEY") 

    if not  endpoint or not key:    
        print("Error: Azure Vision endpoint or key is missing.")
        return  

    cv_client= ImageVisionClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    image_file_path = "../images/1.png"

    with open(image_file_path, "rb") as image_file:
        analysis = cv_client.analyze_image(
            image=image_file,
            features=[visualfeatures.read]
        )

    if result is not None:
        print("Detected text:")
        for line in analysis.read.lines:
            print(line.content)
    else:
        print("No text detected.")
            
if __name__ == "__main__":
    main()