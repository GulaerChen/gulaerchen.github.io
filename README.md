# MIR-SingerSeparation Dataset & Auto-selection

### Dataset Description
The dataset consists of 3 types (Please refer to paper to introduce various categories.) of singer separation datasets, each track 10 seconds long, segments from 476 English and 500 Chinese songs, and male/female vocalist ratio for English songs was 269:207, while that for Chinese songs was 223:277. The tracks are all 8kHz Mono 16-bit audio files in .wav format.

### Versions
1.0.0 (default): No release notes.

### System Demo
<a href="https://gulaerchen.github.io/MIR-SingerSeparation/" target="_blank"> Singer Separation </a>

### Download datasets
* <a href="https://drive.google.com/file/d/1SgMEGxPmgtTBTwWukDE53hR9W5ajOUvW/view?usp=sharing" target="_blank"> EN-D </a>
* <a href="https://drive.google.com/file/d/1k6S9i64Z1USqy1xwPlZDXN8DNTwpLY6c/view?usp=sharing" target="_blank"> CH-D </a>
* <a href="https://drive.google.com/file/d/1FveU1Jp02GopUpff33EgYFZtVOfMeHa4/view?usp=sharing"> EN-S </a>

### Download size
* EN-D: 17.0 GB
* CH-D: 8.25 GB
* EN-S: 11.6 GB

### Dataset size
* EN-D: 22 GB
* CH-D: 12 GB
* EN-S: 15 GB

### Splits
![](https://i.imgur.com/bXUBHa5.png)

### Auto Selection
* <a href="https://drive.google.com/file/d/1wLDoLHdBb36_11tSWEPI2di86mTAQtjn/view?usp=sharing" target="_blank"> Pitch Data </a>
```shell
python auto_selection.py 
```

### Citation
Please cite the paper to use the dataset.
```bibtex
@misc{chen2021singer,
    title={Singer separation for karaoke content generation},
    author={Hsuan-Yu Chen and Xuanjun Chen and Jyh-Shing Roger Jang},
    year={2021},
    eprint={2110.06707},
    archivePrefix={arXiv},
    primaryClass={cs.SD}
}
```
