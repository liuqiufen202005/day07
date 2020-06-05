import yaml

# 写入数据
data = {'Search_Data': {
    'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
    'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}

# 将data写入到当前目录下 ww.yml文件中
with open("./ww.yaml", "a") as f:  # 以a模式:追加写入文件
    # 写入yaml数据
    yaml.safe_dump(data, f, encoding="utf-8", allow_unicode=True)
