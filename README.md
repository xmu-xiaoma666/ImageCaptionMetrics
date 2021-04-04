# Eval Tools for Imgae Captioning & NLP

## 1.Introduction

This repository contains 2 tools:

- A py3 Lib for NLP & image-caption metrics : [BLEU](https://www.aclweb.org/anthology/P02-1040.pdf), [METEOR](https://www.aclweb.org/anthology/W05-0909.pdf), [CIDEr](https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Vedantam_CIDEr_Consensus-Based_Image_2015_CVPR_paper.pdf), [ROUGE](https://www.aclweb.org/anthology/W04-1013.pdf),[SPICE](https://arxiv.org/pdf/1607.08822.pdf), [WMD](https://mkusner.github.io/publications/WMD.pdf).
- Code for a two-tailed t-test with paired samples. It will reveals whether the difference of two results is significant. In   this code, we complete evaluation code for Spice details(*i.e.*,Object, Relation, Attribute, Color, Count, and Size ).

## 2.Requirements

- java 1.8+
- python 3
  
- gensim
  
- Stanford CoreNLP 3.6.0([download](http://nlp.stanford.edu/software/stanford-corenlp-full-2015-12-09.zip), [baiduyun](https://pan.baidu.com/s/1t_JcBjEfa5OTasA22ocE_w )(code:gsis))

  - add stanford-corenlp-3.6.0.jar to

    `pycocoevalcap/spice/lib/`

  - add stanford-corenlp-3.6.0-models.jar to

    `pycocoevalcap/spice/lib/`

- `google_word2vec_model` for WMD[(download)](https://docs.google.com/uc?export=download&id=0B7XkCwpI5KDYNlNUTTlSS21pQmM)
  - unzip it and add GoogleNews-vectors-negative300.bin to `pycocoevalcap/wmd/data`

## 3.Usage

## 3.1 Data preparation

Note that the input format must be the same as the file in `examples/gts.json` and `examples/res.json`

- gts.json format:

`{%d:[%s,%s,%s,%s,%s],...}`%（id,sentence1,sentence2,sentence3,sentence4,sentence5）

- gts.json format:

`{%d:[%s],...}`%（id,sentence）



### 3.2 Eval metric

- **Eval with saving spice**(spice details will be save to "save_path")

  ```
  python demo.py --gts_path examples/gts.json --res_path examples/res.json --save_spice --save_path output/test_spice.json
  ```

- **Eval without saving spice**

  ```
  python demo.py --gts_path examples/gts.json --res_path examples/res.json 
  ```

![](.\examples\metric_result.png)

Important args:

- `--gts_path`: path to ground truths
- `--res_path`: path to generated captions
- `--save_spice`: whether to save json file of spice details
- `--save_path`: path to save json file of spice details



### 3.3  two-tailed t-test with paired sample

```
python statistic.py
```

![](./examples/p_value.png)



## 4. Acknowledgements

- WMD metric from https://github.com/mtanti/coco-caption
- Main code from https://github.com/EricWWWW/image-caption-metrics
