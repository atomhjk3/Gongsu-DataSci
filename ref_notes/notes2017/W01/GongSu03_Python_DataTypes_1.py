
# coding: utf-8

# # 파이썬 기본 자료형 1부

# 파이썬 언어에서 사용되는 값들의 기본 자료형을 살펴본다. 
# 
# 변수에 할당될 수 있는 가장 단순한 자료형에는 네 종류가 있다:
# 
# * 정수 자료형(`int`): 
#     * ..., `-3`, `-2`, `-1`, `0`, `1`, `2`, `3`, 등등
#     * `1 + 2`, `-2 * 3`, 등등
# 
# 
# * 부동소수점 자료형(`float`): 
#     * `1.2`, `0.333333`, `-1.2`, `-3.7680`, 등등 
#     * `2.0 \ 3.5`, `3.555 + 3.4 * 7.9`, 등등
#     
#         
# * 불리언 자료형(`bool`): `True`, `False`를 포함하여 두 값으로 계산될 수 있는 값
#     * 예: `1 == 1`, `2 < 3`, `1 + 1 > 3 and 2 < 3`, 등등
# 
# 
# * 문자열 자료형(`str`): 
#     * `'a'`, `'abc'`, `'enginneering'`, ... 등등
#     * `'abc' * 2`, `'engineering' + 'math'`, 등등
#     
# 
# 이번 장 주요 내용:
# 
# * 정수, 부동소수점, 불리언 자료형을 소개. 문자열 자료형은 다음 장에서 다룸.
# 
# * 변수에 할당된 값과 그 값의 자료형을 알아내는 데에 사용하는 두 개의 함수의 기본적인 활용법 
# 
#     * `print()` 함수: 변수에 할당된 값을 확인할 때 사용 
#     * `type()` 함수: 값의 자료형을 확인할 때 사용
# 
# 
# * 특정 자료형과 관련하여 많이 사용되는 함수와 메소드 살펴보기 

# ## 파이썬 명령어 기초 사용법

# Spyder, IDLE 등을 사용하여 파이썬 명령어를 실행할 수 있다.
# 
# 명령 프롬프트(prompt)는 보통 아래의 모양을 갖는다.
# 
# * `>>>`
# 
# 또는
# 
# * `In [1]:`

# 파이썬은 "스크립트 언어"에 속한다. 즉, 코드를 작성한 후에 바로 실행시킬 수 있다. 
# C와 Java 등의 언어는 코드를 작성한 후에 코드가 들어 있는 파일을 컴파일하여 생성된 목적코드(object code)를 실행하기 때문에 컴파일 언어라고 불린다.  

# 예를 들어, `print()` 함수를 이용하여 터미널 화면에 문자열 값을 보여주고 싶다면 단순히 아래와 같이 코드를 작성하고 실행하면 된다. 
# 
# 주의: `print`는 "출력하다", "화면에 보여주다", "인쇄하다" 등으로 번역한다. 반면에 함수를 정의할 때 사용하는 `return`은 "값을 돌려준다" "리턴한다" 등으로 번역하여 사용한다. `print`와 `return`은 사용 용도다 서로 완전히 다르다. 나중에 차이점을 배우게 된다.

# In[1]:

print("Hello World")


# 변수를 선언하고 값을 바로 확인할 수 있다.

# In[2]:

a = 1 + 1
a


# 파이썬을 계산기처럼 활용할 수도 있다.

# In[3]:

2 + 3


# In[4]:

a = 2 + 3
a + 1


# In[5]:

42 - 15.3


# In[6]:

100 * 11


# In[7]:

7 / 2


# 주의: 
# 
# * 파이썬2에서는 나눗셈 연산자(`/`)는 정수 자료형인 경우 몫을 계산한다. 반면에 부동소수점이 사용되면 부동소수점을 리턴한다.
# 
# 
# * 파이썬3에서는 나눗셈 연산자(`/`)는 무조건 부동소수점을 리턴한다. 
# 
#         In [22]: 7 / 2
#         Out[22]: 3.5

