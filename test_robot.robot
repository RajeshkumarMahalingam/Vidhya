*** Settings ***
Library			Collections
Library			OperatingSystem

*** Variables ***
${testdata}		1
${cs13}			1
${cs14}			1
#${data}
################################
${string_var}    Hello, World!
#${int_var}       42
${control_status} 	NO



*** Test Case ***
Running trial version testing
	[Tags]																						RUNRUN1
	IF    ('${cs13}' == '1') and ('${cs14}' == '1')
        Log    The control settings status is 'yes'
    ELSE
        Log    The control settings status is not 'yes'
    END
    Log 	"outside"
    
Running trial1 version testing
	[Tags]																						RUNRUN1
	test trial 	'${data}'=10


Find Variable Type
	[Tags]																						RUNRUN
	${data} 	Set Variable	'10'
	test trial	${data}
    ${type_string}=    Evaluate    type('${string_var}').__name__
    #${type_int}=       Evaluate    type(${int_var}).__name__
    ${type_int}=       Evaluate    type(${data}).__name__
    Log    Type of ${string_var}: ${type_string}
    #Log    Type of ${int_var}: ${type_int}
    Log    Type of ${data}: ${type_int}

Running control panel settings with condition one
	[Tags]																							controlstatus1
	#Accessing control panel settings
	${cs} =    Evaluate    common_reader.Capturing.cs
	${control_status}    Get From Dictionary    ${cs}    cs100
	IF    '${control_status}' == 'yes'
        Log    The control settings status is 'yes'
    ELSE
        Log    The control settings status is not 'yes'
    END

	
Running control panel settings with condition one
	[Tags]																					testruns
	IF 	'${control_status}' == 'yes'
		FOR    ${i}    IN RANGE    1    6    # Range from 1 to 5
        	Log    ${i}
    	END
    ELSE
    	Log 	"This test case no need to executed"
	END


*** Keywords ***
test trial
	[Arguments]		${data}
	Log 	${data}
	