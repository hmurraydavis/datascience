#CODEBOOK

The majority of the column names are formatted like this:

fertilizer_crop_unit_region

...where fertilizer, crop, unit, and region are chosen from the following lists.

##fertilizer
- all: all fertilizers
- nit: nitrogen (N)
- pho: phosphate (P2O5)
- pot: potash (K2O)
- npp: nit + pho + pot total
- mul: multiple-nutrient material
- sin: single-nutrient material
- sec: secondary or micronutrient material
- mss: mul + sin + sec total
- anh: anhydrous ammonia
- aqu: aqueous ammonia
- amn: ammonium nitrate
- ams: ammonium sulfate
- nso: nitrogen solutions
- sni: sodium nitrate
- ure: urea
- not: other nitrogen (not anh, aqu, amn, ams, nso, sni, or ure)
- spl: superphosphates < 22% grade
- spg: superphosphates > 22% grade
- spo: other superphosphates (not spl or spg)
- dap: diammonium phosphate
- map: monoammonium phosphate
- npo: other nitrogen phosphate
- kcl: potassium chloride
- pos: single-nutrient potash
- gyp: gypsum
- sul: sulfur
- sfa: sulfuric acid
- znc: zinc compound
- com: compost
- man: manure
- sew: sewage sludge
- oom: other organic materials (not gyp, sul, sfa, znc, com, man, or sew)
- sp2: 20% superphosphate
- sp4: 44-46% superphosphate

##crop
- all: all crops
- cor: corn
- cot: cotton
- soy: soybeans
- whe: wheat
- oth: other crop

##unit
- ton: tons
- dol: dollars
- per: percent of acreage of crop in region receiving fertilizer
- lbs: pounds

##region
- us: the entire United States
- anything else: a state abbreviation