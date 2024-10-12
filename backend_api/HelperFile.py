

class HelperClass:
    def sortProjectData(self, featuredProject , basicProject):
        data = []
        i, j = 0, 0
        m = len(featuredProject)
        n = len(basicProject)
        imgCounter = 0
        
        while i < m or j < n:
            #use to insert featured project in array
            if i < m:
                data.append(featuredProject[i])
                i += 1
            
            #use to insert basic project and image at middle row after row
            cnt = 0
            while(j < n and cnt < 3):
                if imgCounter % 6 == 1:
                    data.append({'img': "true"})
                else:
                    data.append(basicProject[j])
                    j += 1
                imgCounter += 1
                cnt += 1
        return data