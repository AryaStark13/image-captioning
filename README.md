# image-captioning

1. Clone the repository:
```
git clone https://github.com/AryaStark13/image-captioning.git
```

2. Install the requirements:
```
pip install -r requirements.txt
```

3. Make a change in the file 'image_captioning_cleaned_env\Lib\site-packages\pycocotools\coco.py' as follows:

In the function 'showAnns' change the final 2 lines from:
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