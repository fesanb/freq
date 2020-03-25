EESchema Schematic File Version 4
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Wire Wire Line
	6650 3750 6650 3950
$Comp
L Connector:TestPoint_Probe TP1
U 1 1 5E7B92D2
P 6650 3150
F 0 "TP1" H 6802 3251 50  0000 L CNN
F 1 "CH1" H 6802 3160 50  0000 L CNN
F 2 "" H 6850 3150 50  0001 C CNN
F 3 "~" H 6850 3150 50  0001 C CNN
	1    6650 3150
	1    0    0    -1  
$EndComp
$Comp
L power:VPP #PWR01
U 1 1 5E7AE5D9
P 7050 3450
F 0 "#PWR01" H 7050 3300 50  0001 C CNN
F 1 "VPP" V 7065 3578 50  0000 L CNN
F 2 "" H 7050 3450 50  0001 C CNN
F 3 "" H 7050 3450 50  0001 C CNN
	1    7050 3450
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR03
U 1 1 5E7AC327
P 6650 3950
F 0 "#PWR03" H 6650 3700 50  0001 C CNN
F 1 "GND" H 6655 3777 50  0000 C CNN
F 2 "" H 6650 3950 50  0001 C CNN
F 3 "" H 6650 3950 50  0001 C CNN
	1    6650 3950
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5E7AB73D
P 6650 3600
F 0 "R1" H 6720 3646 50  0000 L CNN
F 1 "100" H 6720 3555 50  0000 L CNN
F 2 "" V 6580 3600 50  0001 C CNN
F 3 "~" H 6650 3600 50  0001 C CNN
	1    6650 3600
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x01_Male J?
U 1 1 5E7C9437
P 6000 3450
F 0 "J?" H 6108 3631 50  0000 C CNN
F 1 "RPI pin 16" H 6108 3540 50  0000 C CNN
F 2 "" H 6000 3450 50  0001 C CNN
F 3 "~" H 6000 3450 50  0001 C CNN
	1    6000 3450
	1    0    0    -1  
$EndComp
Text Notes 7200 3400 0    50   ~ 0
3.3v from signal generator
Wire Wire Line
	6200 3450 6650 3450
Wire Wire Line
	6650 3450 7050 3450
Connection ~ 6650 3450
Wire Wire Line
	6650 3450 6650 3150
$EndSCHEMATC
