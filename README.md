# lalala

![icons8-music-note-48](https://github.com/DomiDhillon/mp3Downloader/assets/65451658/d94a3985-bc63-4c2c-bb9d-dfc05dcd5498)

## 1. (optional) Create conda env with packages you'll need
```
conda env create -f youtubenv.yml
```
## 2. Activate the new env
```
conda activate youtubenv
```

## 3. Download mp3 (replace _url_ by a link)
```
python mp3Downloader.py url --filename new_optional_name --directory optional/output/directory/
```
- if you don't precise the output directory, then it will be downloaded in working dir.
- if you don't precise name, it will be the same as online minus weird characters and minus space.
