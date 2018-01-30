#########iterators
def check_q1():
    grade=0
    try:
        from ex8_iterators import reverse_iter
    except:
        print('error in code')

    try:
        example1=reverse_iter([1,2,3,4])
        example2=reverse_iter(['a','b','c'])


        lst1=[]
        lst2=[]
        for i in range(6):
            lst1.append(example1.next())
            lst2.append(example2.next())
        if lst1==[4, 3, 2, 1, None, None]:
            grade+=1
        else:
            print('expected (appending all results into a list): [4, 3, 2, 1, None, None]\n actual (appending all results into a list): ',lst1)
        if lst2==['c','b','a',None,None,None]:
            grade+=1
        else:
            print("expected (appending all results into a list): ['c', 'b', 'a', None, None, None]\n actual (appending all results into a list): ",lst2)
    except:
        ('error')
    return grade

def check_q2():
    grade = 0
    try:
        from ex8_iterators import roll_pair_of_dice
    except:
        print('error in roll_pair_of_dice')
        return 0
    res=[1,2,3,4,5,6]
    try:
        dice=roll_pair_of_dice()
        for i in range(20):
            temp=next(dice)
            if (temp[0] not in res) or (temp[1] not in res):
                print('error in roll_pair_of_dice: expected a tuple of numbers between 1-6')
                return 0
        return 1
    except:
        print('error in code')
        return 0

def check_q3():
    grade = 0
    try:
        from ex8_iterators import myRange
    except:
        print('error in myRange')
        return 0

    r1=myRange(0,3,1)
    r2=myRange(3,0,-1)
    r3=myRange(0,5,2)

    exp1=[0,1,2,'stop']
    exp2=[3,2,1,'stop']
    exp3=[0,2,4,'stop']

    for i in range(4):
        ind=use_generator(r1,exp1[i],'0,3,1')
        if ind==0:
            break
    if i==3:
        grade += 1


    for i in range(4):
        ind = use_generator(r2, exp2[i],'3,0,-1')
        if ind == 0:
            break
    if i==3:
        grade += 1

    for i in range(4):
        ind = use_generator(r3, exp3[i],'0,5,2')
        if ind == 0:
            break
    if i==3:
        grade += 1

    return grade

def check_f1():
    grade = 0
    err=.0001
    try:
        from ex8_2nd_order import power_function
    except:
        print('error in power function')
        return 0

    try:
        temp=2
        f2 = power_function(2)
        if abs(f2(2)-4)<err:
            grade+=1
        else:
            print('error: power_function(2)')

        temp=3
        f3 = power_function(3)
        if abs(f3(3) - 27) < err:
            grade += 1
        else:
            print('error: power_function(3)')

        temp=4
        f4 = power_function(4)
        if abs(f4(.5) - 2) < err:
            grade += 1
        else:
            print('error: power_function(4)')

        temp=5
        f5 = power_function(5)
        if abs(f5(1.5) - 11.180339887498949) < err:
            grade += 1
        else:
            print('error: power_function(5)')
    except:
        print('error in power_function(',temp,')')

    return grade

def check_f2():
    grade = 0
    err = .0001
    try:
        from ex8_2nd_order import diff_function
    except:
        print('error in diff_function')
        return 0

    try:
        function1=lambda x: x**2+2*x+1
        function2=lambda x: x**.5 +1
        your_function=diff_function(function1,function2)
        if abs(your_function(2) - 6.585786437626905) < err:
            grade += 1
        else:
            print('error: (x**2+2*x+1)-(x**.5+1) for input 2: expected: 6.585786 actual: ', your_function(2))

        your_function = diff_function(function2, function1)
        if abs(your_function(3.5) + 17.37917130661303) < err:
            grade += 1
        else:
            print('error: (x**.5+1)-(x**2+2*x+1) for input 2: expected: -17.37917130661303 actual: ', your_function(3.5))
    except:
        print('error in diff_function ')
    return grade



def check_f3():
    grade = 0
    err = .0001
    try:
        from ex8_2nd_order import get_contained_area_func
    except:
        print('error in contained_area')
        return 0

    try:
        function1=lambda x: x**2
        function2=lambda x: 0
        your_function=get_contained_area_func(0,1,100)
        if abs(your_function(function1,function2) - .33335) < err:
            grade += 1
        else:
            print('error in contained area between x**2 and 0: expected: .3335 actual: ', your_function(function1,function2))

        if abs(your_function(function2,function1) - .33335) < err:
            grade += 1
        else:
            print('error in contained area between x**2 and 0: expected: .3335 actual: ', your_function(function2,function1))
    except:
        print('error in contained_area ')
    return grade



def check_f4():
    grade = 0
    err = .0001
    try:
        from ex8_2nd_order import binary_search
    except:
        print('error in binary_search')
        return 0

    try:
        function1=lambda x: x**3
        function2=lambda x: x**5+2*x+2
        epsilon=.00001
        your_result=binary_search(function1,-1,1,epsilon)
        if abs(your_result) < epsilon:
            grade += 1
        else:
            print('error in binary_search of x**3 in [-1,1] for epsilon=.00001: expected: 0 actual: ', your_result)

        your_result = binary_search(function2, -2, 2, epsilon)
        if abs(your_result +0.817470550537109) < epsilon:
            grade += 1
        else:
            print('error in binary_search of x**5+2*x+2 in [-1,1] for epsilon=.00001: expected: 0.817470550537109 actual: ', your_result)
    except:
        print('error in binary_search ')
    return grade










def use_generator(generator,expected,string):
    try:
        temp=next(generator)
        if temp != expected:
            print('error in myRange(',string,'). expected:',expected, '  actual: ',temp )
            return 0
    except StopIteration:
        if expected!='stop':
            return 0
        else:
            return 1
    except:
        return 0
    return 1


#######second order




def main():
    grades=[]
    grades.append(check_q1())
    grades.append(check_q2())
    grades.append(check_q3())
    grades.append(check_f1())
    grades.append(check_f2())
    grades.append(check_f3())
    grades.append(check_f4())
    #print(grades)
    print('your grade is ' , sum(grades)*100/16)




