from os import name
import requests
import colorsys
#gets data and returns the name and rgb code as an tuple
def get_data():
    x = requests.get("https://www.webucator.com/article/python-color-constants-module/",verify=False).text
    codes=[]
    names=[]
    for elements in x.split("<td>"):
        if "RGB(" in elements:
            codes.append(elements)
        if "RGB(" not in elements and "#" not in elements:
            names.append(elements)
    return (codes,names)

#roughly formats all the codes for use
def format_codes(codes):
    result = []
    for i in range(len(codes)-1):
        result.append(codes[i+1].split("<")[0].split("B")[-1])
    return result

#formats all names to be used
def format_names(names):
    end_names = []
    for i in range(len(names)):
        end_names.append(names[i].split("<")[0])
    return end_names

# checks in the overlap method if there are simular color names and removes the overlap ones
def do_check(name_list,code_list):
    for elements in name_list[0:-2]:
        if check_overlap(elements,name_list[name_list.index(elements)+1]) == True:
            index = name_list.index(elements)
            del name_list[index]
            del code_list[index]
    return (name_list,tuple_rgb_codes(code_list))

#if for charekters are the same within one name the overlpaed name gets removed
def check_overlap(first,second):
    count=0
    for e in range(len(first)):
        try:
            if first[e] == second[e]:
                count+=1
        except IndexError:
            pass
    if count >2:
        return True
    else:
        return False
    
#convertes the strings into usable tuples
def tuple_rgb_codes(codes):
    tupled_codes=[]
    for rgb_codes in codes:
        codes_to_use = list(rgb_codes.split(","))
        #remove the brackets
        codes_to_use[0]=codes_to_use[0].split("(")[-1]
        codes_to_use[-1]=codes_to_use[-1].split(")")[0]
        tuple_c =[]
        for element in codes_to_use:
            tuple_c.append(int(element))
        tupled_codes.append(tuple(tuple_c))           
    return tupled_codes

def get_standart_colors(names,codes):
    standart = ["red1","blue","yellow1","springgreen","white","pink","purple","black","brown","orange"]
    standart_colors=[]
    standart_codes=[]
    for elements in names:
        for color_names in standart:
            if color_names == elements:
                standart_colors.append(elements)
                standart_codes.append(codes[names.index(elements)])
    return (standart_colors,standart_codes)

#sorting the RGB values after the HSV algorithm
def Sort(arres):
    names=[]
    code_arr = sorted(arres[1],key=lambda rgb: colorsys.rgb_to_hsv(*rgb))
    for element in code_arr:
        names.append(arres[0][arres[1].index(element)])
    return(names,code_arr)

#main funktion to get the finished data
def RGB(filtered,range_color,standart_colors):
    data = get_data()
    if standart_colors:
        temp = get_standart_colors(format_names(data[1]),format_codes(data[0]))
        return Sort(do_check(temp[0],temp[1]))
    else:
        if filtered:
            tmp = Sort(do_check(format_names(data[1]),format_codes(data[0])))
            return (tmp[0][0:range_color],tmp[1][0:range_color])
        else:
            tmp = Sort([format_names(data[1]),tuple_rgb_codes(format_codes(data[0]))])
            return (tmp[0][0:range_color],tmp[1][0:range_color])

if __name__ == "__main__":
    x=RGB(True,-1,False)
    print(x[0][68])
    print(x[1][68])
