"""Compare already aligned images; this method does not classify environmental events."""
from math import isfinite
from PIL import Image

def compare(before: Image.Image, after: Image.Image, threshold: float = 30):
    if not isfinite(threshold) or not 1 <= threshold <= 255:
        raise ValueError("threshold must be finite and between 1 and 255")
    if before.size != after.size:
        raise ValueError("Images must have the same dimensions and already be aligned")
    if min(before.size) < 1:
        raise ValueError("Images must not be empty")
    a = list(before.convert("L").resize((32, 32), Image.Resampling.BILINEAR).tobytes())
    b = list(after.convert("L").resize((32, 32), Image.Resampling.BILINEAR).tobytes())
    differences = [abs(x-y) for x,y in zip(a,b)]
    changed = sum(d > threshold for d in differences)
    return {"method": "absolute luminance difference", "grid": [32,32],
            "threshold": threshold, "changed_cells": changed,
            "total_cells": len(differences), "changed_percent": round(100*changed/len(differences),2),
            "mean_difference": round(sum(differences)/len(differences),2),
            "limitation": "Requires aligned images; does not identify wildfires, classify land use or establish legality."}
