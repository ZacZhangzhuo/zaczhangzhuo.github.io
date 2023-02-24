UpdateSkillPage = True

import re
import math

def markdown_to_dict(markdown_string):
    # split the input string into tables
    tables = re.split(r"\n\s*\n", markdown_string.strip())
    CategoryNumber = 0
    # iterate over the tables and convert each one to a list of dictionaries
    result = []
    for table in tables:
        rows = table.split('\n')
        headers = [header.strip() for header in rows[0].split('|')[2:-1]]
        headers.insert(0, "Skill")
        headers.insert(0, "Category")
        Category = rows[0].split('|')[1].strip()
        CategoryNumber += 1
        for row in rows[2:-1]:
            values = [value.strip() for value in row.split('|')[1:-1]]
            values.insert(0, Category)
            result.append(dict(zip(headers, values)))

    return result, CategoryNumber



if UpdateSkillPage:

    #! Change
    location = "zCV.md"
    #! Get the text from the md file
    md = open(location, "r", encoding="utf-8")
    mdTexts = md.read()
    mdTexts = mdTexts.split("**Professional Skills**")
    mdDic, CategoryNumber  = markdown_to_dict(mdTexts[1])
    md.close()
    # json_dump(mdDic, "zCV.json")

##! Convert string data to points part
def evenly_distributed_points_on_sphere(center, radius, n_points):
    # generate n_points evenly distributed points on a sphere with radius and center point
    phi = (1 + math.sqrt(5)) / 2.0  # golden ratio
    theta = math.pi * (3 - math.sqrt(5))  # golden angle
    points = []
    for i in range(n_points):
        y = 1 - (i / (n_points - 1)) * 2
        radius_at_height = math.sqrt(radius**2 - y**2)
        phi_increment = theta * i
        x = math.cos(phi_increment) * radius_at_height
        z = math.sin(phi_increment) * radius_at_height
        points.append([x+center[0], y+center[1], z+center[2]])
    return points


CenterPoints = evenly_distributed_points_on_sphere([0,0,0], 1, CategoryNumber)
relationships = []
sizes = [1 for i in range(CategoryNumber)]

for d in mdDic:
    

    





# ##! Point Generator Part
# maxIteration = 1000
# def Distance(point1, point2):
#     x = (point1[0] - point2[0])**2
#     y = (point1[1] - point2[1])**2
#     z = (point1[2] - point2[2])**2
#     return (x +y+ z)**0.5
# def Add(point1, point2):
#     return [point1[0] + point2[0], point1[1] + point2[1], point1[2] + point2[2]]
# def Minus(point1, point2):
#     return [point1[0] - point2[0], point1[1] - point2[1], point1[2] - point2[2]]
# def Unitize(vector):
#     length = (vector[0]**2 + vector[1]**2 + vector[2]**2)**0.5
#     if length > 0:
#         return [vector[0]/length, vector[1]/length, vector[2]/length]
#     else: return [0,0,0]
# def Multiply(vector, number):
#     return [vector[0]*number, vector[1]*number, vector[2]*number]

# for iteration in range(maxIteration):
#     totalVector = []
#     counts = []

#     for p in range(len(Points)):
#         totalVector.append([0,0,0])
#         counts.append(0)
    
#     for i in range(len(Points)):
#         for j in range(i+1, len(Points)):

#             distance = Distance(Points[i], Points[j])
#             subVector = Minus(Points[i], Points[j])
#             subVector = Unitize(subVector)

#             subVector =Multiply( subVector, (Radiuses[i] + Radiuses[j] - distance))
#             totalVector[i] = Add(totalVector[i],subVector)
#             totalVector[j] =Minus(  totalVector[j],subVector)
#             counts[i] += 1
#             counts[j] += 1
#     isContinue = True
#     for k in range(len(Points)):
#         if counts[k] != 0:
#             move =Multiply( totalVector[k], 1/((float)(counts[k])))

#             if Distance(move,[0,0,0]) > 0.01:isContinue = False

#             Points[k] = Add(Points[k], move)
#     if isContinue:
#         print ("Iteration: " + str(iteration))
#         break



