reset
clear

set ls 1 lw 1 dt 3 lc 0  #Dotted
set ls 2 lw 1 dt 3 lc 2  #Dotted
set ls 3 lw 1.5 dt 1 lc 3  #Straight black
set ls 4 lw 1.5 dt 4 lc 4  #Dashed-dotted
set ls 5 lw 1 dt 2 lc 5  #Dashed
set ls 6 lw 1 dt 3 lc 6  #Dotted 
set ls 7 lw 1 dt 4 lc 7  #Dashed
set ls 8 lw 2 dt 1 lc 8  #Straight
set ls 9 lw 3 dt 1 lc 9  #Straight
set ls 10 lw 3 dt 1 lc 0 #Straight black line

set style textbox opaque noborder

set grid xtics
set grid mytics
set xzeroaxis ls 10
#set logscale y
set xrange [-12:0]
set yrange [-20:20]
set key bottom right box opaque font ",16"
#set key top right box opaque font ",17"

set terminal pngcairo size 1024,768 enhanced font 'Arial, 25'
set output 'PDOS.png'
#set terminal postscript eps size 3.5,2.52 color enhanced font 'Helvetica, 20'
#set xtics ("{/Symbol G}" 0, "X" 0.114260, "S" 0.265135, "Y" 0.379394, "{/Symbol G}" 0.530269)
set format x "%2.1f"
set format y "%2.2f"
#set xtics  -6,1,0
set mxtics 2
#set mytics 5

set label '{/Symbol a} ' at -0.5,19 boxed
set label '{/Symbol b} ' at -0.5,-2 boxed
#set xlabel 'x'
#set ylabel '{/Symbol Y}'
set xlabel 'Energy (eV)'
set ylabel 'PDOS'

#####  run006  #####
fenergyA_001 =  -4.701474172345848
fenergyB_001 =  -3.468009323302781         

#set label 'E_{diff} = 0.138429 eV' at -4.2,16.0 font "Arial, 19" boxed
set arrow from fenergyA_001, graph 1 to fenergyA_001, graph 0.5 nohead ls 7
set arrow from fenergyB_001, graph 0 to fenergyB_001, graph 0.5 nohead ls 7

p   'T_PDOS.dat' u 1:7       w l ls 3 title    '4f-Tb',\
    'T_PDOS.dat' u 1:(-$11)  w l ls 3 notitle  ' ',\
    'T_PDOS.dat' u 1:2       w l ls 8 title    'Total',\
    'T_PDOS.dat' u 1:(-$3)   w l ls 8 notitle  ' ',\
    'T_PDOS.dat' u 1:13      w l ls 9 title    'Ligands',\
    'T_PDOS.dat' u 1:(-$14)  w l ls 9 notitle  ' ',\
#    'T_PDOS.dat' u 1:15      w l ls 4 title    'Tb',\
#    'T_PDOS.dat' u 1:(-$16)  w l ls 4 notitle  ' ',\
#
#p  'T_PDOS.dat' u 1:13      w l ls 4 title    'Ligands',\
#   'T_PDOS.dat' u 1:(-$14)  w l ls 4 notitle  ' ',\
#   'T_PDOS.dat' u 1:7       w l ls 3 title    '4f-Tb',\
#   'T_PDOS.dat' u 1:(-$11)  w l ls 3 notitle  ' ',\
#   'T_PDOS.dat' u 1:(-$10)  w l ls 2 notitle  '{/Symbol b} C',\
#   'T_PDOS.dat' u 1:(-$11)  w l ls 3 notitle  '{/Symbol b} 4f-Tb',\
#   'T_PDOS.dat' u 1:(-$12)  w l ls 4 notitle  '{/Symbol b} H',\
p   'T_PDOS.dat' u 1:($13-$14)    w l ls 3 title  'Ligands: PDOS({/Symbol a})-PDOS({/Symbol b})',\


#-------------------------------------------------------------------------------#
reset
clear

set grid mytics
set xrange [*:1]
set yrange [-5:-2.5]
#set key bottom right box opaque font ",16"
#set key top right box opaque font ",17"

set terminal pngcairo size 1024,768 enhanced font 'Arial, 23'
set output 'E_levels.png'
set format x "%2.0f"
set format y "%2.1f"
set xtics -1,100,100
set ytics -5,0.5,-2.5
show mytics
set multiplot layout 1, 2;
set style textbox opaque noborder
set key at 0.4,-2.7 box opaque font ",16"

