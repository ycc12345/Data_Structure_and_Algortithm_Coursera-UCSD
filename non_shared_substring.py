# python3
import sys

class Node:
	def __init__(self):
		self.label = dict()
		self.parent = -1
		self.position = -1

def find_branch_position(text, suffix_text):
	cursor = 0
	length = len(text)
	while text[cursor] == suffix_text[cursor]:
		cursor += 1
		if cursor == length:
			break
	return cursor

def build_suffix_tree(text):
	root = Node()
	suffix_tree = [root]
	for i in range(len(text)):
		CurrentNode = 0
		index = i
		while True:
			find = False
			for s, l in suffix_tree[CurrentNode].label:
				if text[s].startswith(text[index]):
					start = s
					length = l
					find = True
					break
			if find:
				branchPosition = find_branch_position(text[start:start+length],text[index:])	
				if branchPosition == length:
					CurrentNode = suffix_tree[CurrentNode].label[(start,length)]
					index += length
				else:
					#break a branch
					index += branchPosition
					NewNode = Node()
					NewNode.parent = CurrentNode
					m = suffix_tree[CurrentNode].label.pop((start,length))
					suffix_tree[CurrentNode].label[(start,branchPosition)] = len(suffix_tree)
					NewNode.label[(start+branchPosition, length-branchPosition)] = m
					suffix_tree[m].parent = len(suffix_tree)
					suffix_tree.append(NewNode)
					CurrentNode = len(suffix_tree) - 1
			else:
				#create a branch
				NewNode = Node()
				NewNode.position = i
				NewNode.parent = CurrentNode
				suffix_tree[CurrentNode].label[(index, len(text)-index)] = len(suffix_tree)
				suffix_tree.append(NewNode)
				break
	return suffix_tree

def path_to(node, suffix_tree):
	end, _ = list(suffix_tree[node].label.keys())[0]
	begin = end
	while suffix_tree[node].parent != -1:
		for (start, length), m in suffix_tree[suffix_tree[node].parent].label.items():
				if m == node:
					begin = begin - length
		node = suffix_tree[node].parent
	return (begin, end)

def dfs(node, l, suffix_tree, result):
	if suffix_tree[node].position != -1:
		if suffix_tree[node].position > l:
			return 0
		elif suffix_tree[node].position < l:
			for (start, length), m in suffix_tree[suffix_tree[node].parent].label.items():
				if m == node and start < l:
					result.append((suffix_tree[node].position, start+1))
			return 1
		else:
			return 1				
	child = []
	for (start,length), m in suffix_tree[node].label.items():
		child.append(dfs(m, l, suffix_tree,result))
	if 0 in child:
		return 0
	else:
		result.append(path_to(node, suffix_tree))
		return 1

def solve (p, q):
	result = []
	l = len(q)
	suffix_tree = build_suffix_tree(p+'#'+q+'$')
	dfs(0, l,suffix_tree, result)
	result = [(end-start, start) for start, end in result]
	length, start = min(result)
	return p[start:start+length]

sys.setrecursionlimit(4000)
p = sys.stdin.readline ().strip ()
q = sys.stdin.readline ().strip ()

ans = solve (p, q)

sys.stdout.write (ans + '\n')