# In[8]:

7.0 / 2


# 나머지를 계산하는 연산자는 `%` 이다.

# In[9]:

7%5


# 지수 계산: 예를 들어, 2의 3승을 계산하고자 할 때 사용한다.

# In[10]:

2 ** 3


# In[11]:

9 ** 0.5


# ## 변수 선언 및 활용
# 
# 컴퓨터 프로그램을 데이터를 이용하여 다음과 같은 일들을 처리하기 위한 명령문들의 나열로 생각할 수 있다.
# * 데이터 읽기
# * 데이터 생성하기
# * 데이터 계산하기
# * 데이터 변환하기
# * 데이터 정리하기
# * 데이터 저장하기
# 
# 특정 데이터를 조작하기 위해서는 해당 데이터를 저장하거나 불러올 수 있어야 한다. 그러기 위해서 변수를 활용한다. 
# 변수를 일종의 그릇에 비유할 수 있으며, 변수에 할당된 데이터는 그릇에 담겨진 내용물에 해당한다. 
# 
# 파이썬에서 변수의 이름을 지으려면 기본적으로 세 가지 규칙을 따라야 한다.
# 
# * 반드시 영어 알파벳 문자(`a-z,A-Z`) 또는 밑줄기호(`_`)로 시작해야 하며, 이후에는 알파벳, 숫자(`0-9`), 밑줄기호가 임의로 사용될 수 있다.
# 
# * 파이썬 예약어(def, from, import 등)를 변수 이름으로 사용하면 안된다. 
# 
# * 대소문자를 구분해야 한다: 'YOU', 'you', 'You', 'yOu'는 모두 다른 이름으로 처리된다. 
# 
# * '-', '+', '*','/' 등의 연산자 기호는 이름에 사용될 수 없다. 
# 
# * '@', '$', '?' 등의 기호도 사용되지 않는다. 

# ## 변수 선언

# 변수에 특정 값을 할당하는 것을 변수 선언이라 부른다. 
# 변수 선언은 아래 모양을 갖춘다.
# 
#     변수이름 = 할당할 값
#     
# 예를 들어 아래에서 `a_number`라는 변수이름에 정수 2가 할당되었고, `a_word` 변수에는 `dog`라는 문자열이 할당되었다.   

# 주의:
# 
# * 변수를 생성하고자 할 때 값을 초기화하면 된다. 즉, 변수를 미리 선언할 필요가 없다. C와 Java와의 주요 차이점 중의 하나이다.
# 
# * 자료형을 선언할 필요가 없다. 변수의 자료형을 파이썬이 알아서 판단한다. 이를 동적 타이핑(dynamic typing)이라 한다. 

# In[12]:

# int a_number = 2 
a_number = 2
a_word = 'dog'


# 예를 들어, C 언어의 경우 아래와 같이 선언해야 한다.
# 
#     int a_number = 2 
#     char a_word[] = 'dog'

# 변수에 할당된 값을 확인하기 위해 `print()` 함수를 이용한다.

# In[13]:

print(a_number)


# In[14]:

print(a_word)


# 변수에 할당된 값의 자료형을 확인하려면 `type()` 함수를 호출한다.

# In[15]:

type(a_number)


# In[16]:

type(a_word)


# 선언된 변수를 이용하여 연산을 할 수도 있다.

# In[17]:

a_number + 7


# In[18]:

(a_number * 6.0) / 5


# 연산의 결과를 변수에 할당할 수 있다. 해당 변수에는 연산의 결과만을 기억한다. 

# In[19]:

first_result = 8 / 3.5
first_result


# 계산된 결과의 자료형도 `type()` 함수를 이용하여 확인할 수 있다.

# In[20]:

type(first_result)


# 문자열의 경우 덧셈과 곱셈 연산자를 사용할 수 있다.

# In[21]:

"Bull " + a_word


# In[22]:

a_word * 2


