reset
clear

set ls 1  lw 1   dt 3 lc 0              #Dotted
set ls 2  lw 3.0 dt 1 lc rgb "#CD2626"  #Schoene Rot
set ls 3  lw 4.0 dt 1 lc rgb "#0000EE"  #Schoene Blau
set ls 4  lw 1.5 dt 4 lc 4              #Dashed-dotted
set ls 5  lw 1   dt 2 lc 5              #Dashed
set ls 6  lw 1   dt 3 lc 6              #Dotted 
set ls 7  lw 1   dt 4 lc 7              #Dashed
set ls 8  lw 2   dt 1 lc 8              #Straight
set ls 9  lw 3   dt 1 lc 9              #Straight
set ls 10 lw 3   dt 1 lc 0              #Straight black line
set ls 11 lw 0.7 dt 3 lc 0              #Dashed

set macros
#SVG = "set terminal svg size 350,262  fname \
# 'Verdana, Helvetica, Arial, sans-serif'"

#@SVG
set terminal pngcairo size 1024,768 enhanced font 'Arial, 21'

set output '2PorYPc/HS/2te_GEO/CP2K/PDOS_2Por-Y-Pc.png'

set title "PDOS: 2Por-Y-Pc"

set style textbox opaque noborder

F2P = "2PorYPc/HS/2te_GEO/CP2K/2-PorYPc-2teGEO_T-PDOS.dat"

set grid ls 11
set grid xtics
set grid mytics
set xrange [-6:-3]
set yrange [-50:50]
set format x "%2.1f"
set format y "%2.0f"
#set xtics  -6,1,0
set mxtics 5
set mytics 2
set xlabel 'Energy [eV]'
set ylabel 'PDOS'
set xzeroaxis ls 10

set key bottom right box opaque font ",21"
set style textbox opaque noborder

set label '{/Symbol a} ' at -0.5,19 boxed
set label '{/Symbol b} ' at -0.5,-19 boxed

fenergyA_001 = -4.063993324452062
fenergyB_001 = -4.13542321334778

set arrow from fenergyA_001, graph 1 to fenergyA_001, graph 0.5 nohead ls 7
set arrow from fenergyB_001, graph 0 to fenergyB_001, graph 0.5 nohead ls 7

p F2P u 1:2     w l ls 2 title 'Total DOS {/Symbol a}',\
  F2P u 1:(-$3) w l ls 3 title 'Total DOS {/Symbol b}',\


