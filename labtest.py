def lab2rgb(lab):
    y = (lab[0] + 16) / 116.0
    x = lab[1] / 500.0 + y
    z = y - lab[2] / 200.0

    x = 0.95047 * ((x * x * x) if (x * x * x > 0.008856) else ((x - 16/116.0) / 7.787));
    y = 1.00000 * ((y * y * y) if (y * y * y > 0.008856) else ((y - 16/116) / 7.787));
    z = 1.08883 * ((z * z * z) if (z * z * z > 0.008856) else ((z - 16/116) / 7.787));

    r = x *  3.2406 + y * -1.5372 + z * -0.4986;
    g = x * -0.9689 + y *  1.8758 + z *  0.0415;
    b = x *  0.0557 + y * -0.2040 + z *  1.0570;

    r = (1.055 * (r**(1/2.4)) - 0.055) if (r > 0.0031308) else (12.92 * r);
    g = (1.055 * (g**(1/2.4)) - 0.055) if (g > 0.0031308) else (12.92 * g);
    b = (1.055 * (b**(1/2.4)) - 0.055) if (b > 0.0031308) else (12.92 * b);

    return [max(0, min(1, r)) * 255, max(0, min(1, g)) * 255, max(0, min(1, b)) * 255]



def rgb2lab(rgb):
    r = rgb[0] / 255.0
    g = rgb[1] / 255.0
    b = rgb[2] / 255.0

    r = ((r + 0.055) / 1.055)**2.4 if (r > 0.04045) else (r / 12.92);
    g = ((g + 0.055) / 1.055)**2.4 if (g > 0.04045) else (g / 12.92);
    b = ((b + 0.055) / 1.055)**2.4 if (b > 0.04045) else (b / 12.92);

    x = (r * 0.4124 + g * 0.3576 + b * 0.1805) / 0.95047;
    y = (r * 0.2126 + g * 0.7152 + b * 0.0722) / 1.00000;
    z = (r * 0.0193 + g * 0.1192 + b * 0.9505) / 1.08883;

    x = x**(1/3.0) if (x > 0.008856) else (7.787 * x) + 16/116.0;
    y = y**(1/3.0) if (y > 0.008856) else (7.787 * y) + 16/116.0;
    z = z**(1/3.0) if (z > 0.008856) else (7.787 * z) + 16/116.0;

    return [(116.0 * y) - 16.0, 500.0 * (x - y), 200.0 * (y - z)]

def deltaE(labA, labB):
    deltaL = labA[0] - labB[0];
    deltaA = labA[1] - labB[1];
    deltaB = labA[2] - labB[2];
    c1 = (labA[1] * labA[1] + labA[2] * labA[2])**0.5;
    c2 = (labB[1] * labB[1] + labB[2] * labB[2])**0.5;
    deltaC = c1 - c2;
    deltaH = deltaA * deltaA + deltaB * deltaB - deltaC * deltaC;
    deltaH = 0 if (deltaH < 0) else (deltaH)**0.5;
    sc = 1.0 + 0.045 * c1;
    sh = 1.0 + 0.015 * c1;
    deltaLKlsl = deltaL / (1.0);
    deltaCkcsc = deltaC / (sc);
    deltaHkhsh = deltaH / (sh);
    i = deltaLKlsl * deltaLKlsl + deltaCkcsc * deltaCkcsc + deltaHkhsh * deltaHkhsh;
    return 0 if (i < 0) else (i)**0.5;
    
#Test calls -----------------
print (rgb2lab([10,25,50]))
#print lab2rgb(rgb2lab([10,25,50]))
#print deltaE(rgb2lab([10,25,50]),rgb2lab([20,30,40]))
