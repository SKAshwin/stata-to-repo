## Matching names to judges

The matching of which judge is being referred to by JudgesconcurringTouse and JudgesdissentingTouse fields (and the Author field) is done by `all_matching_judges_to_name` and `clean_matches`. This is necessary to correctly create the JudgeRulings for each case (when a dissenter is said to be WILLIAM, we need to know which of the 3 judge objects attached to that case is WILLIAM). There are some cases which couldn't be matched by general rules, and so I have noted down how they were handled.

### No matches

There are 15433 relationships that weren't matched successfully, out of about 1.16 million ruings. They are broken down as such:
```
Dissenter not found 2451
Concurrer not found 1507
Author not found 11485
```

Future work should look into the very high rate at whhich Author's couldn't be matched.

### Settling Conflicts

The case `881 F2d 1128`, with case-id `X3A693`, has a concurring judge marked as WILL, but there are two judges: `WILL, HUBERT L.` and `WILLIAMS, STEPHEN F.` who the code thinks it might be referring to. However, obviously, and from checking the case manually, it is `WILL, HUBERT L.` who concurred and wrote the opinion.

The following 32 authors are also problematic and need to be manually sorted eventually. For now, one is randomly assigned as author (in `get_matches`). For each case, the 'Author' in question could be two different judges.


| caseid | citation     | Circuit | j1name                | j2name                | j3name                  | Author   |
| ------ | ------------ | ------- | --------------------- | --------------------- | ----------------------- | -------- |
| X2AI1L | 261 F3d 701  | 7       | WOOD, HARLINGTON, JR. | WILLIAMS, ANN CLAIRE  | WOOD, DIANE PAMELA      | WOOD     |
| X315UN | 142 F3d 999  | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | RIPPLE, KENNETH F.      | WOOD     |
| X32MDE | 966 F2d 1326 | 10      | ANDERSON, STEPHEN H.  | ANDERSON, ALDON J.    | EBEL, DAVID M.          | ANDERSON |
| X353EH | 96 F3d 1033  | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | ESCHBACH, JESSE E.      | WOOD     |
| X353MP | 96 F3d 260   | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | ESCHBACH, JESSE E.      | WOOD     |
| X37P0T | 149 F3d 603  | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | KANNE, MICHAEL S.       | WOOD     |
| X3FB17 | 207 F3d 994  | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | KANNE, MICHAEL S.       | WOOD     |
| X3FLOD | 227 F3d 817  | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | KANNE, MICHAEL S.       | WOOD     |
| X3FNL0 | 232 F3d 556  | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | KANNE, MICHAEL S.       | WOOD     |
| X3FNLH | 232 F3d 595  | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | ROVNER, ILANA DIAMOND   | WOOD     |
| X3FU29 | 30 F3d 108   | 10      | ANDERSON, STEPHEN H.  | ANDERSON, ALDON J.    | EBEL, DAVID M.          | ANDERSON |
| X3PJJL | 820 F2d 384  | 0       | NEWMAN, PAULINE       | NEWMAN, BERNARD       | BISSELL, JEAN GALLOWAY  | NEWMAN   |
| X3VMH9 | 971 F2d 608  | 10      | ANDERSON, STEPHEN H.  | ANDERSON, ALDON J.    | EBEL, DAVID M.          | ANDERSON |
| X48389 | 153 F3d 805  | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | RIPPLE, KENNETH F.      | WOOD     |
| X4QAL4 | 165 F3d 579  | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | RIPPLE, KENNETH F.      | WOOD     |
| X4VBJL | 133 F3d 1025 | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | KANNE, MICHAEL S.       | WOOD     |
| X4VFLC | 141 F3d 1223 | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | RIPPLE, KENNETH F.      | WOOD     |
| X50F4B | 239 F3d 882  | 7       | WOOD, HARLINGTON, JR. | EVANS, TERENCE THOMAS | WOOD, DIANE PAMELA      | WOOD     |
| X50TAV | 252 F3d 937  | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | MANION, DANIEL A.       | WOOD     |
| X5106T | 256 F3d 702  | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | MANION, DANIEL A.       | WOOD     |
| X510T8 | 257 F3d 712  | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | KANNE, MICHAEL S.       | WOOD     |
| X51871 | 267 F3d 648  | 7       | WOOD, HARLINGTON, JR. | WILLIAMS, ANN CLAIRE  | WOOD, DIANE PAMELA      | WOOD     |
| X51A4P | 269 F3d 753  | 7       | WOOD, HARLINGTON, JR. | EVANS, TERENCE THOMAS | WOOD, DIANE PAMELA      | WOOD     |
| X51A7G | 269 F3d 871  | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | MANION, DANIEL A.       | WOOD     |
| X51DOM | 272 F3d 398  | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | MANION, DANIEL A.       | WOOD     |
| X6BCTI | 344 F3d 1282 | 11      | EDMONDSON, JAMES L.   | CARNES, EDWARD E.     | CARNES, JULIE ELIZABETH | CARNES   |
| X6CPVU | 353 F3d 1331 | 11      | EDMONDSON, JAMES L.   | CARNES, EDWARD E.     | CARNES, JULIE ELIZABETH | CARNES   |
| X6CRDU | 346 F3d 1024 | 11      | EDMONDSON, JAMES L.   | CARNES, EDWARD E.     | CARNES, JULIE ELIZABETH | CARNES   |
| XAC7M8 | 91 F3d 1032  | 7       | WOOD, HARLINGTON, JR. | WOOD, DIANE PAMELA    | KANNE, MICHAEL S.       | WOOD     |
| XAFMTQ | 277 F3d 936  | 7       | WOOD, HARLINGTON, JR. | WILLIAMS, ANN CLAIRE  | WOOD, DIANE PAMELA      | WOOD     |
| XAFNAC | 276 F3d 934  | 7       | WOOD, HARLINGTON, JR. | WILLIAMS, ANN CLAIRE  | WOOD, DIANE PAMELA      | WOOD     |
| XE6JBO | 338 F3d 1221 | 11      | EDMONDSON, JAMES L.   | CARNES, EDWARD E.     | CARNES, JULIE ELIZABETH | CARNES   |