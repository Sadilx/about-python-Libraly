import pandas as pd
import numpy as np

s1=pd.Series([1,2,3,5]) #Seriesは一列データ型
print(s1)

df=pd.DataFrame({
    "名前":["吉田","前田","高橋"],
    "役割":["村長","農民","郷士"],
    "身長":[199,162,187]
    })
#DataFrameは２次元のラベル付きのデータ構造→Excelのセルみたいに作れる
print(df)
print(df.dtypes) #objectかintかとか出してくれる

print(df.columns) #列ラベルの確認

data = {
    "名前":['田中','山田','高橋'],
    "役割":['営業部長','広報部','技術責任者'],
    "身長":[178, 173, 169]
    }
df = pd.DataFrame(data, columns=["名前", "役割", "身長"])
# データフレーム生成時に対応するデータを持っていない場合、そのデータの列にはNaNが割り当てられます。
#カラムの名称を変更・置換可能
df.columns = ["Name","Position","height"]
print(df)

df = pd.DataFrame(np.random.randn(20,2))
df.head() # 先頭から5件
df.tail()   # 末尾から5件

df.head().append(df.tail()) # 先頭から5件と末尾から5件の計10件を取得
df.head(3).append(df.tail(3)) # 先頭から3件と末尾から3件の計6件を取得