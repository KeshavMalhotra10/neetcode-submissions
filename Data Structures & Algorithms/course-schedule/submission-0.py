class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #store courses and prereq in a hashmap
        courseToPre = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            courseToPre[course].append(pre)
        
        visited = set() #track which courses we already visited, so no cycle occurs

        def dfs(course):
            #check 1:
            if course in visited:
                return False
            if courseToPre[course] == []:
                return True
            visited.add(course)

            #run dfs on each prereq
            for pre in courseToPre[course]:
                if not dfs(pre): return False
            visited.remove(course)
            courseToPre[course] = []
            return True

        for course in courseToPre:
             if not dfs(course): return False
        return True
        



        

    
            
            



                
            


