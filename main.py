import glob
import pandas as pd


def parse_xmls_with_pandas(files):
    dataframes = []

    for file in files:
        dataframes.append(pd.read_xml(file, xpath='//Transaction'))

    df = pd.concat(dataframes)

    print(df.shape)

    df2 = df.drop_duplicates()

    print(df2.shape)

    df2.Amount = df2.Amount.astype('Int64')
    df2.Balance = df2.Balance.astype('Int64')
    df2.PurposeCode = df2.PurposeCode.astype('Int64')

    df2.to_csv('data\\STB_statements.csv', encoding='utf-8')


def get_files():
    files = []
    for path in glob.glob('data\\*.xml', recursive=True):
        files.append(path)
    return files


if __name__ == '__main__':
    files = get_files()
    parse_xmls_with_pandas(files)
