*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***         StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Bottom Left North          0             0             3                     NORTH         0           1           4
Bottom Left South          0             0             6                     SOUTH         0           0           7
Bottom Left East           0             0             9                     EAST          1           0           10
Bottom Left West           0             0             12                    WEST          0           0           13
Middle North               4             4             52                    NORTH         4           5           53
Middle South               4             4             55                    SOUTH         4           3           56
Middle East                4             4             58                    EAST          5           4           59
Middle West                4             4             61                    WEST          3           4           62
Top Left North             9             9             40                    NORTH         9           8           41
Top Left South             9             9             43                    SOUTH         9           9           44
Top Left East              9             9             46                    EAST          9           9           47
Top Left West              9             9             49                    WEST          8           9           50




*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}
