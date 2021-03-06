from app.logic.teams import (getExtTeamName, getNiceTeamName,
                             getShortNiceTeamName)


def test_getExtTeamName():
    assert getExtTeamName("all") == "allteams"
    assert getExtTeamName("all units") == "allteams"
    assert getExtTeamName("all teams") == "allteams"
    assert getExtTeamName("All Teams") == "allteams"
    assert getExtTeamName("ALL TEAMS") == "allteams"
    assert getExtTeamName("team a") == "teamalpha"
    assert getExtTeamName("team bravo") == "teambravo"
    assert getExtTeamName("team 1") == "team00001"
    assert getExtTeamName("team 11") == "team00011"
    assert getExtTeamName("team 101") == "team00101"
    assert getExtTeamName("team 100") == "team00100"
    assert getExtTeamName("t c") == "teamcharlie"
    assert getExtTeamName("t 1") == "team00001"
    assert getExtTeamName("t 101") == "team00101"
    assert getExtTeamName("t1") == "team00001"
    assert getExtTeamName("trans a") == "z_transalpha"
    assert getExtTeamName("trans bravo") == "z_transbravo"
    assert getExtTeamName("trans 1") == "z_trans00001"
    assert getExtTeamName("trans 11") == "z_trans00011"
    assert getExtTeamName("trans 101") == "z_trans00101"
    assert getExtTeamName("trans 100") == "z_trans00100"
    assert getExtTeamName("a") == "teamalpha"
    assert getExtTeamName("bravo") == "teambravo"
    assert getExtTeamName("1") == "team00001"
    assert getExtTeamName("11") == "team00011"
    assert getExtTeamName("101") == "team00101"
    assert getExtTeamName("100") == "team00100"
    assert getExtTeamName(" Team3") == "team00003"
    assert getExtTeamName(" Team400") == "team00400"
    assert getExtTeamName("5") == "team00005"
    assert getExtTeamName("Bravo") == "teambravo"
    assert getExtTeamName("B") == "teambravo"
    assert getExtTeamName("t b") == "teambravo"
    assert getExtTeamName("x") == "teamxray"
    assert getExtTeamName("x1") == "teamxray1"
    assert getExtTeamName("Team 01") == "team00001"
    assert getExtTeamName("Team 101") == "team00101"
    assert getExtTeamName("Team 102") == "team00102"
    assert getExtTeamName("Team 2") == "team00002"
    assert getExtTeamName("Team Charlie") == "teamcharlie"
    assert getExtTeamName("Team02") == "team00002"
    assert getExtTeamName("Team1") == "team00001"
    assert getExtTeamName("TeamAlpha") == "teamalpha"
    assert getExtTeamName("Transport Bravo") == "z_transportbravo"
    assert getExtTeamName("transportbravo") == "z_transportbravo"
    assert getExtTeamName("transport bravo2") == "z_transportbravo2"
    assert getExtTeamName("Transport1a") == "z_transport00001a"
    assert getExtTeamName("Transport1driver") == "z_transport00001driver"


def test_getNiceTeamName():
    assert getNiceTeamName("ALL TEAMS") == "ALL TEAMS"
    assert getNiceTeamName(" Team3") == "Team 3"
    assert getNiceTeamName(" Team400") == "Team 400"
    assert getNiceTeamName("5") == "Team 5"
    assert getNiceTeamName("Bravo") == "Team Bravo"
    assert getNiceTeamName("B") == "Team Bravo"
    assert getNiceTeamName("t b") == "Team Bravo"
    assert getNiceTeamName("t 1") == "Team 1"
    assert getNiceTeamName("t1") == "Team 1"
    assert getNiceTeamName("x") == "Team Xray"
    assert getNiceTeamName("x1") == "Team Xray 1"
    assert getNiceTeamName("Team 01") == "Team 1"
    assert getNiceTeamName("Team 101") == "Team 101"
    assert getNiceTeamName("Team 102") == "Team 102"
    assert getNiceTeamName("Team 2") == "Team 2"
    assert getNiceTeamName("Team Charlie") == "Team Charlie"
    assert getNiceTeamName("Team02") == "Team 2"
    assert getNiceTeamName("Team1") == "Team 1"
    assert getNiceTeamName("TeamAlpha") == "Team Alpha"
    assert getNiceTeamName("Transport Bravo") == "Transport Bravo"
    assert getNiceTeamName("transportbravo") == "Transport Bravo"
    assert getNiceTeamName("transport bravo2") == "Transport Bravo 2"
    assert getNiceTeamName("Transport1a") == "Transport 1 A"
    assert getNiceTeamName("Transport1driver") == "Transport 1 Driver"


def test_getShortNiceTeamName():
    assert getShortNiceTeamName("ALL TEAMS") == "ALL"
    assert getShortNiceTeamName(" Team3") == "3"
    assert getShortNiceTeamName(" Team400") == "400"
    assert getShortNiceTeamName("5") == "5"
    assert getShortNiceTeamName("Bravo") == "B"
    assert getShortNiceTeamName("B") == "B"
    assert getShortNiceTeamName("t b") == "B"
    assert getShortNiceTeamName("t 1") == "1"
    assert getShortNiceTeamName("t1") == "1"
    assert getShortNiceTeamName("x") == "X"
    assert getShortNiceTeamName("x1") == "X1"
    assert getShortNiceTeamName("Team 01") == "1"
    assert getShortNiceTeamName("Team 101") == "101"
    assert getShortNiceTeamName("Team 102") == "102"
    assert getShortNiceTeamName("Team 2") == "2"
    assert getShortNiceTeamName("Team Charlie") == "C"
    assert getShortNiceTeamName("Team02") == "2"
    assert getShortNiceTeamName("Team1") == "1"
    assert getShortNiceTeamName("TeamAlpha") == "A"
    assert getShortNiceTeamName("Transport Bravo") == "TransportB"
    assert getShortNiceTeamName("transportbravo") == "TransportB"
    assert getShortNiceTeamName("transport bravo2") == "TransportB2"
    assert getShortNiceTeamName("Transport1a") == "Transport1A"
    assert getShortNiceTeamName("Transport1driver") == "Transport1Driver"
