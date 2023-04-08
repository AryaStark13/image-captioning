# image-captioning

1. Create a virtual environment and activate it.
```
python -m venv image_captioning_cleaned_env
image_captioning_cleaned_env\Scripts\activate
```

Check if the virtual environment is activated by seeing if the name of the environment is displayed in the terminal.

2. Clone the repository:
```
git clone https://github.com/AryaStark13/image-captioning.git
```

3. Install the requirements:
```
pip install -r requirements.txt
```

4. Make a change in the **pycocotools** module file *image_captioning_cleaned_env\Lib\site-packages\pycocotools\coco.py* as follows:

In the function *showAnns* change the *final 2 lines* from: (should be line 302 and 303 or around there)
```
for ann in anns:
        print(ann['caption'])
```
to:
```
return_anns = []
for ann in anns:
    return_anns.append(ann['caption'])
return return_anns
```