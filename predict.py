import os
import pandas as pd
import argparse
from pycaret.classification import *


def process_csv(input_file, output_file):
    # 指定要读取的列
    data_input = ['Weight', 'AOP', 'RDS', 'ROP', 'WBC', 'ALB', 'MV']

    # 读取输入csv文件
    df = pd.read_csv(input_file)

    # 提取指定列的数据
    df_selected = df[data_input]
    
    catboost_model = load_model('models/catboost_tuned')
    predictions = predict_model(catboost_model, data=df_selected, raw_score=True)
    probability = predictions['prediction_score_1']
    predictions = predictions.drop(['prediction_score_0','prediction_score_1'],axis=1)
    predictions['probability'] = probability
    # 如果没有指定输出路径，则默认在当前目录中创建一个名为 "result.csv" 的文件
    if output_file is None:
        output_file = os.path.join(os.getcwd(), 'result.csv')
    predictions.to_csv(output_file, index=False)
    print(f"Predictions saved to {output_file}")
    
    # 保存结果到输出csv文件
    # df_selected.to_csv(output_file, index=False)

if __name__ == '__main__':
    # 创建参数解析器
    parser = argparse.ArgumentParser(description='Process input and output csv files.')
    parser.add_argument('--input', type=str, help='Input csv file path')
    parser.add_argument('--output', type=str, help='Output csv file path')
    args = parser.parse_args()

    process_csv(args.input, args.output)