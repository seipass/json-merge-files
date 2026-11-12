from __future__ import annotations
def run(a,b):
 out=dict(a)
 for k,v in b.items(): out[k]=run(out[k],v) if k in out and isinstance(out[k],dict) and isinstance(v,dict) else v
 return out
