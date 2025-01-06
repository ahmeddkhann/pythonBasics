
# Indexing in python 
# there can be three different types of indexing
#one is "Start", next is "End" and last one is "Step"
#below is the example


cnic_number = "16928722-837239-82"
print(cnic_number) #print whole CNIC number // 16928722-837239-82
print(cnic_number[6]) #print number at index 6 // 2
print(cnic_number[1:5]) #wil print from index 1 to index 5 // 6928
print(cnic_number[5:]) #will print from index5 to end // 722-837239-82
print(cnic_number[:3]) #will print from start to index 3 exluxsively index 3 // 169
print(cnic_number[::2]) #will print one and leave one .(in this case) // 1982-3298
print(cnic_number[::3]) #will print one and leave two in this case // 12282-
print(cnic_number[-1]) #negative indexing prints from end // 2