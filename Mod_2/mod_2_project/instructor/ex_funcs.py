def get_bad_coeffs_list(model):
    pvalues = model.pvalues.rename('p-values')
    pvalues.sort_values(ascending=False,inplace=True)
    bad_pvals_coeffs = list(pvalues[ pvalues > .05].index)
    
    for coeff in ['const','Intercept']:
        if coeff in bad_pvals_coeffs:
            bad_pvals_coeffs.remove(coeff) 
    return bad_pvals_coeffs