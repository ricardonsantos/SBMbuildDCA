The provided codes herein can be used as a protocol to develop protein fold predictions using structure-based models simulations and coevolutionary information.

A list of locally pre-installed softwares is required to perform this protocol:
  LovoAlign - http://www.ime.unicamp.br/~martinez/lovoalign/home.html
  Gromacs with support to gaussian potentials - http://smog-server.org/extension/gromacs-4.5.4_sbm1.0.tar.gz
  HMMER - http://hmmer.org/
  
  The SBMbuildDCA-master.zip compressed folder provided contains the following files:
  
    (1) A python script (inside folder dcasbm) to generate SBMs from protein sequence and coevolution couplings.

    (2) Python scripts to map family positions in corresponding protein sequence as interaction pairs (map_dca.py) and to trim 
       full models generating only the protein structure fragment covered by the family evaluated by coevolution (getregion.py). 

    (3) A parameter file (sbm_calpha_SA.mdp) to run SBMs simulations using simulating annealing for folding.

    (4) A folder with example input files (example_aqp1) in order to reproduce the validated protocol and debug errors    
       when simulating new sistems.
       
   
   From the files in (4), one can run the a fold prediction using the following commands in a terminal located at this same folder:
   
   
          python ../dcasbm/dcasbm.py P29972_Jpred.txt DCA_top226   
   
   will generate the SBM topology and model initial coordinates

   
          grompp -f sbm_calpha_SA.mdp -c P29972_Jpred_calpha.gro -p P29972_Jpred_calpha.top -o run.tpr   
          mdrun -deffnm run -pd                                                                          
   
   will run the simulation
   
   The final predicted model can be converted to PDB format and compared to the original experimental model (4CSK.pdb in the 
   example case) using LovoAlign implementation:
          
          editconf -f run.gro -p run.pdb
          
   will convert the GROMACS output model to PDB format.
          
          lovoalign -p1 run.pdb -p2 4CSK.pdb -seqnum
          
   will provide the TM-score between models.
   
   Questions and comments can be sent to rikchicfb@gmail.com
