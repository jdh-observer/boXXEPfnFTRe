import re

numerical_columns = ["pool", "player", "rankint"]

def apply_normalizations(s):
	s = s.strip()
	s = s.replace(" : ", "：")
	s = s.replace(" : ", "：")
	return s

def read_csv(path,keys):
	separator = ","
	rst = []
	with open(path, encoding="utf8") as infile:
		lines = infile.readlines()
		
		if len(lines) < 2:
			raise Exception(f"When reading csv file {path}: expected at least 2 lines")
		
		assert(len(keys) == len(set(keys)))
		
		for l in lines[1:]:
			fields = apply_normalizations(l).split(separator)
			assert(len(fields) >= len(keys))
			cur_vals = dict()
			for j in range(len(keys)):
				if keys[j] in numerical_columns:
					if fields[j] != "":
						cur_vals[keys[j]] = int(fields[j])
					else:
						cur_vals[keys[j]] = 0
				else:
					cur_vals[keys[j]] = fields[j].strip()
					
			rst.append(cur_vals)
	return rst
