import json
import os

clades = ["osca1", "osca2", "osca3_4"]
base_dir = "/home/mfcaval/github/doutorado/analyses/03_synteny/hyphy_subclades"

print("================================================================================")
print("             HYPHY SUBCLADE COMPARATIVE SELECTION ANALYSIS RESULTS              ")
print("================================================================================")

for clade in clades:
    clade_path = os.path.join(base_dir, clade)
    relax_json = os.path.join(clade_path, "relax_results.json")
    cf_json = os.path.join(clade_path, "contrast_fel_results.json")
    
    print(f"\n>>> CLADE: {clade.upper()} <<<")
    
    # 1. Parse RELAX Results
    if os.path.exists(relax_json):
        try:
            with open(relax_json, 'r') as f:
                r_data = json.load(f)
            
            test_results = r_data.get("test results", {})
            pval = test_results.get("p-value", "N/A")
            k_val = test_results.get("relaxation or intensification parameter", "N/A")
            
            # Format and interpret RELAX
            pval_str = f"{pval:.6f}" if isinstance(pval, float) else str(pval)
            k_str = f"{k_val:.4f}" if isinstance(k_val, float) else str(k_val)
            
            status = "No significant selection change"
            if isinstance(pval, float) and pval <= 0.05:
                if isinstance(k_val, float) and k_val < 1.0:
                    status = f"SIGNIFICANT SELECTION RELAXATION (K = {k_str}, p = {pval_str})"
                elif isinstance(k_val, float) and k_val > 1.0:
                    status = f"SIGNIFICANT SELECTION INTENSIFICATION (K = {k_str}, p = {pval_str})"
            else:
                status = f"No significant selection change (K = {k_str}, p = {pval_str})"
                
            print(f"  [RELAX] K parameter = {k_str} | LRT p-value = {pval_str}")
            print(f"  [RELAX] Biological Status: {status}")
            
            # Print GTR baseline omega values if available
            fits = r_data.get("fits", {})
            mg94 = fits.get("MG94xREV with separate rates for branch sets", {})
            rate_dist = mg94.get("Rate Distributions", {})
            omega_ref = rate_dist.get("Reference", {}).get("omega", {}).get("0", {}).get("value", "N/A")
            omega_test = rate_dist.get("Test", {}).get("omega", {}).get("0", {}).get("value", "N/A")
            if isinstance(omega_ref, (int, float)) and isinstance(omega_test, (int, float)):
                print(f"  [RELAX] dN/dS values: Reference (evergreen) = {omega_ref:.4f} | Test (resurrection) = {omega_test:.4f}")
                
        except Exception as e:
            print(f"  [RELAX] Error parsing {relax_json}: {e}")
    else:
        print("  [RELAX] relax_results.json not found!")
        
    # 2. Parse Contrast-FEL Results
    if os.path.exists(cf_json):
        try:
            with open(cf_json, 'r') as f:
                cf_data = json.load(f)
                
            mle = cf_data.get("MLE", {})
            headers = [h[0] for h in mle.get("headers", [])]
            content = mle.get("content", {})
            
            # Find indices
            alpha_idx = -1
            beta_ref_idx = -1
            beta_test_idx = -1
            pval_idx = -1
            
            for idx, h in enumerate(headers):
                h_lower = h.lower()
                if h_lower == "alpha":
                    alpha_idx = idx
                elif "beta" in h_lower and "reference" in h_lower:
                    beta_ref_idx = idx
                elif "beta" in h_lower and "test" in h_lower:
                    beta_test_idx = idx
                elif "p-value" in h_lower and "overall" in h_lower:
                    pval_idx = idx
            
            sig_sites = []
            if isinstance(content, dict):
                for partition, sites_data in content.items():
                    if isinstance(sites_data, list):
                        for s_idx, row in enumerate(sites_data):
                            pval = row[pval_idx] if pval_idx != -1 else 1.0
                            if isinstance(pval, float) and pval <= 0.05:
                                sig_sites.append((s_idx + 1, pval, row))
                    elif isinstance(sites_data, dict):
                        for s_key, row in sites_data.items():
                            pval = row[pval_idx] if pval_idx != -1 else 1.0
                            if isinstance(pval, float) and pval <= 0.05:
                                sig_sites.append((int(s_key) + 1, pval, row))
            elif isinstance(content, list):
                for s_idx, row in enumerate(content):
                    pval = row[pval_idx] if pval_idx != -1 else 1.0
                    if isinstance(pval, float) and pval <= 0.05:
                        sig_sites.append((s_idx + 1, pval, row))
                        
            print(f"  [Contrast-FEL] Found {len(sig_sites)} significant sites at nominal p <= 0.05:")
            if sig_sites:
                print(f"    {'Codon':<6} | {'alpha (syn)':<12} | {'beta_Ref (Vper)':<15} | {'beta_Test (Vtub)':<16} | {'LRT p-value':<12}")
                print(f"    {'-'*65}")
                for s, p, r in sorted(sig_sites, key=lambda x: x[0]):
                    alpha = r[alpha_idx] if alpha_idx != -1 else 0.0
                    beta_ref = r[beta_ref_idx] if beta_ref_idx != -1 else 0.0
                    beta_test = r[beta_test_idx] if beta_test_idx != -1 else 0.0
                    print(f"    {s:<6d} | {alpha:<12.4f} | {beta_ref:<15.4f} | {beta_test:<16.4f} | {p:<12.5f}")
            else:
                print("    No significant site-specific selective divergence found.")
                
        except Exception as e:
            print(f"  [Contrast-FEL] Error parsing {cf_json}: {e}")
    else:
        print("  [Contrast-FEL] contrast_fel_results.json not found!")

print("\n================================================================================")
