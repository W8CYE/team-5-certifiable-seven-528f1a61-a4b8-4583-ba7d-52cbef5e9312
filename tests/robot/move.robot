*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***         StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Valid Case #1              0             0             1                     NORTH         0           1           2
Invalid Case #2            0             0             5                     SOUTH         0           0           6
Middle North               4             4             52                    NORTH         4           5           53
Middle South               4             4             55                    SOUTH         4           3           56
Middle East                4             4             58                    EAST          5           4           59
Middle West                4             4             61                    WEST          3           4           62



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