# 하지만 변수에 할당된 값의 자료형에 따라 연산의 가능여부가 결정된다. 
# 예를 들어, 숫자의 문자열의 합은 정의되어 있지 않으며, 실행할 경우 오류가 발생한다.

# In[23]:

a_number + a_word


# 주의: 오류 내용을 초보자가 이해하기는 어렵다. 여기서는 자료형이 맞지 않아 오류가 발생할 경우에 `TypeError`가 발생한다는 사실만을 기억해 두면 좋다. 

# 변수에 할당된 값은 변경이 가능하다. 원래 할당된 값을 변경할 수 있다는 의미에서 변수라 부른다. 변수가 아닌 숫자를 상수라 부른다. 

# In[24]:

print(a_number)
a_number = 5

print(a_number)


# ## 기본 자료형
# 
# 파이썬에는 8개의 자료형이 미리 선언되어 있다. 그중 네 개는 단순자료형이며, 나머지 네 개는 컬렉션 자료형(모음 자료형)이다. 
# 
# ### 단순 자료형
# 
# 하나의 값만을 대상으로 한다는 의미에서 단순 자료형이다. 즉, 정수 하나, 부동소수점 하나, 불리언 값 하나, 문자열 하나 등등.
# 
# * 정수(int)
# * 부동소수점(float)
# * 불리언 값(bool)
# * 문자열(str)
# 
# ### 컬렉션 자료형
# 
# 여러 개의 값들을 하나로 묶어서 다룬다는 의미에서 컬렉션 자료형이다.
# 
# * 리스트(list)
# * 튜플(tuple)
# * 집합(set)
# * 사전(dictionary)
# 
# 여기서는 단순 자료형을 소개하고, 컬렉션 자료형은 이후에 다룬다.

# ### 정수(int)
# 
# 일반적으로 알고 있는 정수(자연수, 0, 음의 정수)들의 자료형을 나타내면 덧셈, 뺄셈, 곱셈, 나눗셈 등의 일반 연산이 가능하다. 

# **주의**: 정수들의 나눗셈의 결과는 부동소수점이다. 
# 
# 파이썬3에서 처럼 정수들의 나눗셈이 부동소수점이 되도록 하려면 아래 명령어를 먼저 실행하면 된다.
# 최신 버젼인 파이썬3과의 호환성을 위해 필요할 수 있다.
# 
#     from __future__ import division
#     
#     In [4]: 8 / 5
#     Out[4]: 1.6
#     
# 위 명령어를 실행한 후에 기존의 정수들의 나눗셈 연산을 위해서는 몫을 계산하는 연산자인 `//`을 사용하면 된다.
# 
#     In [5]: 8 // 5
#     Out[5]: 1
# 
#     In [5]: 8 % 5
#     Out[5]: 3

# ### 부동소수점(float)
# 
# 부동소수점은 원래 실수를 컴퓨터에서 다루기 위해 개발되었으나 실제로는 유리수 일부만을 다룬다. 
# 무리수인 원주율 pi의 경우에도 컴퓨터의 한계로 인해 소수점 이하 적당한 자리에서 끊어서 사용한다. 

# In[25]:

new_float = 4.0
print(new_float)


# 정수와 실수 사이에 강제로 형변환 가능하다. 실수를 정수로 변환하고자 할 경우 `int()` 함수를 사용한다. 그러면 소수점 이하는 버려진다. 

# In[26]:

int(4.8)


# 정수를 실수로 형변환하려면 `float()` 함수를 사용한다.

# In[27]:

float(2)


# **주의**: 변수를 형변환한다고 해서 변수에 할당된 값이 변하는 것은 아니다. 다만, 형변환한 값을 다른 변수에 저장해서 활용할 수는 있다.

# In[28]:

basic_int = 2
print(float(basic_int))
print(type(basic_int))


# In[29]:

float_basic_int = float(basic_int)
print(type(float_basic_int))


