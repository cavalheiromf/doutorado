from pathlib import Path
import pandas as pd


def scenario_dimensions(base_dir):
    base = Path(base_dir)
    master = pd.read_csv(
        base.parent / "comparative_axes/comparative_families_master_table_v2.tsv",
        sep="\t",
    ).set_index("FamilyID")
    ann = pd.read_csv(
        base / "results/orthogroup_functional_annotations.tsv", sep="\t"
    ).set_index("FamilyID")
    masks = [
        pd.Series(True, index=master.index),
        ~master.Flag_Transposon & ~master.Flag_High_Copy_Asymmetry,
        ~master.Flag_Organellar,
        ann.Has_Non_IEA.reindex(master.index).fillna(False),
    ]
    focal = master["BranchSig_Exp_Vper"].eq(True)
    return [(int(mask.sum()), int((mask & focal).sum())) for mask in masks]
