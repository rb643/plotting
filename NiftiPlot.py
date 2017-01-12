######################### plotting #######################
# plot vector to nifti using the original parcellation used to obtain the vector

import matplotlib.pylab as plt
import nilearn
import nilearn.plotting

import numpy as np
import nibabel as nib

# create the relevant writing function
def rebuild_nii(num):

    # load the vector
    data = np.load('Mean_Vec.npy')
    a = data[:,num].copy()
    # load the atlas
    nim = nib.load('cc400_roi_atlas.nii')
    imdat=nim.get_data()
    imdat_new = imdat.copy()

    for n, i in enumerate(np.unique(imdat)):
        if i != 0:
            imdat_new[imdat == i] = a[n-1] * 100000 # scaling factor used to offset the low numbers in our vector. Could also try to get float values in nifti...

    nim_out = nib.Nifti1Image(imdat_new, nim.get_affine(), nim.get_header())
    nim_out.set_data_dtype('float32')
    # to save:
    nim_out.to_filename('Gradient_'+ str(num) +'_res.nii')

    nilearn.plotting.plot_epi(nim_out)
    return(nim_out)

# and plot them
for i in range(10):
    nims = rebuild_nii(i)
