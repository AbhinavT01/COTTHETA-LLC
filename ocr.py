#!/usr/bin/env python
# coding: utf-8

# In[326]:


import pandas as pd
import numpy as np
import re
import cv2 

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

import easyocr

plt.style.use('ggplot')


# # easyocr

# * final

# In[327]:


reader = easyocr.Reader(['en','hi'], gpu = True)


# In[350]:


def preprocess(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # contrast the image 
    image = cv2.convertScaleAbs(image, -1, alpha=0.9,beta=1.5) 

    # Check the image dimensions
    (h, w) = image.shape[:2]

    # If the image is in landscape orientation
    if w > h:
        # Convert the image to grayscale
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Rotate the image to portrait orientation
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, 90, 1.0)
        image = cv2.warpAffine(image, M, (h, w), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    else:
        # Image is already in portrait orientation, grayscale of original image
        image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    return image


# Automatically rotate the image to portrait orientation if in landscape
gray_image = preprocess('sample data/pan1_sample.png')

# # Display the grayscale image
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()


# In[356]:


results = reader.readtext(gray_image)
df=pd.DataFrame(results, columns=['bbox','text','conf'])
df['text']=df['text'].apply(lambda x : re.sub(".*(नाम|तारीख ).","",x))
pattern = re.compile(r'^(DL|ID|DLID|CDL|CDLID)\s*'
                     r'([A-Z0-9]{1,2})\s*'  # First name initial(s)
                     r'([A-Z]{2})\s*'  # Middle initial(s)
                     r'([A-Z0-9]{1,5})\s*'  # Last name
                     r'([A-Z]{1,2})\s*'  # Suffix (e.g., JR, SR, III)
                     r'([A-Z0-9]{1,5})\s*'  # Date of birth (MMDDYYYY)
                     r'([A-Z]{1,2})\s*'  # Expiration date month
                     r'([A-Z0-9]{1,5})\s*'  # Expiration date year
                     r'([A-Z0-9]{1,5})\s*'  # License number
                     r'([A-Z]{1,2})\s*'  # Issue date month
                     r'([A-Z0-9]{1,5})\s*'  # Issue date year
                     r'([A-Z]{1,2})\s*'  # Address
                     r'([A-Z0-9]{1,5})\s*'  # City
                     r'([A-Z]{2})\s*'  # State
                     r'([A-Z0-9]{1,5})\s*'  # Zip code
                     r'([A-Z]{1,2})\s*'  # Height
                     r'([A-Z0-9]{1,5})\s*'  # Weight
                     r'([A-Z]{1,2})\s*'  # Eye color
                     r'([A-Z]{1,2})\s*'  # Hair color
                     r'([A-Z]{1,2})\s*'  # Sex
                     r'([A-Z0-9]{1,5})\s*'  # Restrictions)
        )
df['type']=df['text'].apply(lambda x:pattern.match(x))
df['text']=df['text'].apply(lambda x :np.nan if bool(re.findall(r'(Digitally|sign|Physically|Valid|unless).*',x,flags=re.IGNORECASE)) else x) #removing sign cell
df['text']=df['text'].apply(lambda x: np.nan if str(x).isnumeric() else x) #removing issue date since causing error
df=df.dropna()
df.drop(columns=['type'],inplace=True)
# removing sign photo if detected logic
index_to_drop = df['conf'].idxmin()
df.drop(index_to_drop, inplace=True)
df=df.reset_index(drop=True)


# In[357]:


df # this df will be use to create the bounding boxes


# In[358]:


def plot_bounding_boxes(df, image_path):
    # Read the image
    # image = cv2.imread(image_path)
    
    # Plot the image
    fig, ax = plt.subplots()
    ax.imshow(cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB))

    # Add bounding boxes, text, and confidence scores
    for index, row in df.iterrows():
        # Get bounding box coordinates
        bbox = row['bbox']
        x1, y1 = bbox[0]
        x2, y2 = bbox[2]

        # Add bounding box
        rect = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
    # Show plot
    plt.axis('off')
    plt.show()

plot_bounding_boxes(df,gray_image)


# ---

# 

# In[359]:


def ocr_text(df):
    try:
        new_rows=[]
        for i,r in df.iterrows():
            new_rows.append(r.to_dict())
        # Create a new DataFrame with the added rows
        df_new = pd.DataFrame(new_rows)
        
        keys=list(df_new['text'].iloc[::2])
        values=list(df_new['text'].iloc[1::2])

        df_new=pd.DataFrame({"key":keys,
                    "value":values})
        
        return df_new
    except:
        print("Erorr")


# In[360]:


ocr_text(df) # df_new will be used to check the facts


# In[361]:


import os

folder_path = "uploads"

# Get the current working directory
current_directory = os.getcwd()

# List all files and directories in the uploads folder
contents = os.listdir(folder_path)

# Iterate through each item in the folder
for item in contents:
    item_path = os.path.join(folder_path, item)
    # Check if the item is a file
    if os.path.isfile(item_path):
        # Extract the filename and full path
        file_name = os.path.basename(item_path)
        # Get the relative path
        relative_path = os.path.relpath(item_path, current_directory)
        # print("Image Name:", file_name)
        print(relative_path)


# In[362]:


index_to_drop = df['conf'].idxmin()
df.drop(index_to_drop, inplace=True)


# In[363]:


df

