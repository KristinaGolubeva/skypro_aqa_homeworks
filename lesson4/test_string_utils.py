import pytest
from string_utils import StringUtils

SU = StringUtils

#2
@pytest.mark.parametrize('string, result', [("homework","Homework"), ("домашка","Домашка")])
def test_capitilize_positive_str(string,result):
    SU = StringUtils()
    res = SU.capitilize(string)
    assert res == result

#2
@pytest.mark.parametrize('string, result', [(" homework","Homework"), ("1домашка","1Домашка")])
def test_capitilize_negative_str(string,result):
    SU = StringUtils()
    res = SU.capitilize(string)
    assert res == result

#6
@pytest.mark.parametrize('string, result', [(" homework","homework"), (" домашка","домашка"), (" Домашка","Домашка"), ("  homework","homework"), ("домашка","домашка"), ("  ","")])
def test_whitespace_positive_str(string,result):
    SU = StringUtils()
    res = SU.trim(string)
    assert res == result

#1
@pytest.mark.parametrize('string, result', [("_homework","homework")])
def test_whitespace_negative_str(string,result):
    SU = StringUtils()
    res = SU.trim(string)
    assert res == result

#2
@pytest.mark.parametrize('string, delim, result', [("В рецепт добавить: соль, сахар, яйца, муку, дрожжи", ",", ["В рецепт добавить: соль", " сахар", " яйца", " муку", " дрожжи"]), ("В рецепт добавить: соль, сахар, яйца, муку, дрожжи", ":", ["В рецепт добавить", " соль, сахар, яйца, муку, дрожжи"])]) 
def test_delimeter_positive_str(string,delim,result):
    SU = StringUtils()
    res = SU.to_list(string,delim)
    assert res == result

#3
@pytest.mark.parametrize('string, delim, result', [("В рецепт добавить: соль, сахар, яйца, муку, дрожжи", ":", ["В рецепт добавить: соль", " сахар", " яйца", " муку", " дрожжи"]), ("В рецепт добавить: соль, сахар, яйца, муку, дрожжи", ",", ["В рецепт добавить", " соль, сахар, яйца, муку, дрожжи"]), ("Как здорово. Что все мы здесь. Сегодня. Собрались", "", ["Как здорово", "Что все мы здесь", "Сегодня", "Собрались"])]) 
def test_delimeter_negative_str(string,delim,result):
    SU = StringUtils()
    res = SU.to_list(string,delim)
    assert res == result

#5
@pytest.mark.parametrize('string, symbol, result', [("Homework","w",True), ("Домашка","Д",True), ("Домашка","а",True), ("Домашка","f",False), ("Домашка","д",False)])
def test_contains_positive_str(string,symbol,result):
    SU = StringUtils()
    res = SU.contains(string,symbol)
    assert res == result

#5
@pytest.mark.parametrize('string, symbol, result', [("Homework","S",True), ("Домашка","F",True), ("Домашка","д",True), ("Домашка","Д",False), ("Homework","m",False)])
def test_contains_negative_str(string,symbol,result):
    SU = StringUtils()
    res = SU.contains(string,symbol)
    assert res == result

#4
@pytest.mark.parametrize('string, symbol, result', [("Homework","w","Homeork"), ("Домашка","Д","омашка"), ("Домашка","а","Домшк"),("Homework","a","Homework")])
def test_deleteSymbol_positive_str(string,symbol,result):
    SU = StringUtils()
    res = SU.delete_symbol(string,symbol)
    assert res == result

#2
@pytest.mark.parametrize('string, symbol, result', [("Домашка","д","омашка"), ("Домашка","а","Домашк")])
def test_deleteSymbol_negative_str(string,symbol,result):
    SU = StringUtils()
    res = SU.delete_symbol(string,symbol)
    assert res == result

#5
@pytest.mark.parametrize('string, symbol, result', [("Homework","H",True), ("Домашка","Д",True), ("домашка","д",True), ("Homework","h",False), ("Homework","o",False)])
def test_startswith_positive_str(string,symbol,result):
    SU = StringUtils()
    res = SU.starts_with(string,symbol)
    assert res == result

#4
@pytest.mark.parametrize('string, symbol, result', [("Homework","h",True), ("Домашка","о",True), ("домашка","Д",True), ("Homework","H",False)])
def test_startswith_negative_str(string,symbol,result):
    SU = StringUtils()
    res = SU.starts_with(string,symbol)
    assert res == result

#5
@pytest.mark.parametrize('string, symbol, result', [("Homework","k",True), ("Домашка","а",True), ("домашкА","А",True), ("домашкА","а",False), ("Homework","б",False)])
def test_endwith_positive_str(string,symbol,result):
    SU = StringUtils()
    res = SU.end_with(string,symbol)
    assert res == result

#5
@pytest.mark.parametrize('string, symbol, result', [("Homework","K",True), ("Домашка","А",True), ("домашкА","ш",True), ("домашкА","А",False), ("домашка","а",False)])
def test_endwith_negative_str(string,symbol,result):
    SU = StringUtils()
    res = SU.end_with(string,symbol)
    assert res == result

#4
@pytest.mark.parametrize('string, result', [("",True), (" ",True), ("            ",True), ("Homework",False)])
def test_isempty_positive_str(string,result):
    SU = StringUtils()
    res = SU.is_empty(string)
    assert res == result

#4
@pytest.mark.parametrize('string, result', [("__",True), ("fgfaj",True), ("           g",True), ("",False)])
def test_isempty_negative_str(string,result):
    SU = StringUtils()
    res = SU.is_empty(string)
    assert res == result

#3
@pytest.mark.parametrize('lst, joiner, result', [(["Как", "здорово", "что", "все", "мы", "здесь", "сегодня", "собрались"],", ","Как, здорово, что, все, мы, здесь, сегодня, собрались"), (["Сострадание", "это то, что делает нас людьми"]," - ","Сострадание - это то, что делает нас людьми"), (["Я пришел к тебе с приветом", "Рассказать, что солнце встало."],". ","Я пришел к тебе с приветом. Рассказать, что солнце встало.")])
def test_listtostring_positive_str(lst,joiner,result):
    SU = StringUtils()
    res = SU.list_to_string(lst,joiner)
    assert res == result

#3
@pytest.mark.parametrize('lst, joiner, result', [(["Как", "здорово", "что", "все", "мы", "здесь", "сегодня", "собрались"],"","Как, здорово, что, все, мы, здесь, сегодня, собрались"), (["Сострадание", "это то, что делает нас людьми"]," -","Сострадание - это то, что делает нас людьми"), (["Я пришел к тебе с приветом", "Рассказать, что солнце встало."],",","Я пришел к тебе с приветом. Рассказать, что солнце встало.")])
def test_listtostring_negative_str(lst,joiner,result):
    SU = StringUtils()
    res = SU.list_to_string(lst,joiner)
    assert res == result


#29 negative 
#36 positive