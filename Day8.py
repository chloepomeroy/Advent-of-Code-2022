#!/usr/bin/env python
# coding: utf-8

# In[3]:


text_file = open("day8.txt", "r")
data = text_file.read()
rows= data.split('\n')


# In[4]:


grid = [list(row) for row in rows]


# In[15]:


def trees(grid):
    visible = 2*len(grid) + 2*(len(grid[0])-2)
    inside_visible = []
    for i in range(1,len(grid)-1):
        row_items_left = [int(grid[i][0])]
        row_items_right = [int(grid[i][len(grid[i])-1])]
    
        for j in range(1,len(grid[i])-1):
            if int(grid[i][j])>max(row_items_left):
                inside_visible.append(f"{i}, {j}")
            else:
                pass
            row_items_left.append(int(grid[i][j]))

        for k in range(len(grid[i])-2, 0, -1):
            if int(grid[i][k])>max(row_items_right):
                inside_visible.append(f"{i}, {k}")
            else:
                pass
            row_items_right.append(int(grid[i][k]))
        
    unzip_lst = zip(*grid)
    grid_col = []
    for l in unzip_lst:
        col = []
        for m in l:
            col.append(m)
        grid_col.append(col)
        
    for n in range(1,len(grid_col)-1):
        col_items_left = [int(grid_col[n][0])]
        col_items_right = [int(grid_col[n][len(grid_col[n])-1])]
    
        for o in range(1,len(grid_col[n])-1):
            if int(grid_col[n][o])>max(col_items_left):
                inside_visible.append(f"{o}, {n}")
            else:
                pass
            col_items_left.append(int(grid_col[n][o]))

        for p in range(len(grid_col[n])-2, 0, -1):
            if int(grid_col[n][p])>max(col_items_right):
                inside_visible.append(f"{p}, {n}")
            else:
                pass
            col_items_right.append(int(grid_col[n][p]))
    
    result = visible+len(set(inside_visible))
        
    return(result)
    


# In[22]:


print(f"part 1 answer: {trees(grid)}")


# In[266]:


def get_scenic_score(grid):
    lr_scores = {}
    scenic_scores = {}
    
    unzip_lst = zip(*grid)
    grid_col = []
    for i in unzip_lst:
        col = []
        for j in i:
            col.append(j)
        grid_col.append(col)
        
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            trees_seen_l = []
            trees_seen_r = []
            treehouse = int(grid[row][col])
            left = [0]
            right=[0]
            for k in range(col-1, -1, -1):
                if max(left)<treehouse:                    
                    trees_seen_l.append(f"{row}, {k}")
                left.append(int(grid[row][k]))
                
            for k in range(col+1, len(grid[row])):
                if max(right)<treehouse:
                    trees_seen_r.append(f"{row}, {k}")
                right.append(int(grid[row][k]))
            
            lr_scores[f"{row}, {col}"] = len(trees_seen_l)*len(trees_seen_r)
                
    for col in range(0, len(grid_col)):              
        for row in range(0, len(grid_col[col])):
            trees_seen_u = []
            trees_seen_d = []
            treehouse = int(grid_col[col][row])
            up=[0]
            down=[0]
            for k in range(row-1, -1, -1):
                if max(up)<treehouse:                    
                    trees_seen_u.append(f"{col}, {k}")
                up.append(int(grid_col[col][k]))
                
            for k in range(row+1, len(grid_col[col])):
                if max(down)<treehouse:
                    trees_seen_d.append(f"{col}, {k}")
                down.append(int(grid_col[col][k]))
                
            key = f"{row}, {col}"
            
            scenic_scores[key] = lr_scores.get(key)*len(trees_seen_u)*len(trees_seen_d)
    
    return max(scenic_scores.values())
                    
        


# In[267]:


print(f"part 2 answer: {get_scenic_score(grid)}")


# In[ ]:




