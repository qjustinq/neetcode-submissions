class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 

        pointer_anchor = 0
        pointer_next = len(heights) - 1

        while pointer_anchor < pointer_next:
            
            box_height = min(heights[pointer_anchor], heights[pointer_next])
            box_width = pointer_next - pointer_anchor

            current_area = box_height * box_width
            if current_area > max_area:
                max_area = current_area

            if heights[pointer_anchor] < heights[pointer_next]:
                pointer_anchor += 1
            else:
                pointer_next -= 1
        
        return max_area
            