# ### 키워드 관련 주의사항
# 
# 지금까지 살펴보았듯이 `float`, `int`, `print`, `type`와 같은 단어는 녹색으로 표시되는데 이는 그 단어들이 파이썬에서 특별한 역할을 수행하는 키워드이기 때문이다. 
# 
# 그런 키워드를 재정의할 수는 있지만 하지 않는 것이 좋다. 
# 혹여 실수로 아래와 같은 일을 할 수도 있는데 매우 조심해야 한다.

# In[30]:

int = 4
print("What have we done to int?", int)
int(5.0)


# 즉, `int()` 함수의 본래의 정의가 사라졌다. 이럴 때는 아래와 같이 원래의 함수로 되돌릴 수 있다.

# In[31]:

del int
int(5.0)


# ### 연산자 우선순위
# 
# 일반적으로 알려진 연산자들 사이의 우선순위를 알아야 한다. 
# 줄여서 PEMDAS(펨다스)로 기억하면 좋다. 
# 
# PEMDAS: 
# * 괄호(Parentheses)
# * 지수승(Exponents)
# * 곱셈(Multiplication)
# * 나눗셈(Division)
# * 덧셈(Addition)
# * 뺄셈(Subtraction).
# 
# 왼쪽에 오는 연산자의 우선순위가 높다.
# 지수승을 나타내는 기호는 `**`이다.

# In[32]:

eqn1 = 2 * 3 - 2
print(eqn1)


# In[33]:

eqn2 = -2 + 2 * 3
print( eqn2 )


# In[34]:

eqn3 = -2 + (2 % 3)
print( eqn3 )


# In[35]:

eqn4 = (.3 + 5) // 2
print(eqn4)


# In[36]:

eqn5 = 2 ** 4 // 2
print(eqn5)


# ## 불리언 값(bool)
# `if` 또는 `while` 문에서 사용되는 불리언 자료형에는 두 개의 값만 사용된다.
# * `True`
# * `False`
# 
# 이 두 개의 값만을 이용하여 복잡한 프로그램을 구현할 수 있다.
# 
# 예제: 강아지를 한 마리만 갖고 있다고 가정하자. 
# 
# 이것을 표현하기 위해 puppy(강아지 한마리)라는 변수에 True를 할당하고, 여러 마리의 강아지를 뜻하는 puppies 변수에는 False를 할당한다.

# In[37]:

puppy = True


# In[38]:

print(puppy)


# In[39]:

type(puppy)


# In[40]:

puppies = False


# 두 개의 변수 선언을 아래와 같이 동시에 할 수 있다. 등호기호 왼편과 오른편에 사용되는 변수와 값의 개수가 동일해야 함에 주의한다.

# In[41]:

puppy, puppies = True, False


# In[42]:

print("Do I have a puppy?", puppy)
print("Do I have puppies?", puppies)


# 주의: 위에서 사용된 print함수의 사용법을 기억해둔다. print 함수는 인자를 여러 개 받을 수 있으며 그 값들을 차례대로 동시에 한 줄에 출력한다. 각각의 값들은 스페이스(space)로 구분되어진다.

# ### 불리언 연산자
# 
# `and`, `not`, `or` 세 개의 연산자를 이용하여 불리언 연산을 할 수 있다. 각 연산자의 의미는 일반적으로 알려진 것과 동일하다.

# In[43]:

True and True


# In[44]:

True and False


# 불리언 자료형의 변수를 이용하여 연산을 수행할 수도 있다.

# In[45]:

puppy and puppies


# In[46]:

not puppies


# In[47]:

not puppy


# ### 불리언 연산자 우선순위

# not 연산자의 우선순위가 가장 높다.

# In[48]:

puppy and not puppies


# In[49]:

puppy or puppies


# In[50]:

False or False


