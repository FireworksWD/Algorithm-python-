if __name__ == "__main__":
    x1,y1,x2,y2 = map(float,input().split())
    x3,y3,x4,y4 = map(float,input().split())
    area = 0
    if max(min(x1,x2),min(x3,x4)) < min(max(x1,x2),max(x3,x4)) and max(min(y1,y2),min(y3,y4)) < min(max(y1,y2),max(y3,y4)):
        area = (min(max(x1,x2),max(x3,x4)) - max(min(x1,x2),min(x3,x4))) * (min(max(y1,y2),max(y3,y4)) - max(min(y1,y2),min(y3,y4)))
        print('%.2f' % area)
    else:
        print('%.2f' % area)