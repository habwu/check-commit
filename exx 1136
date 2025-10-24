N_str = input()
N = int(N_str)
odd_session_order = []
for _ in range(N):
    num_str = input()
    odd_session_order.append(int(num_str))
result = []
traversal_stack = []
if N > 0:
    traversal_stack.append([0, N - 1, 0])
while len(traversal_stack) > 0:
    current_task = traversal_stack.pop()
    start_idx = current_task[0]
    end_idx = current_task[1]
    state = current_task[2]
    if start_idx > end_idx:
        continue
    root_val = odd_session_order[end_idx]

    if state == 0:
        traversal_stack.append([start_idx, end_idx, 1])
        right_subtree_start_in_current_segment = start_idx
        while right_subtree_start_in_current_segment < end_idx and \
              odd_session_order[right_subtree_start_in_current_segment] < root_val:
            right_subtree_start_in_current_segment += 1
        if start_idx <= right_subtree_start_in_current_segment - 1:
            traversal_stack.append([start_idx, right_subtree_start_in_current_segment - 1, 0])
        if right_subtree_start_in_current_segment <= end_idx - 1:
            traversal_stack.append([right_subtree_start_in_current_segment, end_idx - 1, 0])
    elif state == 1:
        result.append(root_val)
for val in result:
    print(val)
