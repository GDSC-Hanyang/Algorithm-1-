def solution(sizes):
	w, h= 0, 0
	for size in sizes:
		if size[0] < size[1]:
			size[0], size[1] = size[1], size[0]
		if w < size[0]: w = size[0]
		if h < size[1]: h = size[1]
	return w*h