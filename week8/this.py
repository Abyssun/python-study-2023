from bubblepy import BubbleBabble
s = 'SQNU{4f017f99-f869-49cb-93d2-1bd832f8e8b0}'
bb = BubbleBabble()
s1 = bb.encode(s)
print(s1)
print(bb.decode(s1))