##-------------------------------------------------------------------------------#
##reset
#clear
#
#set terminal pngcairo size 1024,768 enhanced font 'Arial, 21'
#
#set output 'PDOS9periods-TbPc2_CNT13_0-AF-TZVP-Elevels.png'
##set output 'PDOS9periods-TbPc2_CNT13_0-FE-TZVP-Elevels.png'
#
#set title "Energy levels: (13,0)-CNT+TbPc_2 (AF)" 
##set title "PDOS: 9 periods (13,0)-CNT+TbPc_2 (FE)"
#
#set style textbox opaque noborder
#
#set grid ls 11
#set grid xtics
#set grid mytics
#set xrange [*:1]
#set yrange [-4.0:-2.5]
#set format x "%2.0f"
#set format y "%2.1f"
#set xtics  -1,100,100
#set ytics -4.0,0.2,-2.5
##set mxtics 5
#set mytics 3
#set xlabel ' '
#set ylabel 'Energy [eV]'
#set xzeroaxis ls 10
#
#set key at 0.4,-2.65 box opaque font ",16"
#
#set multiplot layout 1, 2;
#set tmargin 2
#set bmargin 3
#set lmargin 9
#set rmargin 6
#
#set style arrow 1 nohead lc 7 lw 3
#set style arrow 2 nohead lc 3 lw 3
#
#p   'TbPc-13_0_CNT-AF-ALPHA_k1-1.pdos' using (0):($2*27.211384523):(1):(0) with vectors arrowstyle 1 title '{/Symbol a}',\
#    'TbPc-13_0_CNT-AF-BETA_k1-1.pdos' using (0):($2*27.211384523):(1):(0) with vectors arrowstyle 2 title '{/Symbol b}'
#
##p   'TbPc-13_0_CNT-FE-ALPHA_k1-1.pdos' using (0):($2*27.211384523):(1):(0) with vectors arrowstyle 1 title '{/Symbol a}',\
##    'TbPc-13_0_CNT-FE-BETA_k1-1.pdos' using (0):($2*27.211384523):(1):(0) with vectors arrowstyle 2 title '{/Symbol b}'
#
#
#set ls 3  lw 1.5 dt 1 lc 0   #Straight black
#set ls 8  lw 2   dt 2 lc 0   #Straight
#set ls 10 lw 3   dt 1 lc 0   #Straight black line
#
#set notitle
#
#set style textbox opaque noborder
#
#set grid ls 11
#set grid ytics
#set xrange [-5:5]
#set yrange [-4.0:-2.5]
#set format x "%2.0f"
#set format y2 "%2.1f"
#set xtics  -5,1,5
#set ytics -4.0,0.2,-2.5
#set y2tics -4.0,0.2,-2.5
##unset ytics
#unset mxtics
#set xlabel 'PDOS'
#set ylabel 'Energy [eV]'
#set xzeroaxis ls 10
#set yzeroaxis ls 10
#set key
#
#set key at 4.5,-2.65  box opaque font ",16"
#
#set label '{/Symbol a} ' at 3,-2.7 boxed
#set label '{/Symbol b} ' at -3,-2.7 boxed
#
#unset arrow
#
#p   'TbPc-13_0_CNT-AF_T-PDOS.dat' u 7:1       w l ls 3 title    '4f-Tb',\
#    'TbPc-13_0_CNT-AF_T-PDOS.dat' u (-$11):1  w l ls 3 notitle  ' ',\
#    'TbPc-13_0_CNT-AF_T-PDOS.dat' u 13:1      w l ls 8 title    'Ligands',\
#    'TbPc-13_0_CNT-AF_T-PDOS.dat' u (-$14):1  w l ls 8 notitle  ' ',\
#
##p   'TbPc-13_0_CNT-FE_T-PDOS.dat' u 7:1       w l ls 3 title    '4f-Tb',\
##    'TbPc-13_0_CNT-FE_T-PDOS.dat' u (-$11):1  w l ls 3 notitle  ' ',\
##    'TbPc-13_0_CNT-FE_T-PDOS.dat' u 13:1      w l ls 8 title    'Ligands',\
##    'TbPc-13_0_CNT-FE_T-PDOS.dat' u (-$14):1  w l ls 8 notitle  ' ',\
#
#unset multiplot
#
##-------------------------------------------------------------------------------#
#reset
#clear
#
#set ls  1 lw 3 dt 1 lc 1  
#set ls  2 lw 3 dt 1 lc 3  
#set ls 10 lw 3 dt 1 lc 0  
#set grid mytics
#set xrange [-1:1]
#set yrange [-5:-3]
#set yzeroaxis ls 10
##set key bottom right box opaque font ",16"
#
#set terminal pngcairo size 1024,768 enhanced font 'Arial, 23'
##set output 'E_levels_MOS.png'
#set format x "%2.0f"
#set format y "%2.1f"
#set xtics -100,100,100
#set ytics -5,0.5,-3
#show mytics
#set style textbox opaque
#set key width 2
#set key at -1.7,-3.2 box opaque font ",16"
#set label '{/Symbol a} ' at -0.7,-3.05 boxed
#set label '{/Symbol b} ' at  0.3,-3.05 boxed
#unset xtics
#
##set xlabel ' '
#set ylabel 'Energy (eV)' offset 1.5,0
#
##LUMO_0-AF = *27.211384523
##LUMO_1-AF = *27.211384523
##LUMO_2-AF = *27.211384523
##LUMO_3-AF = *27.211384523
##LUMO_4-AF = *27.211384523
#
##LUMO_0-FE = *27.211384523
##LUMO_1-FE = *27.211384523
##LUMO_2-FE = *27.211384523
##LUMO_3-FE = *27.211384523
##LUMO_4-FE = *27.211384523
#
#set macros
#set arrow from 0,LUMO_1-AF, graph 0 to  1,LUMO_1-AF, graph 1 nohead ls 2
#set arrow from 0,LUMO_2-AF, graph 0 to  1,LUMO_2-AF, graph 1 nohead ls 2
#set arrow from 0,LUMO_3-AF, graph 0 to -1,LUMO_3-AF, graph 1 nohead ls 2
#set arrow from 0,LUMO_4-AF, graph 0 to  1,LUMO_4-AF, graph 1 nohead ls 2
##set arrow from 0,LUMO_1-FE, graph 0 to  1,LUMO_1-FE, graph 1 nohead ls 2
##set arrow from 0,LUMO_2-FE, graph 0 to  1,LUMO_2-FE, graph 1 nohead ls 2
##set arrow from 0,LUMO_3-FE, graph 0 to -1,LUMO_3-FE, graph 1 nohead ls 2
##set arrow from 0,LUMO_4-FE, graph 0 to  1,LUMO_4-FE, graph 1 nohead ls 2
#
#LMARGIN = "set lmargin at screen 0.45; set rmargin at screen 0.65"
#@LMARGIN
#set style arrow 1 nohead lc 7 lw 3
#set style arrow 2 nohead lc 3 lw 3
##set arrow from 0,LUMO_0, graph 0 to -1,LUMO_0, graph 1 nohead arrowstyle 1
#p   'TbPc-13_0_CNT-AF-ALPHA_k1-1.pdos' using (0):($2*27.211384523):(-1):(0) with vectors arrowstyle 1 title 'HOMOs',\
#    'TbPc-13_0_CNT-AF-BETA_k1-1.pdos' using (0):($2*27.211384523):(1):(0) with vectors arrowstyle 1 notitle 'HOMOs {/Symbol b}',\
#
##p   'TbPc-13_0_CNT-FE-ALPHA_k1-1.pdos' using (0):($2*27.211384523):(-1):(0) with vectors arrowstyle 1 title 'HOMOs',\
##    'TbPc-13_0_CNT-FE-BETA_k1-1.pdos' using (0):($2*27.211384523):(1):(0) with vectors arrowstyle 1 notitle 'HOMOs {/Symbol b}',\
