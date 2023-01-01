def hex_string_to_RGB(h): 
    h = h[1:]
    h = [h[i:i+2] for i in range(0, len(h), 2)]
    
    rgb_val = [int(i, base=16) for i in h]
    rgb = ['r', 'g', 'b']
    
    return dict(zip(rgb, rgb_val))