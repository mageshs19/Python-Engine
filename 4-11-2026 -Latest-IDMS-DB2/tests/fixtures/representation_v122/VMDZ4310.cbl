000010 CBL ARITH(EXTEND)                                                00010000
000020 IDENTIFICATION DIVISION.                                         00020000
000030 PROGRAM-ID. VMDZ4310.                                            00030000
000040                                                                  00040000
000050 AUTHOR.       PYTHON-AUTOMATION-USING-AI.                        00050000
000060*                                                                 00060000
000070*  OPZOEKEN GEGEVENS MAANDELIJKSE MUTATIES VIA ACCESS             00070000
000080*  IDMS DB OMLOOP/CIRCULATIE                                      00080000
000090*                                                                 00090000
000100                                                                  00100000
000110******************************************************************00110000
000120* WIJZIGINGEN :                                                  *00120000
000130*                                                                *00130000
000140* TERMA : 11/03/2009 P27                                         *00140000
000150* NIEUWE ZONE OLD-CI TOEGEVOEGD IN INPUT-FILE +                  *00150000
000160* DEZE ZONE OLD-CI MOVEN NAAR NR-CIINPTR-OORD VAN VMBD510I       *00160000
000170******************************************************************00170000
000180                                                                  00180000
000190 ENVIRONMENT DIVISION.                                            00190000
000200 CONFIGURATION SECTION.                                           00200000
000210*----------------------                                           00210000
000220 SOURCE-COMPUTER. ES9000.                                         00220000
000230 OBJECT-COMPUTER. ES9000.                                         00230000
000240 SPECIAL-NAMES.                                                   00240000
000250     DECIMAL-POINT IS COMMA.                                      00250000
000260                                                                  00260000
000270 INPUT-OUTPUT SECTION.                                            00270000
000280*---------------------                                            00280000
000290 FILE-CONTROL.                                                    00290000
000300     SELECT FI-MUTATIES         ASSIGN TO UT-S-DD010.             00300000
000310     SELECT FO-MUTATIES         ASSIGN TO UT-S-DD100.             00310000
000320                                                                  00320000
000330*----------------------                                           00330000
000340                                                                  00340000
000350                                                                  00350000
000360 DATA DIVISION.                                                   00360000
000370*---------------                                                  00370000
000380                                                                  00380000
000390 FILE SECTION.                                                    00390000
000400*-------------                                                    00400000
000410 FD  FI-MUTATIES                                                  00410000
000420     LABEL RECORD IS STANDARD                                     00420000
000430     RECORDING F                                                  00430000
000440     BLOCK CONTAINS 0.                                            00440000
000450 01  FI-MUTATIES-REC          PIC  X(21).                         00450000
000460*                                                                 00460000
000470 FD  FO-MUTATIES                                                  00470000
000480     LABEL RECORD IS STANDARD                                     00480000
000490     RECORDING F                                                  00490000
000500     BLOCK CONTAINS 0.                                            00500000
000510 01  FO-MUTATIES-REC            PIC  X(1500).                     00510000
000520*                                                                 00520000
000530 WORKING-STORAGE SECTION.                                         00530000
000540*------------------------                                         00540000
000550* -- DATE PARM --                                                 00550000
000560 01  W-DATE              PIC 9(8).                                00560000
000570 01  W-DATE-X REDEFINES W-DATE.                                   00570000
000580     05  W-DATE-Y        PIC 9(4).                                00580000
000590     05  W-DATE-M        PIC 9(2).                                00590000
000600     05  W-DATE-D        PIC 9(2).                                00600000
000610                                                                  00610000
000620 01  VOLGNUMMER                 PIC 9(07) VALUE ZEROES.           00620000
000630 01  WS-COUNT-TREATED              PIC 9(15) VALUE ZEROES.        00630000
000640                                                                  00640000
000650 01  WS-NR-ISSUE.                                                 00650000
000660     03  WS-NR-ID-ISSUE PIC X(7).                                 00660000
000670     03  WS-NR-CD-ISSUE PIC X(2).                                 00670000
000680                                                                  00680000
000690* -- CLE DU FORMULAIRE --                                         00690000
000700 01  WS-NR-ID-GOOD.                                               00700000
000710     03  WS-NR-CIO              PIC 9(8)    COMP-3.               00710000
000720     03  WS-DA-CREA             PIC 9(8)    COMP-3.               00720000
000730     03  WS-NR-ID               PIC 9(6)    COMP-3.               00730000
000740     03  WS-CT-OPD              PIC 999     COMP-3.               00740000
000750     03  WS-CT-OPG              PIC 999     COMP-3.               00750000
000760     03  FILLER                 PIC XX      VALUE SPACES.         00760000
000770                                                                  00770000
000780 01  WS-MUTATIES.                                                 00780000
000790     03 WS-IN-NR-TIT-BC PIC X(13).                                00790000
000800     03 WS-NR-SUITE     PIC X(2).                                 00800000
000810     03 WS-OLD-CI       PIC X(6).                                 00810000
000820                                                                  00820000
000830* ----- USERABEN -----                                            00830000
000840 01  USERABEN                   PIC X(8) VALUE 'USERABEN'.        00840000
000850                                                                  00850000
000860                                                                  00860000
000870*---------------------------------------------------------------* 00870000
000880*--- COPYBOOKS                                                    00880000
000890*---------------------------------------------------------------* 00890000
000900     COPY VMDZ510I.                                               00900000
000910                                                                  00910000
000920                                                                  00920000
000930*---------------------------------------------------------------* 00930000
000940*--- SWITCHES                                                     00940000
000950*---------------------------------------------------------------* 00950000
000960 01  SW-MUTATIES-EOF            PIC X.                            00960000
000970     88 MUTATIES-NOT-EOF                  VALUE 'N'.              00970000
000980     88 MUTATIES-EOF                      VALUE 'Y'.              00980000
000990                                                                  00990000
001000                                                                  01000000
001010                                                                  01010000
001020     EXEC SQL INCLUDE SQLERRWS END-EXEC.                          01020000
001030     EXEC SQL INCLUDE SQLCA END-EXEC.                             01030000
001040     EXEC SQL INCLUDE DZEVEFTV END-EXEC.                          01040000
001050     EXEC SQL INCLUDE DZBEFFTV END-EXEC.                          01050000
001060                                                                  01060000
001070                                                                  01070000
001080                                                                  01080000
001090                                                                  01090000
001100                                                                  01100000
001110 01  WS-DB2-GENERATED.                                            01110000
001120     10  CS-PROGRAM               PIC X(8)    VALUE 'VMDZ4310'.   01120000
001130                                                                  01130000
001140 01  WS-TIMESTAMP-FIELDS.                                         01140000
001150     05 TS-SYSTEM.                                                01150000
001160        10  DA-SYS.                                               01160000
001170            15  DA-SYS-CCYY.                                      01170000
001180                20  CC            PIC X(2).                       01180000
001190                20  YY            PIC X(2).                       01190000
001200            15  MM                PIC X(2).                       01200000
001210            15  DD                PIC X(2).                       01210000
001220        10  HR-SYS.                                               01220000
001230            15  HH                PIC X(2).                       01230000
001240            15  MI                PIC X(2).                       01240000
001250            15  SS                PIC X(2).                       01250000
001260            15  TT                PIC X(2).                       01260000
001270     05 TS-TIMESTAMP.                                             01270000
001280        10  CC                    PIC X(2).                       01280000
001290        10  YY                    PIC X(2).                       01290000
001300        10  TE-MARKER1            PIC X             VALUE '-'.    01300000
001310        10  MM                    PIC X(2).                       01310000
001320        10  TE-MARKER2            PIC X             VALUE '-'.    01320000
001330        10  DD                    PIC X(2).                       01330000
001340        10  TE-MARKER3            PIC X             VALUE '-'.    01340000
001350        10  HH                    PIC X(2).                       01350000
001360        10  TE-MARKER4            PIC X             VALUE '.'.    01360000
001370        10  MI                    PIC X(2).                       01370000
001380        10  TE-MARKER5            PIC X             VALUE '.'.    01380000
001390        10  SS                    PIC X(2).                       01390000
001400        10  TE-MARKER6            PIC X             VALUE '.'.    01400000
001410        10  TT                    PIC X(2).                       01410000
001420        10  NNNN                  PIC 9(04)         VALUE 0.      01420000
001430                                                                  01430000
001440 01 WS-TOTAL-INPUT PIC S9(11) COMP-3 VALUE +0.                    01440000
001450* DB2 DATE CONVERSION WORKING STORAGE                             01450000
001460 01  WS-DATUMVELDEN.                                              01460000
001470     03  DA-CCYYMMDD.                                             01470000
001480         05  CC                    PIC 99       VALUE ZERO.       01480000
001490         05  YY                    PIC 99       VALUE ZERO.       01490000
001500         05  MM                    PIC 99       VALUE ZERO.       01500000
001510         05  DD                    PIC 99       VALUE ZERO.       01510000
001520     03  DA-CCYYMMDD-R REDEFINES DA-CCYYMMDD.                     01520000
001530         05  CCYY                  PIC 9999.                      01530000
001540         05  MM                    PIC 99.                        01540000
001550         05  DD                    PIC 99.                        01550000
001560     03  DA-DD-MM-CCYY.                                           01560000
001570         05  DD                    PIC 9(02).                     01570000
001580         05  TE-MARKER5            PIC X        VALUE '.'.        01580000
001590         05  MM                    PIC 9(02).                     01590000
001600         05  TE-MARKER6            PIC X        VALUE '.'.        01600000
001610         05  CCYY                  PIC 9(04).                     01610000
001620                                                                  01620000
001630 LINKAGE SECTION.                                                 01630000
001640*----------------                                                 01640000
001650 01  LS-PARM-INPUT.                                               01650000
001660     02  LS-PARM                PIC S9(004) COMP.                 01660000
001670     02  LS-PARAM-IND           PIC X.                            01670000
001680     02  LS-DATE8               PIC  9(008).                      01680000
001690                                                                  01690000
001700                                                                  01700000
001710 PROCEDURE DIVISION USING LS-PARM-INPUT.                          01710000
001720 MAIN.                                                            01720000
001730     DISPLAY 'MAIN.'.                                             01730000
001740*-----                                                            01740000
001750     PERFORM INIT-TREATMENT                                       01750000
001760     PERFORM TREAT-MUTATIES UNTIL MUTATIES-EOF                    01760000
001770     PERFORM END-TREATMENT                                        01770000
001780     STOP RUN                                                     01780000
001790     .                                                            01790000
001800                                                                  01800000
001810*----------------------------------------------------------------*01810000
001820 INIT-TREATMENT.                                                  01820000
001830     DISPLAY 'INIT-TREATMENT.'.                                   01830000
001840     PERFORM 600-GET-TIMESTAMP.                                   01840000
001850*---------------                                                  01850000
001860     OPEN INPUT  FI-MUTATIES                                      01860000
001870     OUTPUT FO-MUTATIES                                           01870000
001880     SET MUTATIES-NOT-EOF TO TRUE.                                01880000
001890                                                                  01890000
001900* -- BINDS VOOR IDMS                                              01900000
001910                                                                  01910000
001920                                                                  01920000
001930                                                                  01930000
001940* -- READY                                                        01940000
001950                                                                  01950000
001960     PERFORM READ-MUTATIES                                        01960000
001970     .                                                            01970000
001980                                                                  01980000
001990*----------------------------------------------------------------*01990000
002000 END-TREATMENT.                                                   02000000
002010*--------------                                                   02010000
002020* -- FINISH                                                       02020000
002030                                                                  02030000
002040     CLOSE FI-MUTATIES                                            02040000
002050     FO-MUTATIES                                                  02050000
002060                                                                  02060000
002070     DISPLAY '# TREATED    = ' WS-COUNT-TREATED                   02070000
002080     DISPLAY 'TOTAL INPUTS ='  WS-TOTAL-INPUT                     02080000
002090     .                                                            02090000
002100                                                                  02100000
002110*----------------------------------------------------------------*02110000
002120 TREAT-MUTATIES.                                                  02120000
002130     DISPLAY 'TREAT-MUTATIES.'.                                   02130000
002140*--------------                                                   02140000
002150     PERFORM SEARCH-MUTATIES.                                     02150000
002160     PERFORM MOVE-MUTATIES.                                       02160000
002170     PERFORM WRITE-MUTATIES.                                      02170000
002180     PERFORM READ-MUTATIES                                        02180000
002190     .                                                            02190000
002200                                                                  02200000
002210*----------------------------------------------------------------*02210000
002220 SEARCH-MUTATIES.                                                 02220000
002230     DISPLAY 'SEARCH-MUTATIES.'.                                  02230000
002240*---------------                                                  02240000
002250     INITIALIZE DCLDZBEFFTV                                       02250000
002260     MOVE '1002'      TO CT-RKTPROD-479BEFF OF DCLDZBEFFTV.       02260000
002270*MOVEs populate the keyed SELECT.                                 02270000
002280     MOVE WS-NR-SUITE TO NS-DBSTK-479BEFF OF DCLDZBEFFTV.         02280000
002290                                                                  02290000
002300     MOVE WS-IN-NR-TIT-BC(1:12)                                   02300000
002310     TO NR-IDSTOCK-479BEFF OF DCLDZBEFFTV.                        02310000
002320     IF WS-IN-NR-TIT-BC(13:1) IS NUMERIC                          02320000
002330        MOVE WS-IN-NR-TIT-BC(13:1) TO NR-CDSTK-479BEFF            02330000
002340       OF DCLDZBEFFTV                                             02340000
002350     ELSE                                                         02350000
002360        DISPLAY 'NON-NUMERIC DB2 KEY COMPONENT'                   02360000
002370        PERFORM SQLERROR                                          02370000
002380     END-IF.                                                      02380000
002390     MOVE 442 TO SQL-LOCATION.                                    02390000
002400     EXEC SQL                                                     02400000
002410     SELECT                                                       02410000
002420       NR_IDSTOCK_479BEFF,                                        02420000
002430       NS_DBSTK_479BEFF,                                          02430000
002440       AM_CNDSTK_479BEFF,                                         02440000
002450       AM_CNSTK_479BEFF,                                          02450000
002460       NR_IDISSUE_479BEFF,                                        02460000
002470       NR_CDISSUE_479BEFF,                                        02470000
002480       NX_CPCRESK_479BEFF,                                        02480000
002490       NX_CPAIDSK_479BEFF,                                        02490000
002500       AM_INTERSK_479BEFF,                                        02500000
002510       CO_IDPRKSK_479BEFF,                                        02510000
002520       NS_IRMOSTK_479BEFF,                                        02520000
002530       DA_UBSECIS_479BEFF                                         02530000
002540     INTO                                                         02540000
002550       :DCLDZBEFFTV.NR-IDSTOCK-479BEFF,                           02550000
002560       :DCLDZBEFFTV.NS-DBSTK-479BEFF,                             02560000
002570       :DCLDZBEFFTV.AM-CNDSTK-479BEFF,                            02570000
002580       :DCLDZBEFFTV.AM-CNSTK-479BEFF,                             02580000
002590       :DCLDZBEFFTV.NR-IDISSUE-479BEFF,                           02590000
002600       :DCLDZBEFFTV.NR-CDISSUE-479BEFF,                           02600000
002610       :DCLDZBEFFTV.NX-CPCRESK-479BEFF,                           02610000
002620       :DCLDZBEFFTV.NX-CPAIDSK-479BEFF,                           02620000
002630       :DCLDZBEFFTV.AM-INTERSK-479BEFF,                           02630000
002640       :DCLDZBEFFTV.CO-IDPRKSK-479BEFF,                           02640000
002650       :DCLDZBEFFTV.NS-IRMOSTK-479BEFF,                           02650000
002660       :DCLDZBEFFTV.DA-UBSECIS-479BEFF                            02660000
002670     FROM DZBEFFTV                                                02670000
002680     WHERE                                                        02680000
002690       CT_RKTPROD_479BEFF = :DCLDZBEFFTV.CT-RKTPROD-479BEFF       02690000
002700       AND NR_IDSTOCK_479BEFF = :DCLDZBEFFTV.NR-IDSTOCK-479BEFF   02700000
002710       AND NR_CDSTK_479BEFF = :DCLDZBEFFTV.NR-CDSTK-479BEFF       02710000
002720       AND NS_DBSTK_479BEFF = :DCLDZBEFFTV.NS-DBSTK-479BEFF       02720000
002730     QUERYNO 442                                                  02730000
002740     END-EXEC                                                     02740000
002750     EVALUATE SQLCODE                                             02750000
002760       WHEN 0                                                     02760000
002770            CONTINUE                                              02770000
002780       WHEN 100                                                   02780000
002790            DISPLAY 'NO DATA FOUND FOR SELECT DZBEFFTV'           02790000
002800            PERFORM SQLERROR                                      02800000
002810       WHEN OTHER                                                 02810000
002820            DISPLAY 'ERROR ON LRF KEYED PARENT SELECT '           02820000
002830                  'DZBEFFTV'                                      02830000
002840            PERFORM SQLERROR                                      02840000
002850     END-EVALUATE                                                 02850000
002860     .                                                            02860000
002870     INITIALIZE DCLDZEVEFTV                                       02870000
002880     MOVE 254 TO SQL-LOCATION                                     02880000
002890     EXEC SQL                                                     02890000
002900        SELECT NR_IDGOOD_479EVEF,                                 02900000
002910           NR_CI1POS_479EVEF,                                     02910000
002920           NR_CI26POS_479EVEF,                                    02920000
002930           DA_CREVTPD_479EVEF                                     02930000
002940        INTO                                                      02940000
002950           :DCLDZEVEFTV.NR-IDGOOD-479EVEF,                        02950000
002960           :DCLDZEVEFTV.NR-CI1POS-479EVEF,                        02960000
002970           :DCLDZEVEFTV.NR-CI26POS-479EVEF,                       02970000
002980           :DCLDZEVEFTV.DA-CREVTPD-479EVEF                        02980000
002990        FROM DZEVEFTV                                             02990000
003000        WHERE CT_RKTPROD_479BEFF = :DCLDZBEFFTV.CT-RKTPROD-479BEFF03000000
003010        AND NR_IDSTOCK_479BEFF = :DCLDZBEFFTV.NR-IDSTOCK-479BEFF  03010000
003020        AND NR_CDSTK_479BEFF = :DCLDZBEFFTV.NR-CDSTK-479BEFF      03020000
003030        AND NS_DBSTK_479BEFF = :DCLDZBEFFTV.NS-DBSTK-479BEFF      03030000
003040        AND CT_RKTEVPR_479EVEF = '0092'                           03040000
003050        ORDER BY NR_ID_479EVEF DESC                               03050000
003060        FETCH FIRST 1 ROW ONLY                                    03060000
003070        QUERYNO 254                                               03070000
003080     END-EXEC                                                     03080000
003090     IF SQLCODE NOT = 0 AND SQLCODE NOT = 100                     03090000
003100        DISPLAY 'ERROR ON LRF SINGLETON SELECT'                   03100000
003110        PERFORM SQLERROR                                          03110000
003120     END-IF.                                                      03120000
003130                                                                  03130000
003140*                                                                 03140000
003150     IF SQLCODE = 100                                             03150000
003160        DISPLAY 'NO DATA FOUND FOR BOUNDED LRF SELECT'            03160000
003170        DISPLAY 'K1=' CT-RKTPROD-479BEFF OF DCLDZBEFFTV           03170000
003180        DISPLAY 'K2=' NR-IDSTOCK-479BEFF OF DCLDZBEFFTV           03180000
003190        DISPLAY 'K3=' NR-CDSTK-479BEFF OF DCLDZBEFFTV             03190000
003200        DISPLAY 'K4=' NS-DBSTK-479BEFF OF DCLDZBEFFTV             03200000
003210        CALL USERABEN                                             03210000
003220     END-IF.                                                      03220000
003230                                                                  03230000
003240* -- ZOEK DE MUTATIE                                              03240000
003250                                                                  03250000
003260     IF SQLCODE = 100                                             03260000
003270        DISPLAY 'NO MORE VMBEVEF : '                              03270000
003280        DISPLAY 'K1=' CT-RKTPROD-479BEFF OF DCLDZBEFFTV           03280000
003290        DISPLAY 'K2=' NR-IDSTOCK-479BEFF OF DCLDZBEFFTV           03290000
003300        DISPLAY 'K3=' NR-CDSTK-479BEFF OF DCLDZBEFFTV             03300000
003310        DISPLAY 'K4=' NS-DBSTK-479BEFF OF DCLDZBEFFTV             03310000
003320        CALL USERABEN                                             03320000
003330     END-IF.                                                      03330000
003340                                                                  03340000
003350*----------------------------------------------------------------*03350000
003360 MOVE-MUTATIES.                                                   03360000
003370     DISPLAY 'MOVE-MUTATIES.'.                                    03370000
003380*-------------                                                    03380000
003390     INITIALIZE VMDZ510I                                          03390000
003400     REPLACING ALPHANUMERIC BY SPACES                             03400000
003410     NUMERIC BY ZEROES.                                           03410000
003420                                                                  03420000
003430     MOVE NR-IDGOOD-479EVEF OF DCLDZEVEFTV TO WS-NR-ID-GOOD.      03430000
003440                                                                  03440000
003450     MOVE NR-CI1POS-479EVEF OF DCLDZEVEFTV TO NR-CIO-FORM-AS      03450000
003460       OF VMDZ510I(1:1).                                          03460000
003470     MOVE NR-CI26POS-479EVEF OF DCLDZEVEFTV TO NR-CIO-FORM-AS     03470000
003480       OF VMDZ510I(2:5).                                          03480000
003490     MOVE WS-DA-CREA TO DA-CREA-FORM-AS-R OF VMDZ510I.            03490000
003500     STRING DA-CR-FORM-AS-Y   OF VMDZ510I '-'                     03500000
003510        DA-CR-FORM-AS-M   OF VMDZ510I '-'                         03510000
003520        DA-CR-FORM-AS-D   OF VMDZ510I '-'                         03520000
003530            '01.01.01.000001'                                     03530000
003540        DELIMITED BY SIZE                                         03540000
003550       INTO TS-CREA-OORD      OF VMDZ510I.                        03550000
003560        MOVE WS-NR-ID  TO NR-ID-FORM-AS OF VMDZ510I.              03560000
003570        MOVE WS-CT-OPG TO CT-OPG-FORM-AS-R OF VMDZ510I.           03570000
003580        MOVE WS-CT-OPD TO CT-OPD-FORM-AS-R OF VMDZ510I.           03580000
003590                                                                  03590000
003600        MOVE NR-IDISSUE-479BEFF OF DCLDZBEFFTV TO WS-NR-ID-ISSUE  03600000
003610        MOVE NR-CDISSUE-479BEFF OF DCLDZBEFFTV TO WS-NR-CD-ISSUE  03610000
003620        MOVE WS-NR-ISSUE TO NR-ISSUIN-OORD OF VMDZ510I.           03620000
003630        MOVE AM-CNSTK-479BEFF OF DCLDZBEFFTV                      03630000
003640       TO AM-CNS-FORM-AS      OF VMDZ510I.                        03640000
003650        MOVE NR-IDSTOCK-479BEFF OF DCLDZBEFFTV TO NR-ST-FORM-AS-R103650000
003660       OF VMDZ510I.                                               03660000
003670        MOVE NR-CDSTK-479BEFF OF DCLDZBEFFTV TO NR-ST-FORM-AS-P4  03670000
003680       OF VMDZ510I.                                               03680000
003690        MOVE NR-ST-FORM-AS OF VMDZ510I TO NR-STIN-OORD            03690000
003700       OF VMDZ510I.                                               03700000
003710        MOVE NS-DBSTK-479BEFF OF DCLDZBEFFTV                      03710000
003720       TO NS-DBST-OORD        OF VMDZ510I.                        03720000
003730        IF NX-CPCRESK-479BEFF OF DCLDZBEFFTV = 0                  03730000
003740           MOVE AM-CNDSTK-479BEFF OF DCLDZBEFFTV                  03740000
003750         TO AM-CND-FORM-AS      OF VMDZ510I                       03750000
003760        ELSE                                                      03760000
003770           MOVE AM-INTERSK-479BEFF OF DCLDZBEFFTV                 03770000
003780         TO AM-INTER-FORM-AS    OF VMDZ510I                       03780000
003790        END-IF.                                                   03790000
003800        MOVE CO-IDPRKSK-479BEFF OF DCLDZBEFFTV                    03800000
003810       TO NR-ID-040SECU       OF VMDZ510I.                        03810000
003820        MOVE NS-IRMOSTK-479BEFF OF DCLDZBEFFTV                    03820000
003830       TO NS-SEQ-040IRMO      OF VMDZ510I.                        03830000
003840        MOVE ZEROES TO DA-CCYYMMDD                                03840000
003850        MOVE DA-UBSECIS-479BEFF OF DCLDZBEFFTV TO DA-DD-MM-CCYY   03850000
003860        EVALUATE TRUE                                             03860000
003870          WHEN DA-DD-MM-CCYY = '01.01.0001'                       03870000
003880               MOVE ZEROES TO DA-CCYYMMDD-R                       03880000
003890          WHEN DA-DD-MM-CCYY = '31.12.9999'                       03890000
003900               MOVE '99999999' TO DA-CCYYMMDD-R                   03900000
003910          WHEN OTHER                                              03910000
003920               MOVE CCYY OF DA-DD-MM-CCYY TO CCYY OF DA-CCYYMMDD-R03920000
003930               MOVE MM OF DA-DD-MM-CCYY TO MM OF DA-CCYYMMDD-R    03930000
003940               MOVE DD OF DA-DD-MM-CCYY TO DD OF DA-CCYYMMDD-R    03940000
003950        END-EVALUATE                                              03950000
003960        MOVE DA-CCYYMMDD-R TO DA-UB-FORM-AS OF VMDZ510I.          03960000
003970        MOVE ZEROES TO DA-CCYYMMDD                                03970000
003980        MOVE DA-CREVTPD-479EVEF OF DCLDZEVEFTV TO DA-DD-MM-CCYY   03980000
003990        EVALUATE TRUE                                             03990000
004000          WHEN DA-DD-MM-CCYY = '01.01.0001'                       04000000
004010               MOVE ZEROES TO DA-CCYYMMDD-R                       04010000
004020          WHEN DA-DD-MM-CCYY = '31.12.9999'                       04020000
004030               MOVE '99999999' TO DA-CCYYMMDD-R                   04030000
004040          WHEN OTHER                                              04040000
004050               MOVE CCYY OF DA-DD-MM-CCYY TO CCYY OF DA-CCYYMMDD-R04050000
004060               MOVE MM OF DA-DD-MM-CCYY TO MM OF DA-CCYYMMDD-R    04060000
004070               MOVE DD OF DA-DD-MM-CCYY TO DD OF DA-CCYYMMDD-R    04070000
004080        END-EVALUATE                                              04080000
004090        MOVE DA-CCYYMMDD-R TO DA-COMPTABILISATION-OPER            04090000
004100       OF VMDZ510I.                                               04100000
004110        MOVE ZEROES TO DA-CCYYMMDD                                04110000
004120        MOVE DA-CREVTPD-479EVEF OF DCLDZEVEFTV TO DA-DD-MM-CCYY   04120000
004130        EVALUATE TRUE                                             04130000
004140          WHEN DA-DD-MM-CCYY = '01.01.0001'                       04140000
004150               MOVE ZEROES TO DA-CCYYMMDD-R                       04150000
004160          WHEN DA-DD-MM-CCYY = '31.12.9999'                       04160000
004170               MOVE '99999999' TO DA-CCYYMMDD-R                   04170000
004180          WHEN OTHER                                              04180000
004190               MOVE CCYY OF DA-DD-MM-CCYY TO CCYY OF DA-CCYYMMDD-R04190000
004200               MOVE MM OF DA-DD-MM-CCYY TO MM OF DA-CCYYMMDD-R    04200000
004210               MOVE DD OF DA-DD-MM-CCYY TO DD OF DA-CCYYMMDD-R    04210000
004220        END-EVALUATE                                              04220000
004230        MOVE DA-CCYYMMDD-R TO DA-EXEC-OORD OF VMDZ510I.           04230000
004240                                                                  04240000
004250        MOVE NX-CPCRESK-479BEFF OF DCLDZBEFFTV                    04250000
004260       TO NS-RANK-COUP        OF VMDZ510I.                        04260000
004270        MOVE NX-CPAIDSK-479BEFF OF DCLDZBEFFTV                    04270000
004280       TO NX-CPAID-STOCK      OF VMDZ510I.                        04280000
004290*    MOVE NX-CPFDU-STOCK      OF VMBEFF                           04290000
004300                                                                  04300000
004310* EXTRA ZONES OPVULLEN                                            04310000
004320                                                                  04320000
004330        EVALUATE WS-CT-OPD                                        04330000
004340          WHEN 00                                                 04340000
004350               MOVE 'MU' TO CO-TYPOPER-OORD OF VMDZ510I           04350000
004360          WHEN OTHER                                              04360000
004370               MOVE '??' TO CO-TYPOPER-OORD OF VMDZ510I           04370000
004380               DISPLAY 'ABEND VERKEERDE CT-OPD = '                04380000
004390               WS-CT-OPD                                          04390000
004400               DISPLAY DCLDZBEFFTV                                04400000
004410               DISPLAY DCLDZEVEFTV                                04410000
004420               CALL USERABEN                                      04420000
004430        END-EVALUATE.                                             04430000
004440* UITGIFTE = SRW DUS '1'                                          04440000
004450        MOVE '1' TO CO-ISSUIN-OORD OF VMDZ510I.                   04450000
004460        MOVE 001 TO NB-ST-OORD OF VMDZ510I.                       04460000
004470* EFFECT = IKB = DEXIA DUS '1'                                    04470000
004480        MOVE '1' TO CO-STIN-OORD OF VMDZ510I.                     04480000
004490                                                                  04490000
004500        ADD 1 TO VOLGNUMMER.                                      04500000
004510        STRING 'CIR '                                             04510000
004520           CT-OPD-FORM-AS OF VMDZ510I ' '                         04520000
004530           VOLGNUMMER                                             04530000
004540           DELIMITED BY SIZE                                      04540000
004550       INTO NR-REFORD-OORD OF VMDZ510I.                           04550000
004560                                                                  04560000
004570* EXTRA'S ANNIE STEPPE                                            04570000
004580           STRING 'X'                                             04580000
004590            '000000'                                              04590000
004600            '      '                                              04600000
004610              DELIMITED BY SIZE                                   04610000
004620       INTO NR-TRANS-OORD  OF VMDZ510I.                           04620000
004630* 10=AGENCY 11=ZETEL                                              04630000
004640*    IF NR-CIO-FORM-AS OF VMDZ510I =                              04640000
004650*       NR-CIW-FORM-AS OF VMDZ510I                                04650000
004660              MOVE '10' TO CO-TYPKAN2-OORD OF VMDZ510I            04660000
004670*    ELSE                                                         04670000
004680*      MOVE '11' TO CO-TYPKAN2-OORD OF VMDZ510I                   04680000
004690*    END-IF.                                                      04690000
004700              MOVE 'DX' TO CO-BANK-OORD OF VMDZ510I.              04700000
004710                                                                  04710000
004720              MOVE WS-OLD-CI TO NR-CIINPTR-OORD OF VMDZ510I.      04720000
004730                                                                  04730000
004740*----------------------------------------------------------------*04740000
004750 WRITE-MUTATIES.                                                  04750000
004760     DISPLAY 'WRITE-MUTATIES.'.                                   04760000
004770*--------------                                                   04770000
004780     ADD 1 TO WS-COUNT-TREATED                                    04780000
004790     WRITE FO-MUTATIES-REC FROM VMDZ510I                          04790000
004800     .                                                            04800000
004810                                                                  04810000
004820*----------------------------------------------------------------*04820000
004830 READ-MUTATIES.                                                   04830000
004840     DISPLAY 'READ-MUTATIES.'.                                    04840000
004850*-------------                                                    04850000
004860     READ FI-MUTATIES INTO    WS-MUTATIES                         04860000
004870        AT END                                                    04870000
004880        SET MUTATIES-EOF TO TRUE                                  04880000
004890     NOT AT END                                                   04890000
004900        ADD 1 TO WS-TOTAL-INPUT                                   04900000
004910        CONTINUE                                                  04910000
004920     END-READ                                                     04920000
004930     .                                                            04930000
004940                                                                  04940000
004950/---------------------------------------------------------------* 04950000
004960*    ERROR HANDLING                                               04960000
004970*---------------------------------------------------------------* 04970000
004980                                                                  04980000
004990                                                                  04990000
005000 600-GET-TIMESTAMP.                                               05000000
005010     DISPLAY '600-GET-TIMESTAMP.'.                                05010000
005020     MOVE FUNCTION CURRENT-DATE TO TS-SYSTEM.                     05020000
005030     MOVE CC OF TS-SYSTEM       TO CC OF TS-TIMESTAMP             05030000
005040     MOVE YY OF TS-SYSTEM       TO YY OF TS-TIMESTAMP             05040000
005050     MOVE MM OF TS-SYSTEM       TO MM OF TS-TIMESTAMP             05050000
005060     MOVE DD OF TS-SYSTEM       TO DD OF TS-TIMESTAMP             05060000
005070     MOVE HH OF TS-SYSTEM       TO HH OF TS-TIMESTAMP             05070000
005080     MOVE MI OF TS-SYSTEM       TO MI OF TS-TIMESTAMP             05080000
005090     MOVE SS OF TS-SYSTEM       TO SS OF TS-TIMESTAMP             05090000
005100     MOVE TT OF TS-SYSTEM       TO TT OF TS-TIMESTAMP             05100000
005110     DISPLAY 'TIMESTAMP: ' TS-TIMESTAMP                           05110000
005120     .                                                            05120000
005130                                                                  05130000
005140*SQLERROR ROUTINE.                                                05140000
005150     EXEC SQL                                                     05150000
005160          INCLUDE SQLERROR                                        05160000
005170     END-EXEC.                                                    05170000
