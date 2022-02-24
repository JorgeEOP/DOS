reset
clear

set ls 1  lw 1   dt 3 lc 0              #Dotted
set ls 2  lw 3   dt 1 lc rgb "#CD2626"  #Schoene Rot   alpha
set ls 3  lw 3   dt 1 lc rgb "#0000EE"  #Schoene Blau  beta
set ls 4  lw 3   dt 1 lc rgb "#DF19B1"  #Rosa          alpha
set ls 5  lw 3   dt 1 lc rgb "#19B1DF"  #Himmelblau    beta
set ls 6  lw 3   dt 1 lc rgb "#EB5165"  #HoelleRot     alpha
set ls 7  lw 3   dt 1 lc rgb "#0413E9"  #Gesegnetblau  beta
set ls 22 lw 3   dt 1 lc rgb "#DA10F0"  #---------     alpha
set ls 33 lw 3   dt 1 lc rgb "#00FFFF"  #Gesegnetblau  beta

set ls 8  lw 2   dt 1 lc 8              #Straight
set ls 9  lw 3   dt 1 lc 9              #Straight
set ls 10 lw 3   dt 1 lc 0              #Straight black line
set ls 11 lw 0.7 dt 3 lc 0              #Dashed
set ls 111 lw 1.3 dt 4 lc 0        

set macros
#SVG = "set terminal svg size 350,262  fname \
# 'Verdana, Helvetica, Arial, sans-serif'"

#@SVG
set terminal pngcairo size 1024,768 enhanced font 'Arial, 21'

#set title "PDOS: 2Por-Y-Pc"
#set title "PDOS: Por-Y-Pc"
#set title "PDOS: YPc 3 membered"
#set title "PDOS: YPc Gas"

set style textbox opaque noborder

## 1 mem
#F2P   = "/Users/jorge_jaeger/Desktop/Physik/KIT/PhD/Nithin/Crystal/1m/SinPoint/\
#CP2K/run_mul_2/1-membered-T-PDOS.dat"
## 2 mem
#F2P   = "/Users/jorge_jaeger/Desktop/Physik/KIT/PhD/Nithin/Crystal/2m/SinPoint/\
#CP2K/run_mul_3/2-membered-T-PDOS.dat"
## 3 mem
#F2P   = "/Users/jorge_jaeger/Desktop/Physik/KIT/PhD/Nithin/Crystal/3m/SinPoint/\
#CP2K/run_mul_2/gas/3-membered_gas-T-PDOS.dat"
## 4 mem
#F2P   = "/Users/jorge_jaeger/Desktop/Physik/KIT/PhD/Nithin/Crystal/4m/SinPoint/\
#CP2K/run_mul_1/4-membered-T-PDOS.dat"
## 5 mem
F2P   = "/Users/jorge_jaeger/Desktop/Physik/KIT/PhD/Nithin/Crystal/5m/SinPoint/\
CP2K/run_mul_2/Gas/5-membered_gas-T-PDOS.dat"
## Gas
#F2P   = "/Users/jorge_jaeger/Desktop/Physik/KIT/PhD/Nithin/Crystal/Gas/\
#Gas_YPc-T-PDOS.dat"
## 2PorYPc
#F2P   = "/Users/jorge_jaeger/Desktop/Physik/KIT/PhD/Nithin/PorYPc/SinPoint/UP/CP2K/\
#PorYPc-T-PDOS.dat"

#set grid ls 11
#set grid xtics
#set grid mytics
#set xrange [-5:-2]
set xrange [-5.5:-2.9]
set yrange [-50:50]
set format x "%2.1f"
set format y "%2.0f"
#set xtics  -6,1,0
set xtics nomirror
set ytics nomirror
set mxtics 5 
set mytics 2
set xlabel 'Energy (eV)'
set ylabel 'PDOS'
set xzeroaxis ls 10

set key top right opaque font ", 14" box ls 9 width  0.0 height 0.6 \
                                     maxcols 2 spacing 1.1 samplen 1

set style textbox opaque noborder

#set label '{/Symbol a} ' at -0.5,19 boxed
#set label '{/Symbol b} ' at -0.5,-19 boxed

