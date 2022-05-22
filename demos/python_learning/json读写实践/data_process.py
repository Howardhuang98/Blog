import json
import pathlib
import pandas as pd


def readFile(file):
    sign = []
    score = []
    Xmin = []
    Ymin = []
    w = []
    h = []
    with open(file, encoding='utf-8') as lines:
        for line in lines:
            # 读取文件,空格进行分割,获取第一列的值
            sign.append(line.split(" ")[0])
            score.append(line.split(" ")[1])
            Xmin.append(line.split(" ")[2])
            Ymin.append(line.split(" ")[3])
            w.append(line.split(" ")[4])
            # 读取文件,空格进行分割,并去掉最后的'\n'
            h.append(line.split(" ")[5].strip())

    return sign, score, Xmin, Ymin, w, h


if __name__ == '__main__':
    # 你的结果文件夹
    path = pathlib.Path("results")
    # label文件
    label = pd.read_csv("label_list.csv", index_col=0)
    # 图像id文件
    img_id = pd.read_csv("TestSet (1).csv", index_col=0)
    # 存储的结果
    jsonFile = 'json_result.json'

    datanames = path.iterdir()
    result = []
    for i in datanames:
        if i.suffix == '.txt':
            ml_1, ml_2, ml_3, ml_4, ml_5, ml_6 = readFile(path / i.name)
            for j in range(len(ml_1)):
                # 将结果保存到dic中
                # dic = {'epoch':i,'cm': [ml_1[i], ml_2[i], ml_3[i], ml_4[i]]}
                # 这里将str转为int(个人需求)
                image_id = img_id.index[img_id["img_name"].str.contains(i.stem)].tolist()
                if not image_id:
                    print(f"{i.name}没有找到id, 自动填入0")
                    image_id = 0
                else:
                    image_id = image_id[0]

                dic = {"image_id:": image_id,
                       'category_id': label[label.Label == ml_1[j]].index.tolist()[0],
                       'bbox': [float(ml_3[j]),
                                float(ml_4[j]),
                                float(ml_5[j]) + float(ml_3[j]),
                                float(ml_6[j]) + float(ml_4[j])],
                       'score': float(ml_2[j])}
                result.append(dic)

    # w模式写入，会覆盖原文件。如果要追加写入改为a模式
    with open(jsonFile, 'w') as name:
        jsonData = json.dumps(result, indent=1)
        name.write(jsonData)
