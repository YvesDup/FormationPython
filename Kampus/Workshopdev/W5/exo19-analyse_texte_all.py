#import os
#import random
import sys
import time

def analyse_texte_v1(text: str, *args):
    """
    """
    # print("in params:", text, args)
    all_strs = (text,) + args
    all_strs = [x for x in all_strs if isinstance(x, str)]

    if not all_strs:
        raise ValueError("Pas de str datas")

    minstr, maxstr, sumstr = all_strs[0], all_strs[0], len(all_strs[0])
    for st in all_strs[1:]:
        if len(st) < len(minstr):
            minstr = st
        elif len(st) > len(maxstr):
            maxstr = st
        sumstr += len(st)

    return minstr, maxstr, sumstr/len(all_strs)

def analyse_texte_v2(text: str, *args):
    all_strs = (text,) + args
    # print(all_strs)
    all_strs = [x for x in all_strs if isinstance(x, str)]
    gmin = ((x, len(x)) for x in all_strs)
    gmax = ((x, len(x)) for x in all_strs)

    return min(gmin, key=lambda x: x[1]),\
            max(gmax, key=lambda x: x[1]),\
            sum((len(x) for x in all_strs))/len(all_strs)

def analyse_texte_v3(text: str, *args):
    all_strs = (text,) + args
    all_strs = [x for x in all_strs if isinstance(x, str)]
    all_strs.sort(key=len)
    return all_strs[0],\
            all_strs[-1],\
            sum((len(x) for x in all_strs))/len(all_strs)

def analyse_text(text: str, *args):
    """
    """
    return analyse_texte_v1(text, *args)

def test_analyse_text():
    """
    """
    datas = (
             ((-47,), None, ValueError),
             ([], None, TypeError),
             (("uu",) , ("uu", "uu", 2.0), None), 
             (("ESSAIS", 1, "TESTS",2.34, True, "U", [1, 2.78, "TT"]), ("U","ESSAIS", 4.0), None ),
             )

    print(analyse_text("ESSAIS", 1,"TESTS",2.34, True, "U", [1, 2.78, "TT"]))
    for args, results, errortype in datas:
        try:
            print("Analyse -> ", (res:=analyse_text(*args)))
            assert res == results
        except Exception as e:
            print(f"error on {args}")
            assert isinstance(e, errortype)

    print("tests all done !!!")

def mesure_analyse_text(fct, datas):
    """
    """
    n = 5000
    start = time.time()
    for _ in range(n):
        fct(*datas)
    mesure = time.time() - start
    print(f"{mesure:.04f} pour {n} executions pour {fct.__name__}")

    
# test_analyse_text()
datas = ("ESSAIS", 1,"TESTS",2.34, True, "U", [1, 2.78, "TT"])*25
if len(sys.argv) == 2:
    import cProfile
    cProfile.run('mesure_analyse_text(analyse_texte_v1, datas)', 'analyse-local.cprof')
else:
    # test_analyse_text()
    mesure_analyse_text(analyse_texte_v1, datas)
    mesure_analyse_text(analyse_texte_v2, datas)
    mesure_analyse_text(analyse_texte_v3, datas)
