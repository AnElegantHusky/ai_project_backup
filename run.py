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
# ============================ task2: 治疗方案
''' 需要代码：
对每种治疗方案进行ask
take_medicine = kb.ask(expr("Medicine(x)"))

'''
# ============================ output
with open("output.txt", "w") as file:
    output_data = ""
    ''' 需要代码：
    将task1, task2结果写入output_data
    
    '''
    file.write(output_data)



