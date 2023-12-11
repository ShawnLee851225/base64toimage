import pandas as pd
import base64
from PIL import Image

data_path = "./data/data1.xlsx"
image_path = "./image"

df = pd.read_excel(data_path)

# all data
# print(df)

# print one data
# data = df["Unnamed: 0"][5]
# data = data.replace('\\', '').replace('\"signimg\" : \"', '')
# while len(data) % 4 != 0:
#     data += '='
# print(data)
# img = base64.b64decode(data)
# # Save the image to a file
# output_file_path = f"{image_path}/output_image.jpg"
# with open(output_file_path, 'wb') as output_file:
#     output_file.write(img)
# print(f"Image saved to: {output_file_path}")

index = df.shape[0]
print(index)

for i in range(index):
    temp = df["Unnamed: 0"][int(i)]
    
    if(pd.isna(temp)):
        print("is NaN")
    else:
        if(temp.find("snmae") != -1):
            print("name")
        else:
            try:
                temp =  temp.replace('\"signimg\" : \"', '')
                temp = temp.strip()
                temp = temp.replace('\\', '')
                
                while len(temp) % 4 != 0:
                    temp += '='
                
                img = base64.b64decode(temp)
                # Save the image to a file
                output_file_path = f"{image_path}/{i}.png"
                with open(output_file_path, 'wb') as output_file:
                    output_file.write(img)
                print(f"Image saved to: {output_file_path}")
                print("finish")
            except Exception as e:
                print(f"Error processing index {i}: {e}")
                continue  # Skip to the next iteration if an error occurs

