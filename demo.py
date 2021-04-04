from pycocoevalcap.eval import eval
import json
import argparse

with open('examples/gts.json', 'r') as f: 
    gts = json.load(f)
with open('examples/res.json', 'r') as f:
    res = json.load(f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image Captioning Eval Tools')
    parser.add_argument('--gts_path',type=str,default='examples/gts.json')
    parser.add_argument('--res_path',type=str,default='examples/res.json')
    parser.add_argument('--save_spice', action='store_true')
    parser.add_argument('--save_path', type=str,default='output/test_spice.json')
    args = parser.parse_args()
    print(args)


    with open(args.gts_path, 'r') as f: 
        gts = json.load(f)
    with open(args.res_path, 'r') as f:
        res = json.load(f)
    mp = eval(gts,res,args)
    print(mp)