set xlabel ' '
set ylabel 'Energy (eV)'

set macros
#set arrow from 0,HOMO_alpha, graph 0 to 0,HOMO_alpha, graph 1 nohead ls 1
LMARGIN = "set lmargin at screen 0.15; set rmargin at screen 0.45"
@LMARGIN
set style arrow 1 nohead lc 7 lw 3
set style arrow 2 nohead lc 3 lw 3
p   'TbPc006DOS-ALPHA_k1-1.pdos' using (0):($2*27.211384523):(1):(0) with vectors arrowstyle 1 title '{/Symbol a}',\
    'TbPc006DOS-BETA_k1-1.pdos' using (0):($2*27.211384523):(1):(0) with vectors arrowstyle 2 title '{/Symbol b}'

LMARGIN = "set lmargin at screen 0.45; set rmargin at screen 0.90"
@LMARGIN
set ls 3  lw 1.5 dt 1 lc 0   #Straight black
set ls 8  lw 2   dt 2 lc 0   #Straight
set ls 10 lw 3   dt 1 lc 0   #Straight black line
set style textbox opaque noborder
set key at 4.5,-2.8  box opaque font ",16"
set yzeroaxis ls 10
set xrange [-5:5]
set yrange [-5:-2.5]
set xtics -5,1,5
unset ytics
set key
set xlabel 'PDOS'
unset ylabel
set y2tics -5,0.5,-2.5
set format y2 "%2.1f"
set label '{/Symbol a} ' at 3,-2.7 boxed
set label '{/Symbol b} ' at -3,-2.7 boxed

p   'T_PDOS.dat' u 7:1       w l ls 3 title    '4f-Tb',\
    'T_PDOS.dat' u (-$11):1  w l ls 3 notitle  ' ',\
    'T_PDOS.dat' u 13:1      w l ls 8 title    'Ligands',\
    'T_PDOS.dat' u (-$14):1  w l ls 8 notitle  ' ',\

unset multiplot

#-------------------------------------------------------------------------------#
reset
clear

set ls  1 lw 3 dt 1 lc 1  
set ls  2 lw 3 dt 1 lc 3  
set ls 10 lw 3 dt 1 lc 0  
set grid mytics
set xrange [-1:1]
set yrange [-5:-3]
set yzeroaxis ls 10
#set key bottom right box opaque font ",16"

set terminal pngcairo size 1024,768 enhanced font 'Arial, 23'
set output 'E_levels_MOS.png'
set format x "%2.0f"
set format y "%2.1f"
set xtics -100,100,100
set ytics -5,0.5,-3
show mytics
set style textbox opaque
set key width 2
set key at -1.7,-3.2 box opaque font ",16"
set label '{/Symbol a} ' at -0.7,-3.05 boxed
set label '{/Symbol b} ' at  0.3,-3.05 boxed
unset xtics

#set xlabel ' '
set ylabel 'Energy (eV)' offset 1.5,0

LUMO_0 = -0.15344705*27.211384523

LUMO_1 = -0.12049897*27.211384523
LUMO_2 = -0.11963221*27.211384523
LUMO_3 = -0.11720845*27.211384523
LUMO_4 = -0.11657657*27.211384523
set macros
set arrow from 0,LUMO_1, graph 0 to  1,LUMO_1, graph 1 nohead ls 2
set arrow from 0,LUMO_2, graph 0 to  1,LUMO_2, graph 1 nohead ls 2
set arrow from 0,LUMO_3, graph 0 to -1,LUMO_3, graph 1 nohead ls 2
set arrow from 0,LUMO_4, graph 0 to  1,LUMO_4, graph 1 nohead ls 2
LMARGIN = "set lmargin at screen 0.45; set rmargin at screen 0.65"
@LMARGIN
set style arrow 1 nohead lc 7 lw 3
set style arrow 2 nohead lc 3 lw 3
#set arrow from 0,LUMO_0, graph 0 to -1,LUMO_0, graph 1 nohead arrowstyle 1
p   'TbPc006DOS-ALPHA_k1-1.pdos' using (0):($2*27.211384523):(-1):(0) with vectors arrowstyle 1 title 'HOMOs',\
    'TbPc006DOS-BETA_k1-1.pdos' using (0):($2*27.211384523):(1):(0) with vectors arrowstyle 1 notitle 'HOMOs {/Symbol b}',\
