import encoder_decoder
def test1():
    print("\n********** Test 1 **********")
    msg = "a"
    k = len(msg)
    n = 1
    e = 0
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test2():
    print("\n********** Test 2 **********")
    msg = "abcdefghijk"
    k = len(msg)
    n = 35
    e = 8
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test3():
    print("\n********** Test 3 **********")
    msg = "abc"
    k = len(msg)
    n = 30
    e = 17
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test4():
    print("\n********** Test 4 **********")
    msg = "Hello"
    k = len(msg)
    n = 50
    e = 24
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test5():
    print("\n********** Test 5 **********")
    msg = "Hello World"
    k = len(msg)
    n = 25
    e = 3
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test6():
    print("\n********** Test 6 **********")
    msg = "testing"
    k = len(msg)
    n = 37
    e = 20
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test7():
    print("\n********** Test 7 **********")
    msg = "testing results"
    k = len(msg)
    n = 37
    e = 5
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test8():
    print("\n********** Test 8 **********")
    msg = "Python"
    k = len(msg)
    n = 80
    e = 44
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test9():
    print("\n********** Test 9 **********")
    msg = "PROJECT"
    k = len(msg)
    n = 70
    e = 36
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test10():
    print("\n********** Test 10 **********")
    msg = "example"
    k = len(msg)
    n = 20
    e = 4
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test11():
    print("\n********** Test 11 **********")
    msg = "decode"
    k = len(msg)
    n = 7
    e = 2
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test12():
    print("\n********** Test 12 **********")
    msg = "List decoding"
    k = len(msg)
    n = 26
    e = 0
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test13():
    print("\n********** Test 13 **********")
    msg = "message"
    k = len(msg)
    n = 35
    e = 7
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test14():
    print("\n********** Test 14 **********")
    msg = "Computer Science"
    k = len(msg)
    n = 96
    e = 20
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test15():
    print("\n********** Test 15 **********")
    msg = "Computer Science Major"
    k = len(msg)
    n = 96
    e = 22
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test16():
    print("\n********** Test 16 **********")
    msg = "codes"
    k = len(msg)
    n = 25
    e = 5
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test17():
    print("\n********** Test 17 **********")
    msg = "Reed Solomon"
    k = len(msg)
    n = 140
    e = 72
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test18():
    print("\n********** Test 18 **********")
    msg = ""
    k = len(msg)
    n = 2
    e = 0
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test19():
    print("\n********** Test 19 **********")
    msg = "Bye!"
    k = len(msg)
    n = 8
    e = 1
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def test20():
    print("\n********** Test 20 **********")
    msg = "Bye!"
    k = len(msg)
    n = 8
    e = 2
    eval_pts = [alpha for alpha in range(n)]
    encoder_decoder.run(msg, n, k, e, eval_pts)

def your_test():
    i = 1
    while 1:
        print(f"********** Test {i} **********\n")
        msg = str(input("Insert the message you wish to test, or exit to stop: "))
        if msg == "exit":
            break
        k = len(msg)
        n = int(input("Insert the \"number of evaluation points\" you want: "))
        e = int(input("Insert the \"number errors\" you want: "))
        eval_pts = [alpha for alpha in range(n)]
        encoder_decoder.run(msg, n, k, e, eval_pts)
        i+=1


if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    # test8()
    # test9()
    # test10()
    # test11()
    # test12()
    # test13()
    # test14()
    # test15()
    # test16()
    test17()
    # test18()
    # test19()
    # test20()