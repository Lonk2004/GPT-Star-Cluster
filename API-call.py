from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


with open("OpenAI-venv/data.json", "r") as data:
    input_data = json.load(data)
    #set my private openai key as environment variable to use here
    batch_size = 2
    for i in range(0, len(input_data), batch_size): 
        #get data for batch to send to api
        batch = input_data[i:i+batch_size]
        response = client.chat.completions.create(model="gpt-4o",
        messages =[
            {"role": "system", "content": "You are a classifier for astronomical images from the PandAS astronomical survey. Do not use metadata or any external information to classify the images."},
            {"role": "user", "content": f"You will be shown batches of image data of either Globular Clusters (GCs) or Galaxies. A batch can contain either one of either, or two of the same. Return an array with an entry for each image in the batch. Return 1 for GC and 0 For galaxy. do not give any further information: {json.dumps(batch)}"}
        ])
        print(response.choices[0].message.content)