## 1 mem
#set output '/Users/jorge_jaeger/Desktop/Physik/KIT/PhD/Nithin/Crystal/1m/\
#SinPoint/CP2K/run_mul_2/PDOS-1m-YPc.png'
## 2 mem
#set output '/Users/jorge_jaeger/Desktop/Physik/KIT/PhD/Nithin/Crystal/2m/\
#SinPoint/CP2K/run_mul_3/PDOS-2m-YPc.png'
## 3 mem
#set output '/Users/jorge_jaeger/Desktop/Physik/KIT/PhD/Nithin/Crystal/3m/\
#SinPoint/CP2K/run_mul_2/gas/PDOS-3m-YPc.png'
## 4 mem
#set output '/Users/jorge_jaeger/Desktop/Physik/KIT/PhD/Nithin/Crystal/4m/\
#SinPoint/CP2K/run_mul_1/PDOS-4m-YPc.png'
## 5 mem
set output '/Users/jorge_jaeger/Desktop/Physik/KIT/PhD/Nithin/Crystal/5m/\
SinPoint/CP2K/run_mul_2/gas/PDOS-5m-YPc.png'
## Gas
#set output '/Users/jorge_jaeger/Desktop/Physik/KIT/PhD/Nithin/Crystal/Gas\
#/PDOS-Gas-YPc.png'
## Gas
#set output '/Users/jorge_jaeger/Desktop/Physik/KIT/PhD/Nithin/PorYPc/SinPoint/\
#UP/CP2K/PDOS-PorYPc.png'

## 1 mem
#fenA = -2.4801817993905764 
#fenB = -3.040056071401779
## 2 mem
#fenA = -2.4286978566131667
#fenB = -3.0367362822797688 
#fenA = -2.3656762860674587 
#fenB = -2.3656762860674587
## 3 mem
#fenA = -2.4378136710055727
#fenB = -3.036409745644817 
#fenA = -2.3638531231889774 
#fenB = -2.366383782109854 
#fenA = -2.4368340611007175
#fenB = -2.446684582921765
# Gas
#fenA = -3.818356140809528 
#fenB = -4.419237971893435 
#fenA = -3.791770616447198 
#fenB = -3.7545182286764396 
## 4 mem
#fenA = -2.428371319978215
#fenB = -3.0367090708935227
#fenA = -2.3557713414739188
#fenB = -2.3496215681823256 
#fenA = -2.3803976460265384
#fenB = -2.3683974246920574 
## 5 mem
#fenA = -2.4977331435192385
#fenB = -3.116030261800578
#fenA = -2.39490131489565
#fenB = -2.378030255423137
#fenA = -2.3768329544283135 
#fenB = -2.3452677463829676 
# Gas
#fenA = -3.473342974596646 
#fenB = -4.089599238909536
#fenA = -3.4757103652000474 
#fenB = -3.4418594007100376 
fenA = -3.4789485201633195 
fenB = -3.433478293746274 
## Gas
#fenA = -4.310446849681974
#fenB = -4.931029724407978
## Gas
#fenA = -4.100837541429129
#fenB = -4.236105342457936 

set arrow from fenA, graph 1 to fenA, graph 0.5 nohead ls 111
set arrow from fenB, graph 0 to fenB, graph 0.5 nohead ls 111

p F2P u 1:2      w l ls 2 title 'Total DOS {/Symbol a}',\
  F2P u 1:2      w filledcurves above y2=0 ls 2 fs transparent solid 0.2 notitle ,\
  F2P u 1:(-$3)  w l ls 3 title 'Total DOS {/Symbol b}',\
  F2P u 1:(-$3)  w filledcurves below y2=0 ls 3 fs transparent solid 0.2 notitle,\
  F2P u 1:9      w l ls 22  title 'C',\
  F2P u 1:9      w filledcurves above y2=0 ls 22 fs transparent solid 0.2 notitle,\
  F2P u 1:(-$10) w l ls 33  title 'C',\
  F2P u 1:(-$10) w filledcurves below y2=0 ls 33 fs transparent solid 0.2 notitle,\

#  F2P u 1:5     w l ls 6  title 'Y',\
#  F2P u 1:(-$6) w l ls 7  title 'Y',\
#  F2P u 1:7     w l ls 22 title 'N',\
#  F2P u 1:(-$8) w l ls 33 title 'N',\
#  F2P u 1:9      w l ls 22  title 'C',\
#  F2P u 1:(-$10) w l ls 33  title 'C',\

#p F2P u 1:8      w l ls 2  title 'C',\
#  F2P u 1:(-$13) w l ls 3  title 'C',\
#  F2P u 1:6      w l ls 4  title 'N',\
#  F2P u 1:(-$11) w l ls 5  title 'N',\
