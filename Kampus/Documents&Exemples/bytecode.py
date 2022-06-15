import dis

def fonction(nums, pos, new_value):
    if pos < len(nums):
        nums[pos] = new_value
        return new_value

print(dis.dis(fonction))