# ### 숫자 비교
# 
# 일반적으로 사용하는 숫자들의 비교를 나타내는 연산자들은 다음과 같다. 리턴값은 모두 불리언 자료형이다.
# 
# * `!=`: 다른지 여부를 판단
# * `==`: 같은지 여부를 판단
# * `<=`: 작거나 같은지 여부를 판단
# * `>=`: 크거나 같은지 여부를 판단
# * `<`: 작은지 여부를 판단
# * `>`: 큰지 여부를 판단

# In[51]:

4 == 4


# In[52]:

4 == 5


# In[53]:

4 != 2


# In[54]:

4 != 4


# In[55]:

4 > 2


# In[56]:

4 > 4


# In[57]:

4 >= 4


# In[58]:

False or False


# ## 연습문제

# ### 연습 

# 두 숫자의 평균값을 구하는 함수를 아래와 같이 작성할 수 있다.
# 
# 주의: 함수에 대해서는 이후에 좀 더 자세히 다룬다. 여기서는 함수를 작성하는 방식에 주의한다. 
# 
# 함수 작성요령:
# ```
# def 함수이름(인자1, 인자2, ..., 인자k):
#     함수본체
#     return 리턴값
# ```

# In[59]:

def average(a, b):
    """ 두 개의 숫자 a와 b가 주어졌을 때,
    두 숫자의 평균을 리턴하는 함수"""

    return (a + b) * 0.5


# 주의: 
# 
# * 큰 따옴표 세 개("""...""")로 둘러싸인 부분은 문서화를 위해 사용되며 주석으로 처리된다.
# 즉, 정의되는 함수의 의미와 역할에 대한 설명을 담는다. 영어로 독스트링(docstring)이라 부른다. 
# 
# * 주석 등에 한글을 사용하고자 할 경우 아래 문장이 문서 맨 첫줄에 있어야 한다.
# ```
#     # coding: utf-8
# ```

# In[60]:

average(10, 20)


# In[61]:

average(10, 4)


# 함수에 대한 정보를 얻고자 할 경우 `help()` 함수를 활용할 수 있다. 
# 그러면 앞서 `average` 함수를 정의할 때 함께 적어 넣은 독스트링이 보여진다.

# In[62]:

help(average)


# ### 연습
# 
# 두 숫자 `a`와 `b`의 사이의 거리를 리턴하는 함수 `distance(a, b)`를 정의하라.
# 
# 활용 예:
# ```
# In [11]: distance(3, 4)
# Out[11]: 1
# 
# In [12]: distance(3, 1)
# Out[12]: 2
# ```

# 아래 코드에서 `pass` 부분을 수정해서 채워야 한다. 
# ```
# def distance(a, b):
#     """if-else문을 사용하지 않고도 가능하다."""
#     pass
# ```    

# 견본답안:

# In[63]:

def distance(a, b):
    return abs(a-b)


# `abs` 함수는 인자로 입력된 숫자의 절대값을 리턴하는 함수이다.

# In[64]:

distance(3, 4)


# In[65]:

distance(3, 1)


# ### 연습
# 
# 두 숫자의 기하평균(geometric mean)을 리턴하는 함수 `geometric_mean(a, b)` 함수를 정의하라. 
# 
# 두 숫자 `a`와 `b`의 기하평균을 `c`라 하면, 두 변의 길이가 각각 `a`와 `b`인 직사각형의 넓이와 변의 길이가 `c`인 정사각형의 넓이가 동일함을 의미한다. 
# 
# 활용 예:
# 
#     In [ ]: geometric_mean(2, 2)
#     Out[ ]: 2.0
# 
#     In [ ]: geometric_mean(2, 8)
#     Out[ ]: 4.0
# 
#     In [ ]: geometric_mean(2, 1)
#     Out[ ]: 1.4142135623730951
#     
# 힌트: 제곱근을 계산해주는 `sqrt()`를 이용한다. 단, `sqrt()` 함수를 이용하려면 먼저 `math` 라는 모듈을 아래와 같이 임포트 해야 한다.
# ```
# import math
# ```
# 
# 이후에 `math.sqrt(3)`와 같은 형식으로 제곱근 함수를 호출할 수 있다.

