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

set title "PDOS: 2Por-Y-Pc"

set style textbox opaque noborder

#F2P   = "2PorYPc/LS/1te_GEO/CP2K/2-PorYPc-1teGEO_T-PDOS.dat"
#F2P   = "2PorYPc/LS/1te_GEO/CP2K/2te_runde/UKS/WFN_SWAP/2-PorYPc-1teGEO_T-PDOS.dat"
F2P   = "2PorYPc/LS/2te_GEO/CP2K/2te_runde/UKS/WFN_FLIP/2-PorYPc-2teGEO_T-PDOS.dat"
#F2P_1 = "2PorYPc/LS/2te_GEO/Turbomole/dos_alpha"
#F2P_2 = "2PorYPc/LS/2te_GEO/Turbomole/dos_beta"

set grid ls 11
set grid xtics
set grid mytics
set xrange [-6:-3]
set yrange [-50:50]
#set yrange [-2000:2000]
set format x "%2.1f"
set format y "%2.0f"
#set xtics  -6,1,0
set mxtics 5
set mytics 2
set xlabel 'Energy [eV]'
set ylabel 'PDOS'
set xzeroaxis ls 10

set key bottom right opaque font ", 14" box ls 9 width  1 height 0.6 \
                                   maxcols 2 spacing 1.1 samplen 2

set style textbox opaque noborder

#set label '{/Symbol a} ' at -0.5,19 boxed
#set label '{/Symbol b} ' at -0.5,-19 boxed

#set output '2PorYPc/LS/1te_GEO/CP2K/PDOS_2Por-Y-Pc.png'
#set output '2PorYPc/LS/1te_GEO/CP2K/2te_runde/UKS/WFN_SWAP/PDOS_2Por-Y-Pc.png'
set output '2PorYPc/LS/2te_GEO/CP2K/2te_runde/UKS/WFN_FLIP/PDOS_2Por-Y-Pc.png'
fenA = -4.053326461043635
fenB = -4.053326461043635 
set arrow from fenA, graph 1 to fenA, graph 0.5 nohead ls 111
set arrow from fenB, graph 0 to fenB, graph 0.5 nohead ls 111

p F2P u 1:2     w l ls 2 title 'Total DOS {/Symbol a}',\
  F2P u 1:(-$3) w l ls 3 title 'Total DOS {/Symbol b}'

#set output '2PorYPc/HS/2te_GEO/Turbomole/PDOS_2Por-Y-Pc_Turbo.png'
#fen  = (fenA + fenB)/2

#p F2P_1 u ($1*27.211386245988):2     w l ls 2 title 'Total DOS {/Symbol a}',\
#  F2P_2 u ($1*27.211386245988):(-$2) w l ls 3 title 'Total DOS {/Symbol b}'

#p F2P u 1:8      w l ls 2  title 'C',\
#  F2P u 1:(-$13) w l ls 3  title 'C',\
#  F2P u 1:6      w l ls 4  title 'N',\
#  F2P u 1:(-$11) w l ls 5  title 'N',\
#  F2P u 1:5      w l ls 6  title 'Y',\
#  F2P u 1:(-$10) w l ls 7  title 'Y',\
#  F2P u 1:7      w l ls 22 title 'O',\
#  F2P u 1:(-$12) w l ls 33 title 'O',\
