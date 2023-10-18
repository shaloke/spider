# from fuzzywuzzy import fuzz

# str1 = "王凯俊"
# str2 = "黄俊康"

# # 使用 fuzz.ratio() 函数计算字符串相似度（以百分比表示）
# similarity_ratio = fuzz.ratio(str1, str2)

# print(similarity_ratio)  # 输出：84


# from nltk.tokenize import word_tokenize  
# from collections import Counter  
  
# def jaccard_similarity(s1, s2):  
#     s1_tokens = word_tokenize(s1)  
#     s2_tokens = word_tokenize(s2)  
#     intersection = Counter(s1_tokens) & Counter(s2_tokens)  
#     union = len(s1_tokens) + len(s2_tokens) - intersection.total()  
#     return float(intersection.total()) / union  
  
# print(jaccard_similarity('我喜欢编程', '我喜欢读书'))

from difflib import SequenceMatcher

def similarity(str1, str2):
    # 使用SequenceMatcher类计算字符串之间的相似度
    seq_matcher = SequenceMatcher(None, str1, str2)
    
    # 获取相似度百分比
    ratio = seq_matcher.ratio()
    
    # 返回相似度百分比
    return ratio * 100

# 测试代码
str1 = '秦皇岛市北戴河区第六建筑安装工程有限公司'
str2 = '北戴河区第六建筑安装工程有限公司'
print(similarity(str1, str2))