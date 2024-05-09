def numberOfLines(widths,s):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r','s','t','u','v','w','x','y','z']
    alp_with_values = {}
    pixels =0
    last_value=0
    line_count =1
    for i in range(len(alphabets)):
        alp_with_values[alphabets[i]] = widths[i]
    for i in s:
        pixels+=alp_with_values[i]
        if pixels>100:
            line_count+=1
            pixels =alp_with_values[i]
            
    print(line_count,pixels)
            
    

widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "bbbcccdddaaa"   
numberOfLines(widths,s)    
