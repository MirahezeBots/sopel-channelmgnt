from sopel_channelmgnt.channelmgnt import get_access
from MirahezeBots_jsonparser import jsonparser as jp

DATA = jp.createdict('tests/test_config.json')
TEST_DATA_CHANNEL = "##test-channel"


def test_simple():
    assert get_access(TEST_DATA_CHANNEL, DATA, "Paladox")


def test_with_space():
    assert get_access(TEST_DATA_CHANNEL, DATA, "Universal_Omega")


def test_with_number():
    assert get_access(TEST_DATA_CHANNEL, DATA, "RhinosF1")


def test_false():
    assert not get_access(TEST_DATA_CHANNEL, DATA, "JohnLewis")
