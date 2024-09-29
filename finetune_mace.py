import os, sys

'''
run this script using "python finetune_mace.py"
see https://github.com/ACEsuit/mace?tab=readme-ov-file#finetuning-foundation-models for documentation
'''

def command_return(i):

    command=[r'mace_run_train  ',
            r'  --name="MACE"  ',
            r'  --foundation_model="./MACE/m0-L2/L2.model" ',
            r'  --model="MACE" ',
            r'  --train_file="dataset_train_20_frame.xyz" ',  
            r'  --valid_file="dataset_valid_20_frame.xyz" ',
            r'  --energy_weight=1.0 ',
            r'  --forces_weight=10.0 ',
            r'  --stress_weight=1.0 ',
            r'  --energy_key="REF_energy" ',
            r'  --forces_key="REF_forces" ',
            r'  --stress_key="REF_stress" ',
            r'  --E0s="{3: -3.482100566595956, 35: -2.5184940099633986}" ',
            r'  --loss="universal" ',
            r'  --compute_stress="True" ',
            r'  --lr=0.005 ',
            r'  --scaling="rms_forces_scaling" ',
            r'  --batch_size=4 ',
            rf'  --max_num_epochs={i} ', 
            r'  --ema ',
            r'  --ema_decay=0.99 ',
            r'  --amsgrad ',
            r'  --default_dtype="float64" ',
            r'  --clip_grad=10 ',
            r'  --device=cuda ',
            r'  --error_table="PerAtomRMSEstressvirials" ',
            r'  --seed=3 ',
            r'  --restart_latest ',
            r'  --keep_checkpoints ',
            ]
        
    return " ".join(command)

model_epochs=[2,5,10,20,50,100,200,500,1000]

for i in model_epochs:
    command=command_return(i)
    os.system(command)
    os.system(f"mv checkpoints/MACE_run-3.model checkpoints/MACE_run-3_epoch-{i}.model")