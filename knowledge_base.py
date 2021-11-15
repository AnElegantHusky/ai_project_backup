import sys
sys.path.append(".\\aima")

from aima.utils import expr
from aima.logic import FolKB, fol_fc_ask

# ============================ 编写clauses
clauses = []
''' 需要代码：
知识 -> expr("...")
clauses.append(expr(".............."))

'''
# ============================ 构造KB
kb = FolKB(clauses)

