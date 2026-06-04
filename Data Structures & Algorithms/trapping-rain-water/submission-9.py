class Solution:

    def count_empty_box(self, height, r,
        max_bar_h, max_bar_idx):

        l = r-1
        curr_height = height[r]
        min_height = min(curr_height, max_bar_h)

        empty_box = 0
        while l > max_bar_idx:

            # trying to fill water by counting empty box
            empty_diff = min_height - height[l]
            if empty_diff > 0:
                empty_box += empty_diff
                # making the index bar as filled with min_height
                height[l] = min_height
            l -= 1
        return empty_box


    def trap(self, height: List[int]) -> int:

        empty_box_count = 0
        
        max_bar_h = height[0]
        max_bar_idx = 0
        height_diff = 0
        
        h_len = len(height)
        if h_len < 3:
            return empty_box_count
        l = 0
        r = 1
        l_bar = height[l]
        r_bar = height[r]
        while r < h_len:

            if l_bar == r_bar:
                if r - l == 1:
                    l += 1
                    r += 1
                    l_bar = height[l]
                    if r >= h_len:
                        return empty_box_count
                    r_bar = height[r]
                    
                else:
                    empty_box = self.count_empty_box(
                        height, r, max_bar_h, max_bar_idx
                    )
                    empty_box_count += empty_box
                    l = r
                    l_bar = height[l]
                    max_bar_idx = r
                    r += 1
                    if r >= h_len:
                        return empty_box_count
                    r_bar = height[r]
                    height_diff = 0


            if r_bar > max_bar_h:
                if r - max_bar_idx > 1:
                    empty_box = self.count_empty_box(
                        height, r, max_bar_h, max_bar_idx
                    )
                    empty_box_count += empty_box
                    
                max_bar_h = r_bar
                max_bar_idx = r
                l = r
                r += 1
                l_bar = height[l]
                if r >= h_len:
                    return empty_box_count
                r_bar = height[r]
                height_diff = 0
                
            if l_bar > r_bar:
                
                diff = max_bar_h - r_bar
                if diff >= height_diff:
                    height_diff = diff
                else:
                    empty_box = self.count_empty_box(
                        height, r, max_bar_h, max_bar_idx
                    )
                    empty_box_count += empty_box
                    
                r += 1
                if r >= h_len:
                    
                    return empty_box_count
                r_bar = height[r]
                

            if l_bar < r_bar:
                if r - l > 1:
                    empty_box = self.count_empty_box(
                        height, r, max_bar_h, max_bar_idx
                    )
                    empty_box_count += empty_box
                    l = r
                    l_bar = height[l]
                    max_bar_h = r_bar
                    max_bar_idx = r
                    r += 1
                    if r >= h_len:
                        return empty_box_count
                    r_bar = height[r]
                    height_diff = 0
                else:

                    l += 1
                    r += 1
                    l_bar = height[l]
                    if r >= h_len:
                        return empty_box_count
                    
                    r_bar = height[r]
                    if l>max_bar_idx and l_bar > max_bar_h:
                      max_bar_h = l_bar
                      max_bar_idx = l
                      height_diff = 0
        return empty_box_count
                
            

                    


        