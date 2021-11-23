import sys
sys.path.append(".\\aima")

from aima.utils import expr
from aima.logic import FolKB, fol_fc_ask
from knowledge_base import kb
from func_timeout import func_timeout, FunctionTimedOut

# ============================ 输入病人症状、检测结果
with open("input.txt", 'r') as file:
    file_data = file.read()
    lines = file_data.split('\n')
    for line in lines:
        kb.tell(line)

# ============================ task1: 诊断、分期
''' 需要代码：
对每种可能分期进行ask
hcc = kb.ask(expr("HCC(x)"))   //返回True or False

不知道kb有没有实现对死循环的处理
'''
diagnosis_keys = ["diagnosis_HCC", "diagnosis_cnlc_1a", "diagnosis_cnlc_1b", "diagnosis_cnlc_2a",
                  "diagnosis_cnlc_2b", "diagnosis_cnlc_3a", "diagnosis_cnlc_3b", "diagnosis_cnlc_4a"]
diagnosis_results = {}
diagnosis_results["diagnosis_HCC"] = kb.ask(expr("diagnosis_HCC(x)"))
if diagnosis_results["diagnosis_HCC"] is True:
    for key in diagnosis_keys[1:]:
        diagnosis_results[key] = kb.ask(expr(key+"(x)"))

# diagnosis_HCC = kb.ask(expr("diagnosis_HCC(x)"))
# diagnosis_according_to_new_size
#
# diagnosis_2_3_month_img_follow_up
# diagnosis_AFP
# diagnosis_US
# diagnosis_6_month
# diagnosis_cnlc_1a = False
# diagnosis_cnlc_1b = False
# diagnosis_cnlc_2a = False
# diagnosis_cnlc_2b = False
# diagnosis_cnlc_3a = False
# diagnosis_cnlc_3b = False
# diagnosis_cnlc_4a = False

# if diagnosis_HCC is True:
#     diagnosis_cnlc_1a = kb.ask(expr("diagnosis_cnlc_1a(x)"))
#     diagnosis_cnlc_1b = kb.ask(expr("diagnosis_cnlc_1b(x)"))
#     diagnosis_cnlc_2a = kb.ask(expr("diagnosis_cnlc_2a(x)"))
#     diagnosis_cnlc_2b = kb.ask(expr("diagnosis_cnlc_2b(x)"))
#     diagnosis_cnlc_3a = kb.ask(expr("diagnosis_cnlc_3a(x)"))
#     diagnosis_cnlc_3b = kb.ask(expr("diagnosis_cnlc_3b(x)"))
#     diagnosis_cnlc_4a = kb.ask(expr("diagnosis_cnlc_4a(x)"))

# diagnosis_results = [diagnosis_HCC, diagnosis_cnlc_1a, diagnosis_cnlc_1b, diagnosis_cnlc_2a, diagnosis_cnlc_2b, diagnosis_cnlc_3a]


# ============================ task2: 治疗方案
''' 需要代码：
对每种治疗方案进行ask
take_medicine = kb.ask(expr("Medicine(x)"))

'''
# ============================ output
with open("output.txt", "w") as file:
    output_data = ""
    # if diagnosis_HCC is True:
    for key in diagnosis_keys:
        output_data += "{}: {}".format(key, diagnosis_results[key])

    ''' 需要代码：
    将task1, task2结果写入output_data
    
    '''
    file.write(output_data)



