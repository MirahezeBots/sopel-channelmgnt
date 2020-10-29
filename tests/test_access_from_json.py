from sopel_channelmgnt.channelmgnt import get_access
from MirahezeBots_jsonparser import jsonparser as jp

DATA = jp.createdict('tests/test_config.json')


def test_simple():
    assert get_access("##test-channel", DATA, "Paladox") == True


def test_with_space():
    assert get_access("##test-channel", DATA, "Universal_Omega") == True


def test_with_number():
    assert get_access("##test-channel", DATA, "RhinosF1") == True

def test_false():
    assert get_access("##test-channel", DATA, "JohnLewis") == False
