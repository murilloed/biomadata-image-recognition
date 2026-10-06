"""Generate synthetic images and record comparison results."""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw
from .core import compare

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="output")
    args = parser.parse_args()
    folder = Path(args.output)
    folder.mkdir(parents=True, exist_ok=True)
    before = Image.new("RGB", (256,256), (45,95,55))
    after = before.copy()
    ImageDraw.Draw(after).rectangle((128,128,255,255), fill=(180,170,120))
    before.save(folder/"before.png")
    after.save(folder/"after.png")
    report = {"synthetic": True, "training": "none; deterministic baseline",
              "scenario": "Artificial change in one quadrant; no real environmental event",
              "result": compare(before, after)}
    (folder/"report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps(report,indent=2))

if __name__ == "__main__":
    main()