# 견본답안:

# In[66]:

import math

def geometic_mean(a, b):
    c = math.sqrt(a * b)
    return c


# sqrt에 대해 알고 싶으면 help 함수를 활용한다.
# ```
# help(math.sqrt)
# ```

# In[67]:

geometic_mean(2, 2)


# In[68]:

geometic_mean(2, 8)


# In[69]:

geometic_mean(2, 1)


# ### 연습
# 
# 바닥면적이 `A`이고 높이가 `h`인 피라미드의 부피를 리턴하는 함수 `pyramid_volume(A, h)`를 정의하라. 
# 
# 활용 예:
# 
#     In [ ]: pyramid_volume(1, 2)
#     Out[ ]: 0.6666666666666666

# 견본답안:

# In[70]:

def pyramid_volume(A, h):
    """4각뿔의 부피는 밑면적 * 높이 * 1/3
    리턴값이 항상 float 자료형이 되도록 한다."""

    V = A * h / 3.0
    return V


# 주의: 3이 아니라 3.0으로 나누는 것에 주의하라. 파이썬3에서는 상관이 없다.

# In[71]:

pyramid_volume(1, 2)


# ### 연습
# 
# 초(second) 단위의 숫자를 받아서 일(day) 단위의 값으로 되돌려주는 `seconds2days(n)` 함수를 정의하라. 입력값은 `int` 또는 `float` 일 수 있으며 리턴값은 `float` 자료형이어야 한다.
# 
# 활용 예:
# 
#     In [ ]: seconds2days(43200)
#     Out[ ]: 0.5

# 견본답안:

# In[72]:

# 하루는 아래 숫자만큼의 초로 이루어진다.
# 하루 = 24시간 * 60분 * 60초.

daysec = 60 * 60 * 24

# 이제 초를 일 단위로 변경할 수 있다.
def seconds2days(sec):
    """ sec을 일 단위로 변경하는 함수.
    강제형변환에 주의할 것"""
    
    return (float(sec) / daysec)


# In[73]:

seconds2days(43200)


# 파이썬3의 경우에는 아래와 같이 정의해도 된다.
# ```
# def seconds2days(sec):
#     return (sec / daysec)
# ```

# ### 연습
# 
# 변의 길이가 각각 `a`, `b`, `c`인 직각육면체의 표면적을 계산해주는 함수 `box_surface(a, b, c)`를 정의하라. 
# 예를 들어, 박스를 페인트칠하고자 할 때 필요한 페인트의 양을 계산하는 문제이다.
# 
# 활용 예:
# 
#     In [ ]: box_surface(1, 1, 1)
#     Out[ ]: 6
# 
#     In [ ]: box_surface(2, 2, 3)
#     Out[ ]: 32

# 견본답안:

# In[74]:

def box_surface(a, b, c):
    """ 각 변의 길이가 각각 a, b, c인 박스의 표면적을 리턴하는 함수.
    힌트: 6개의 면의 합을 구하면 된다"""

    s1, s2, s3 = a * b, b * c, c * a
    return 2 * (s1 + s2 + s3)


# In[75]:

box_surface(1, 1, 1)


# In[76]:

box_surface(2, 2, 3)


# ### 연습
# 
# 변의 길이가 각각 `a`, `b`, `c`인 삼각형의 면적 `A`를 계산하는 함수 `triangle_area(a, b, c)`를 정의하라. 
# 다음 등식을 이용할 수 있다. 
# 
#     A = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#     s = (a + b + c) / 2
#     
# 아래 사이트 참조:
# 
# https://ko.wikipedia.org/wiki/%EC%82%BC%EA%B0%81%ED%98%95

# 견본답안:

# In[77]:

def triangle_area(a, b, c):
    s = (a + b + c) / 2.0
    A = (s * (s - a) * (s - b) * (s - c))
    
    return math.sqrt(A)


# In[78]:

triangle_area(2, 2, 3)
