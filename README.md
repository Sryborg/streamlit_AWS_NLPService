# Streamlit based NLP Application Powered by AWS

This is a simple boiler plate code application which can be used to demostrate an end-to-end working of a AI-enabled website/application.

## Getting started

The following steps will help you set-up the entire end to end 

### Dependencies 
You'll need to have:

- python
- virtualenv

### Installing

You'll need to create a virtual environment using 
```
virtualenv you_env
```

Activate your environment and run
```
pip install -r req.txt
```
Once all the necessary packages are installed, you can go ahead for the execution part.

### Getting Ready
- Start you virtual env

```
source your_env/bin/activate
```
OR
```
conda activate your_env
```
- You will first need to create the model, for that please follow the below steps:
1. Start your jupyter notebook
```
jupyter notebook
```
2. Open the __Basic Bert Trainer.ipynb__ notebook
3. Execute all the steps in the notebook sequentially
4. Although, you'll get the model ready by executing above; I would highly recommend that you try the various model improvement methods before going to production.

### Executing program
```
streamlit run webapp/streamlit_page.py 
```

## Help
For help please write to [me](s.r.yenkar@gmail.com)

## Author
[Sryborg](https://github.com/Sryborg), Machine Learning Engineer

## Acknowledgments
This wouldn't have been possible without the great folks at Google for creating BERT and Analytics Vaidya for creating awesome tutorials.