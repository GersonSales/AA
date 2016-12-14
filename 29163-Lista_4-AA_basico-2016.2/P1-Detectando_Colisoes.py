#http://br.spoj.com/problems/COLISAO7/

stRectangle = map(int, raw_input().split())
ndRectangle = map(int, raw_input().split())

def intercept(r1, r2):
        return r1[0] > r2[2] or r2[0] > r1[2] or r1[1] > r2[3] or r2[1] > r1[3]

if(intercept(stRectangle, ndRectangle)):
    print 0
else:
    print 1




