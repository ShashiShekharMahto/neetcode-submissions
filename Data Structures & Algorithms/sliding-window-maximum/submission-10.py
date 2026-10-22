class Solution:
    def second_max_index(self, nums, i, k):
        max_val = float('-inf')
        second_max = float('-inf')
        max_idx = second_idx = -1

        for j in range(i, k):
            if nums[j] > max_val:
                second_max = max_val
                second_idx = max_idx
                max_val = nums[j]
                max_idx = j

            elif nums[j] > second_max:
                second_max = nums[j]
                second_idx = j

            elif nums[j] == second_max:
                second_idx = j

        return second_idx

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_el = []
        
        first_window = nums[0:k]
        curr_max = max(first_window)
        max_val_idx = first_window.index(curr_max)

        sec_max_idx = self.second_max_index(nums, 0, k)
        sec_max_val = nums[sec_max_idx]

        max_el.append(curr_max)
        print(max_el, max_val_idx)

        for i in range(1, len(nums)-k+1):
            # max_el.append(max(nums[i:i+k]))
            # print(i, nums[i:i+k])
            curr_window_last_element = nums[i+k-1]
            curr_window_last_idx = i + k -1
            if max_val_idx >= i:
                # print("max", nums[i : i+k])
                if sec_max_idx < i or \
                (curr_window_last_element > sec_max_val and \
                curr_window_last_element < curr_max):

                    sec_max_idx = self.second_max_index(nums, i, i+k)
                    sec_max_val = nums[sec_max_idx]

                if curr_max > curr_window_last_element:
                    max_el.append(curr_max)
                    

                elif curr_max == curr_window_last_element:
                    max_el.append(curr_window_last_element)
                    max_val_idx = curr_window_last_idx
                    
                elif curr_window_last_element > curr_max:
                    max_el.append(curr_window_last_element)
                    max_val_idx = curr_window_last_idx
                    curr_max = curr_window_last_element
                

                else:
                    curr_window = nums[i: i+k]
                    curr_max = max(curr_window)
                    max_val_idx = i + curr_window.index(curr_max)

                    max_el.append(curr_max)
                # print(curr_max, sec_max_val, max_el)
                # print()
            
            elif sec_max_idx >= i:
                print("second",nums[i: i+k], i, i+k)
                print(curr_max, sec_max_val, max_val_idx, sec_max_idx)

                if sec_max_val > curr_window_last_element:
                    max_el.append(sec_max_val)

                elif sec_max_val == curr_window_last_element:
                    max_el.append(curr_window_last_element)
                    max_val_idx = i
                    
                elif curr_window_last_element > sec_max_val:
                    max_el.append(curr_window_last_element)
                    max_val_idx = i
                    curr_max = curr_window_last_element
                else:
                    curr_window = nums[i: i+k]
                    curr_max = max(curr_window)
                    max_val_idx = i + curr_window.index(curr_max)

                    max_el.append(curr_max)
                
                curr_window = nums[i: i+k]
                curr_max = max(curr_window)
                max_val_idx = i + curr_window.index(curr_max)

                sec_max_idx = self.second_max_index(nums, i, i+k)
                sec_max_val = nums[sec_max_idx]

                # print(max_el)
                # print()
                
            else:
                curr_window = nums[i: i+k]
                curr_max = max(curr_window)
                max_val_idx = i + curr_window.index(curr_max)

                sec_max_idx = self.second_max_index(nums, i, i + k)
                sec_max_val = nums[sec_max_idx]

                max_el.append(curr_max)
                # print("last", max_el, )

        return max_el