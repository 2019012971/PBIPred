**English** | [中文](https://pbipred.liaolab.net/PBIPred_for_Chinese_users)
# PBIPred tool
The local version of PBIPred (A machine learning based preterm brain injury predictor) for multiple samples.
# 1. Environment
```
# Please run these commands in terminal and install anaconda/miniconda first
git clone https://github.com/2019012971/PBIPred.git
cd PBIPred
conda create -n PBIPred python=3.9
conda activate PBIPred
pip install pycaret pycaret[full]
```
# 2. Data preprocessing
Kindly prepare a comma-separated values (CSV) file to be utilised as input. An illustrative example is provided in the file designated "input_template.csv".
# 3. Predict your own file
```
# The result is on the 'results.csv'
python predict.py --input input_template.csv --output results.csv
```
# 4. Detailed usage
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
