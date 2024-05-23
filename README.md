**English** | [中文](https://pbipred.liaolab.net/PBIPred_for_Chinese_users)
# PBIPred tool
The local version of PBIPred (A machine learning based preterm brain injury predictor) for multiple samples.
# 1. Environment
```
git clone https://github.com/2019012971/PBIPred.git
cd PBIPred
conda env create -f environment.yml -n PBIPred
conda activate PBIPred
```
# 2. Data preprocessing
Please prepare a csv file to be used as input, an example is called "input_template.csv".
# 3. Predict your own file
```
python predict.py --input input_template.csv --output results.csv
```
```
usage: predict.py [-h] [--input INPUT] [--output OUTPUT]

Process input and output csv files.

optional arguments:
  -h, --help       show this help message and exit
  --input INPUT    Input csv file path
  --output OUTPUT  Output csv file path
```
# 4. Webserver
The webserver version of PBIPred is provided at [http://pbipred.liaolab.net](http://pbipred.liaolab.net).
