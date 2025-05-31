# phantom_loader.py
import numpy as np
import os

def load_image(path):
    ext = os.path.splitext(path)[-1].lower()
    
    if ext == '.dcm':
        import pydicom
        ds = pydicom.dcmread(path)
        return ds.pixel_array.astype(np.float32)
    
    elif ext in ['.nii', '.gz']:
        import nibabel as nib
        nii = nib.load(path)
        return nii.get_fdata().astype(np.float32)

    elif ext in ['.png', '.jpg', '.jpeg']:
        from PIL import Image
        img = Image.open(path).convert('L')
        return np.array(img).astype(np.float32)

    else:
        raise ValueError(f"Unsupported file type: {ext}")

