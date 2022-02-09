##Name:Mohamed Khaled Ahmed Atyaa
##group: 3 Alex
##Question 1
# def function(x):
#     return 2*x**2+6*x+4
# def bisection(f,a,b,tolerance):
#     count = 0
#     while abs(b-a)>tolerance:
#         g=(a+b)/2
#         if f(a)*f(g)<0:
#             b=g
#             count+=1
#         else:
#             a=g
#             count+=1
#     return g,count
# root,count=bisection(function,-3,-1.5,1e-5)
# print("bisection method ---> root:",root," and # of iteration:",count)
# ###############################################
# def g(x):
#     return ((-x**2-2)/3)
# def fixed_point(f,p,tolerance):
#     p1=p
#     p2=g(p1)
#     count=0
#     while abs(p2-p1)>tolerance:
#         p1=p2
#         p2=g(p1)
#         count+=1
#     return p2,count
# root,count=fixed_point(g,-1.5,1e-5)
# print("fixed point method ---> root:",root," and # of iteration:",count)
# ######################################
# def f(x):
#     return 2*x**2+6*x+4
# def df(x):
#     return 4*x+6
# def newton(f,df,p,tolerance):
#     x1=p
#     x2=x1-f(x1)/df(x1)
#     count=0
#     while abs(x2-x1)>tolerance:
#         x1=x2
#         x2 = x1 - f(x1) / df(x1)
#         count+=1
#     return x2,count
# root,count=newton(f,df,-3,1e-5)
# print("newton method ---> root:",root," and # of iteration:",count)
##  We see that newton method has the smallest number of iterations so it usually be optimized for many functions
###############################################
###Question 2
# import numpy as np
# def g(x):
#     return np.log(5*x-2)
# def e(x):
#     (np.exp(x)+2)/5
# def fixed_point(f,p,tolerance):
#     p1=p
#     p2=g(p1)
#     count=0
#     while abs(p2-p1)>tolerance:
#         p1=p2
#         p2=g(p1)
#         count+=1
#     return p2,count
# root1,count1=fixed_point(g,2.5,1e-5)
# root2,count2=fixed_point(e,2.5,1e-5)
# print("fixed point method ---> root:",root1," and # of iteration:",count1,"with g(x)=log(5x-2)")
# print("fixed point method ---> root:",root2," and # of iteration:",count2,"with e(x)=exp(x)+2/5")
####we see the tow functions at the same intial point have the same # of iterations
#########################################################################
###Question 3
# import numpy as np
# def f(x):
#     return np.exp(x)-5*x+2
# def df(x):
#     return np.exp(x)-5
# def bisection(f,a,b,tolerance):
#     count = 0
#     while abs(b-a)>tolerance:
#         g=(a+b)/2
#         if f(a)*f(g)<0:
#             b=g
#             count+=1
#         else:
#             a=g
#             count+=1
#     return g,count
# def newton(f,df,p,tolerance):
#     x1=p
#     x2=x1-f(x1)/df(x1)
#     count=0
#     while abs(x2-x1)>tolerance:
#         x1=x2
#         x2 = x1 - f(x1) / df(x1)
#         count+=1
#     return x2,count
# root,count=bisection(f,2,3,1e-5)
# print("bisection method ---> root:",root," and # of iteration:",count)
# root,count=newton(f,df,1,1e-5)
# print("newton method ---> root:",root," and # of iteration:",count)
# ##we see that newton method converge after 3 iteration as the intial guess is very close to the root
########################################
###Question 4
# def function(x):
#     return x**3+2*x**2+10*x-20
# def bisection(f,a,b,tolerance):
#     count = 0
#     while abs(b-a)>tolerance:
#         g=(a+b)/2
#         if f(a)*f(g)<0:
#             b=g
#             count+=1
#         else:
#             a=g
#             count+=1
#     return g,count
# root,count=bisection(function,1,2,1e-5)
# print("bisection method ---> root:",root," and # of iteration:",count)
###############################################
# def f(x):
#     return x**3+2*x**2+10*x-20
# def df(x):
#     return 3*x**2+4*x+10
# def newton(f,df,p,tolerance):
#     x1=p
#     x2=x1-f(x1)/df(x1)
#     count=0
#     while abs(x2-x1)>tolerance:
#         x1=x2
#         x2 = x1 - f(x1) / df(x1)
#         count+=1
#     return x2,count
# root,count=newton(f,df,1.5,1e-5)
# print("newton method ---> root:",root," and # of iteration:",count)
#################################################













































