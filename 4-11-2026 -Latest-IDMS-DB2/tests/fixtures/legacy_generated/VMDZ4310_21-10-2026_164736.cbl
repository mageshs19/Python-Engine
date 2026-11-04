000010 CBL ARITH(EXTEND)                                                00010000
000020 IDENTIFICATION DIVISION.                                         00020000
000030*========================                                         00030000
000040 PROGRAM-ID. VMDZ4310.                                            00040000
000050                                                                  00050000
000060 AUTHOR.       PYTHON-AUTOMATION-USING-AI.                        00060000
000070*                                                                 00070000
000080*  OPZOEKEN GEGEVENS MAANDELIJKSE MUTATIES VIA ACCESS             00080000
000090*  IDMS DB OMLOOP/CIRCULATIE                                      00090000
000100*                                                                 00100000
000110                                                                  00110000
000120******************************************************************00120000
000130* WIJZIGINGEN :                                                  *00130000
000140*                                                                *00140000
000150* TERMA : 11/03/2009 P27                                         *00150000
000160* NIEUWE ZONE OLD-CI TOEGEVOEGD IN INPUT-FILE +                  *00160000
000170* DEZE ZONE OLD-CI MOVEN NAAR NR-CIINPTR-OORD VAN VMBD510I       *00170000
000180******************************************************************00180000
000190                                                                  00190000
000200 ENVIRONMENT DIVISION.                                            00200000
000210*=====================                                            00210000
000220 CONFIGURATION SECTION.                                           00220000
000230*----------------------                                           00230000
000240 SOURCE-COMPUTER. ES9000.                                         00240000
000250 OBJECT-COMPUTER. ES9000.                                         00250000
000260 SPECIAL-NAMES.                                                   00260000
000270     DECIMAL-POINT IS COMMA.                                      00270000
000280                                                                  00280000
000290 INPUT-OUTPUT SECTION.                                            00290000
000300*---------------------                                            00300000
000310 FILE-CONTROL.                                                    00310000
000320     SELECT FI-MUTATIES         ASSIGN TO UT-S-DD010.             00320000
000330     SELECT FO-MUTATIES         ASSIGN TO UT-S-DD100.             00330000
000340                                                                  00340000
000350*----------------------                                           00350000
000360                                                                  00360000
000370                                                                  00370000
000380 DATA DIVISION.                                                   00380000
000390*==============                                                   00390000
000400*---------------                                                  00400000
000410                                                                  00410000
000420 FILE SECTION.                                                    00420000
000430*-------------                                                    00430000
000440 FD  FI-MUTATIES                                                  00440000
000450     LABEL RECORD IS STANDARD                                     00450000
000460     RECORDING F                                                  00460000
000470     BLOCK CONTAINS 0.                                            00470000
000480 01  FI-MUTATIES-REC          PIC  X(21).                         00480000
000490*                                                                 00490000
000500 FD  FO-MUTATIES                                                  00500000
000510     LABEL RECORD IS STANDARD                                     00510000
000520     RECORDING F                                                  00520000
000530     BLOCK CONTAINS 0.                                            00530000
000540 01  FO-MUTATIES-REC            PIC  X(1500).                     00540000
000550*                                                                 00550000
000560 WORKING-STORAGE SECTION.                                         00560000
000570*------------------------                                         00570000
000580* -- DATE PARM --                                                 00580000
000590 01  W-DATE              PIC 9(8).                                00590000
000600 01  W-DATE-X REDEFINES W-DATE.                                   00600000
000610     05  W-DATE-Y        PIC 9(4).                                00610000
000620     05  W-DATE-M        PIC 9(2).                                00620000
000630     05  W-DATE-D        PIC 9(2).                                00630000
000640                                                                  00640000
000650 01  VOLGNUMMER                 PIC 9(07) VALUE ZEROES.           00650000
000660 01  COUNT-TREATED              PIC 9(15) VALUE ZEROES.           00660000
000670                                                                  00670000
000680 01  WS-NR-ISSUE.                                                 00680000
000690     03  WS-NR-ID-ISSUE PIC X(7).                                 00690000
000700     03  WS-NR-CD-ISSUE PIC X(2).                                 00700000
000710                                                                  00710000
000720* -- CLE DU FORMULAIRE --                                         00720000
000730 01  WS-NR-ID-GOOD.                                               00730000
000740     03  WS-NR-CIO              PIC 9(8)    COMP-3.               00740000
000750     03  WS-DA-CREA             PIC 9(8)    COMP-3.               00750000
000760     03  WS-NR-ID               PIC 9(6)    COMP-3.               00760000
000770     03  WS-CT-OPD              PIC 999     COMP-3.               00770000
000780     03  WS-CT-OPG              PIC 999     COMP-3.               00780000
000790     03  FILLER                 PIC XX      VALUE SPACES.         00790000
000800                                                                  00800000
000810 01  WS-MUTATIES.                                                 00810000
000820     03 WS-IN-NR-TIT-BC PIC X(13).                                00820000
000830     03 WS-NR-SUITE     PIC X(2).                                 00830000
000840     03 WS-OLD-CI       PIC X(6).                                 00840000
000850                                                                  00850000
000860* ----- USERABEN -----                                            00860000
000870 01  USERABEN                   PIC X(8) VALUE 'USERABEN'.        00870000
000880                                                                  00880000
000890 01  CS-VM4BD310                PIC X(8) VALUE 'VMDZ4310'.        00890000
000900                                                                  00900000
000910*---------------------------------------------------------------* 00910000
000920*--- COPYBOOKS                                                    00920000
000930*---------------------------------------------------------------* 00930000
000940     COPY VMDZ510I.                                               00940000
000950                                                                  00950000
000960     COPY VMDZ05.                                                 00960000
000970                                                                  00970000
000980*---------------------------------------------------------------* 00980000
000990*--- SWITCHES                                                     00990000
001000*---------------------------------------------------------------* 01000000
001010 01  SW-MUTATIES-EOF            PIC X.                            01010000
001020     88 MUTATIES-NOT-EOF                  VALUE 'N'.              01020000
001030     88 MUTATIES-EOF                      VALUE 'Y'.              01030000
001040                                                                  01040000
001050                                                                  01050000
001060                                                                  01060000
001070*DB2 INFRASTRUCTURE - SQLCA, INCLUDES, FLAGS                   *  01070000
001080     EXEC SQL INCLUDE SQLERRWS END-EXEC.                          01080000
001090     EXEC SQL INCLUDE SQLCA END-EXEC.                             01090000
001100     EXEC SQL INCLUDE DZEVEFTV END-EXEC.                          01100000
001110     EXEC SQL INCLUDE DZBEFFTV END-EXEC.                          01110000
001120                                                                  01120000
001130*DB2 CURSOR END-OF-CURSOR FLAGS                                *  01130000
001140 01  WS-DZEVEFC1-FLAG               PIC X.                        01140000
001150     88  DZEVEFC1-NOT-EOC           VALUE 'N'.                    01150000
001160     88  DZEVEFC1-EOC               VALUE 'Y'.                    01160000
001170                                                                  01170000
001180                                                                  01180000
001190*DB2 CURSOR DECLARATIONS                                       *  01190000
001200     EXEC SQL DECLARE DZEVEFC1 CURSOR WITH HOLD FOR               01200000
001210       SELECT CT_RKTEVPR_479EVEF                                  01210000
001220            , DA_CREVTPD_479EVEF                                  01220000
001230            , NR_CI1POS_479EVEF                                   01230000
001240            , NR_CI26POS_479EVEF                                  01240000
001250            , NR_IDGOOD_479EVEF                                   01250000
001260            , NR_ID_479EVEF                                       01260000
001270       FROM DZEVEFTV                                              01270000
001280       WHERE CT_RKTPROD_479BEFF = :DCLDZBEFFTV.CT-RKTPROD-479BEFF 01280000
001290         AND NR_IDSTOCK_479BEFF = :DCLDZBEFFTV.NR-IDSTOCK-479BEFF 01290000
001300         AND NR_CDSTK_479BEFF = :DCLDZBEFFTV.NR-CDSTK-479BEFF     01300000
001310         AND NS_DBSTK_479BEFF = :DCLDZBEFFTV.NS-DBSTK-479BEFF     01310000
001320       ORDER BY NR_ID_479EVEF DESC                                01320000
001330       FOR READ ONLY                                              01330000
001340       QUERYNO 254                                                01340000
001350     END-EXEC.                                                    01350000
001360                                                                  01360000
001370                                                                  01370000
001380*DB2 GENERATED WORKING STORAGE                                    01380000
001390 01  WS-DB2-GENERATED.                                            01390000
001400     10  CS-PROGRAM               PIC X(8)    VALUE 'VMDZ4310'.   01400000
001410                                                                  01410000
001420*DB2 GENERATED TIMESTAMP AND AUDIT WORKING STORAGE                01420000
001430 01  WS-TIMESTAMP-FIELDS.                                         01430000
001440     05 TS-SYSTEM.                                                01440000
001450        10  DA-SYS.                                               01450000
001460            15  DA-SYS-CCYY.                                      01460000
001470                20  CC            PIC X(2).                       01470000
001480                20  YY            PIC X(2).                       01480000
001490            15  MM                PIC X(2).                       01490000
001500            15  DD                PIC X(2).                       01500000
001510        10  HR-SYS.                                               01510000
001520            15  HH                PIC X(2).                       01520000
001530            15  MI                PIC X(2).                       01530000
001540            15  SS                PIC X(2).                       01540000
001550            15  TT                PIC X(2).                       01550000
001560     05 TS-TIMESTAMP.                                             01560000
001570        10  CC                    PIC X(2).                       01570000
001580        10  YY                    PIC X(2).                       01580000
001590        10  TE-MARKER1            PIC X             VALUE '-'.    01590000
001600        10  MM                    PIC X(2).                       01600000
001610        10  TE-MARKER2            PIC X             VALUE '-'.    01610000
001620        10  DD                    PIC X(2).                       01620000
001630        10  TE-MARKER3            PIC X             VALUE '-'.    01630000
001640        10  HH                    PIC X(2).                       01640000
001650        10  TE-MARKER4            PIC X             VALUE '.'.    01650000
001660        10  MI                    PIC X(2).                       01660000
001670        10  TE-MARKER5            PIC X             VALUE '.'.    01670000
001680        10  SS                    PIC X(2).                       01680000
001690        10  TE-MARKER6            PIC X             VALUE '.'.    01690000
001700        10  TT                    PIC X(2).                       01700000
001710        10  NNNN                  PIC 9(04)         VALUE 0.      01710000
001720                                                                  01720000
001730 LINKAGE SECTION.                                                 01730000
001740*----------------                                                 01740000
001750 01  LS-PARM-INPUT.                                               01750000
001760     02  LS-PARM                PIC S9(004) COMP.                 01760000
001770     02  LS-PARAM-IND           PIC X.                            01770000
001780     02  LS-DATE8               PIC  9(008).                      01780000
001790                                                                  01790000
001800                                                                  01800000
001810 PROCEDURE DIVISION USING LS-PARM-INPUT.                          01810000
001820*=======================================                          01820000
001830     PERFORM 600-GET-TIMESTAMP.                                   01830000
001840                                                                  01840000
001850 MAIN.                                                            01850000
001860*-----                                                            01860000
001870     PERFORM INIT-TREATMENT                                       01870000
001880     PERFORM TREAT-MUTATIES UNTIL MUTATIES-EOF                    01880000
001890     PERFORM END-TREATMENT                                        01890000
001900     STOP RUN                                                     01900000
001910     .                                                            01910000
001920                                                                  01920000
001930*----------------------------------------------------------------*01930000
001940 INIT-TREATMENT.                                                  01940000
001950*---------------                                                  01950000
001960     OPEN INPUT  FI-MUTATIES                                      01960000
001970     OUTPUT FO-MUTATIES                                           01970000
001980     SET MUTATIES-NOT-EOF TO TRUE.                                01980000
001990                                                                  01990000
002000* -- BINDS VOOR IDMS                                              02000000
002010                                                                  02010000
002020                                                                  02020000
002030                                                                  02030000
002040* -- READY                                                        02040000
002050                                                                  02050000
002060     PERFORM READ-MUTATIES                                        02060000
002070     .                                                            02070000
002080                                                                  02080000
002090*----------------------------------------------------------------*02090000
002100 END-TREATMENT.                                                   02100000
002110*--------------                                                   02110000
002120* -- FINISH                                                       02120000
002130                                                                  02130000
002140     CLOSE FI-MUTATIES                                            02140000
002150     FO-MUTATIES                                                  02150000
002160                                                                  02160000
002170     DISPLAY '# TREATED  = ' COUNT-TREATED                        02170000
002180     .                                                            02180000
002190                                                                  02190000
002200*----------------------------------------------------------------*02200000
002210 TREAT-MUTATIES.                                                  02210000
002220*--------------                                                   02220000
002230     PERFORM SEARCH-MUTATIES.                                     02230000
002240     PERFORM MOVE-MUTATIES.                                       02240000
002250     PERFORM WRITE-MUTATIES.                                      02250000
002260     PERFORM READ-MUTATIES                                        02260000
002270     .                                                            02270000
002280                                                                  02280000
002290*----------------------------------------------------------------*02290000
002300 SEARCH-MUTATIES.                                                 02300000
002310*---------------                                                  02310000
002320*DB2: Removed redundant key-group clear; all mapped CALC key      02320000
002330*components are initialized and assigned before SELECT.           02330000
002340     INITIALIZE DCLDZBEFFTV                                       02340000
002350     MOVE '1002'      TO CT-RKTPROD-479BEFF OF DCLDZBEFFTV.       02350000
002360*MOVEs populate the keyed SELECT.                                 02360000
002370     MOVE WS-NR-SUITE TO NS-DBSTK-479BEFF OF DCLDZBEFFTV.         02370000
002380                                                                  02380000
002390*DB2: Expanded LRF FIRST VMBTL07-R01 WHERE ALL-VMBEVEF-BY-VMBEFF  02390000
002400*  -> VMBEVEF WITHIN VMBEFF-VMBEVEF.                              02400000
002410*DB2: LRF path ALL-VMBEVEF-BY-VMBEFF keyed parent access on VMBEFF02410000
002420*  (CALC).                                                        02420000
002430*DB2: LRF keyed parent read for VMBEFF -> keyed SELECT.           02430000
002440     MOVE WS-IN-NR-TIT-BC(1:12)                                   02440000
002450     TO NR-IDSTOCK-479BEFF OF DCLDZBEFFTV.                        02450000
002460     IF WS-IN-NR-TIT-BC(13:1) IS NUMERIC                          02460000
002470        MOVE WS-IN-NR-TIT-BC(13:1) TO NR-CDSTK-479BEFF            02470000
002480      OF DCLDZBEFFTV                                              02480000
002490     ELSE                                                         02490000
002500        DISPLAY 'INVALID LRF CALC KEY FOR VMBEFF'                 02500000
002510        PERFORM SQLERROR                                          02510000
002520     END-IF.                                                      02520000
002530*DB2: Converted LRF keyed parent read for VMBEFF.                 02530000
002530*MOVE 'SELECT-VMBEFF' TO SQL-LOCATION.                            02530000
002540     EXEC SQL                                                     02540000
002550    SELECT                                                        02550000
002560       CT_RKTPROD_479BEFF,                                        02560000
002570       NR_IDSTOCK_479BEFF,                                        02570000
002580       NR_CDSTK_479BEFF,                                          02580000
002590       NS_DBSTK_479BEFF,                                          02590000
002600       AM_CNDSTK_479BEFF,                                         02600000
002610       AM_CNSTK_479BEFF,                                          02610000
002620       CT_RKTPRDX_479BEFF,                                        02620000
002630       NR_IDISSUE_479BEFF,                                        02630000
002640       NR_CDISSUE_479BEFF,                                        02640000
002650       NX_CPCRESK_479BEFF,                                        02650000
002660       NX_CPAIDSK_479BEFF,                                        02660000
002670       NX_CPFDUSK_479BEFF,                                        02670000
002680       AM_INTERSK_479BEFF,                                        02680000
002690       CO_IDPRKSK_479BEFF,                                        02690000
002700       NS_IRMOSTK_479BEFF,                                        02700000
002710       DA_UBSECIS_479BEFF                                         02710000
002720    INTO                                                          02720000
002730       :DCLDZBEFFTV.CT-RKTPROD-479BEFF,                           02730000
002740       :DCLDZBEFFTV.NR-IDSTOCK-479BEFF,                           02740000
002750       :DCLDZBEFFTV.NR-CDSTK-479BEFF,                             02750000
002760       :DCLDZBEFFTV.NS-DBSTK-479BEFF,                             02760000
002770       :DCLDZBEFFTV.AM-CNDSTK-479BEFF,                            02770000
002780       :DCLDZBEFFTV.AM-CNSTK-479BEFF,                             02780000
002790       :DCLDZBEFFTV.CT-RKTPRDX-479BEFF,                           02790000
002800       :DCLDZBEFFTV.NR-IDISSUE-479BEFF,                           02800000
002810       :DCLDZBEFFTV.NR-CDISSUE-479BEFF,                           02810000
002820       :DCLDZBEFFTV.NX-CPCRESK-479BEFF,                           02820000
002830       :DCLDZBEFFTV.NX-CPAIDSK-479BEFF,                           02830000
002840       :DCLDZBEFFTV.NX-CPFDUSK-479BEFF,                           02840000
002850       :DCLDZBEFFTV.AM-INTERSK-479BEFF,                           02850000
002860       :DCLDZBEFFTV.CO-IDPRKSK-479BEFF,                           02860000
002870       :DCLDZBEFFTV.NS-IRMOSTK-479BEFF,                           02870000
002880       :DCLDZBEFFTV.DA-UBSECIS-479BEFF                            02880000
002890    FROM DZBEFFTV                                                 02890000
002900    WHERE                                                         02900000
002910       CT_RKTPROD_479BEFF = :DCLDZBEFFTV.CT-RKTPROD-479BEFF       02910000
002920       AND NR_IDSTOCK_479BEFF = :DCLDZBEFFTV.NR-IDSTOCK-479BEFF   02920000
002930       AND NR_CDSTK_479BEFF = :DCLDZBEFFTV.NR-CDSTK-479BEFF       02930000
002940       AND NS_DBSTK_479BEFF = :DCLDZBEFFTV.NS-DBSTK-479BEFF       02940000
002950    QUERYNO 442                                                   02950000
002960     END-EXEC                                                     02960000
002970     EVALUATE SQLCODE                                             02970000
002980       WHEN 0                                                     02980000
002990            CONTINUE                                              02990000
003000       WHEN 100                                                   03000000
003010            DISPLAY 'NO DATA FOUND FOR SELECT DZBEFFTV'           03010000
003020            PERFORM SQLERROR                                      03020000
003030       WHEN OTHER                                                 03030000
003030 MOVE 'SELECT-DZBEFFTV' TO SQL-LOCATION.                          03030000
003040            DISPLAY 'ERROR ON LRF KEYED PARENT SELECT '           03040000
003050                  'DZBEFFTV'                                      03050000
003060            PERFORM SQLERROR                                      03060000
003070     END-EVALUATE                                                 03070000
003080     .                                                            03080000
003090     INITIALIZE DCLDZEVEFTV                                       03090000
003100     PERFORM 710-OPEN-DZEVEFC1.                                   03100000
003110     PERFORM 720-FETCH-DZEVEFC1.                                  03110000
003120                                                                  03120000
003130*DB2: Parent not-found is handled by the keyed SELECT SQLCODE     03130000
003140*check.                                                           03140000
003150     IF SQLCODE = 100                                             03150000
003160        DISPLAY 'VMBEVEF NOT FOUND : '                            03160000
003170        DISPLAY 'K1=' CT-RKTPROD-479BEFF OF DCLDZBEFFTV           03170000
003180        DISPLAY 'K2=' NR-IDSTOCK-479BEFF OF DCLDZBEFFTV           03180000
003190        DISPLAY 'K3=' NR-CDSTK-479BEFF OF DCLDZBEFFTV             03190000
003200        DISPLAY 'K4=' NS-DBSTK-479BEFF OF DCLDZBEFFTV             03200000
003210        CALL USERABEN                                             03210000
003220     END-IF.                                                      03220000
003230                                                                  03230000
003240* -- ZOEK DE MUTATIE                                              03240000
003250     PERFORM UNTIL DZEVEFC1-EOC                                   03250000
003260                OR CT-RKTEVPR-479EVEF OF DCLDZEVEFTV = '0092'     03260000
003270*DB2: Expanded LRF NEXT VMBTL07-R01 WHERE ALL-VMBEVEF-BY-VMBEFF ->03270000
003280*  VMBEVEF WITHIN VMBEFF-VMBEVEF.                                 03280000
003290        PERFORM 720-FETCH-DZEVEFC1                                03290000
003300     END-PERFORM.                                                 03300000
003310     PERFORM 730-CLOSE-DZEVEFC1.                                  03310000
003320                                                                  03320000
003330     IF DZEVEFC1-EOC                                              03330000
003340        DISPLAY 'NO MORE VMBEVEF : '                              03340000
003350        DISPLAY 'K1=' CT-RKTPROD-479BEFF OF DCLDZBEFFTV           03350000
003360        DISPLAY 'K2=' NR-IDSTOCK-479BEFF OF DCLDZBEFFTV           03360000
003370        DISPLAY 'K3=' NR-CDSTK-479BEFF OF DCLDZBEFFTV             03370000
003380        DISPLAY 'K4=' NS-DBSTK-479BEFF OF DCLDZBEFFTV             03380000
003390        CALL USERABEN                                             03390000
003400     END-IF.                                                      03400000
003410                                                                  03410000
003420*----------------------------------------------------------------*03420000
003430 MOVE-MUTATIES.                                                   03430000
003440*-------------                                                    03440000
003450     INITIALIZE VMDZ510I                                          03450000
003460     REPLACING ALPHANUMERIC BY SPACES                             03460000
003470     NUMERIC BY ZEROES.                                           03470000
003480                                                                  03480000
003490     MOVE NR-IDGOOD-479EVEF OF DCLDZEVEFTV TO WS-NR-ID-GOOD.      03490000
003500                                                                  03500000
003510     MOVE NR-CI1POS-479EVEF OF DCLDZEVEFTV TO NR-CIO-FORM-AS(1:1) 03510000
003520       OF VMDZ510I.                                               03520000
003530     MOVE NR-CI26POS-479EVEF OF DCLDZEVEFTV TO NR-CIO-FORM-AS(2:5)03530000
003540       OF VMDZ510I.                                               03540000
003550     MOVE WS-DA-CREA TO DA-CREA-FORM-AS-R OF VMDZ510I.            03550000
003560     STRING DA-CR-FORM-AS-Y   OF VMDZ510I '-'                     03560000
003570        DA-CR-FORM-AS-M   OF VMDZ510I '-'                         03570000
003580        DA-CR-FORM-AS-D   OF VMDZ510I '-'                         03580000
003590            '01.01.01.000001'                                     03590000
003600        DELIMITED BY SIZE                                         03600000
003610       INTO TS-CREA-OORD      OF VMDZ510I.                        03610000
003620        MOVE WS-NR-ID  TO NR-ID-FORM-AS OF VMDZ510I.              03620000
003630        MOVE WS-CT-OPG TO CT-OPG-FORM-AS-R OF VMDZ510I.           03630000
003640        MOVE WS-CT-OPD TO CT-OPD-FORM-AS-R OF VMDZ510I.           03640000
003650                                                                  03650000
003660        MOVE NR-IDISSUE-479BEFF OF DCLDZBEFFTV TO WS-NR-ID-ISSUE  03660000
003670        MOVE NR-CDISSUE-479BEFF OF DCLDZBEFFTV TO WS-NR-CD-ISSUE  03670000
003680        MOVE WS-NR-ISSUE TO NR-ISSUIN-OORD OF VMDZ510I.           03680000
003690        MOVE AM-CNSTK-479BEFF OF DCLDZBEFFTV                      03690000
003700       TO AM-CNS-FORM-AS      OF VMDZ510I.                        03700000
003710        MOVE NR-IDSTOCK-479BEFF OF DCLDZBEFFTV TO                 03710000
003720       NR-ST-FORM-AS-R(1:12) OF VMDZ510I.                         03720000
003730        MOVE NR-CDSTK-479BEFF OF DCLDZBEFFTV TO                   03730000
003740       NR-ST-FORM-AS-R(13:1)                                      03740000
003750       OF VMDZ510I.                                               03750000
003760        MOVE NR-IDSTOCK-479BEFF OF DCLDZBEFFTV TO                 03760000
003770       NR-STIN-OORD(1:12)                                         03770000
003780       OF VMDZ510I.                                               03780000
003790        MOVE NR-CDSTK-479BEFF OF DCLDZBEFFTV TO NR-STIN-OORD(13:1)03790000
003800       OF VMDZ510I.                                               03800000
003810        MOVE SPACES TO NR-STIN-OORD(14:1) OF VMDZ510I.            03810000
003820        MOVE NS-DBSTK-479BEFF OF DCLDZBEFFTV                      03820000
003830       TO NS-DBST-OORD        OF VMDZ510I.                        03830000
003840        IF NX-CPCRESK-479BEFF OF DCLDZBEFFTV = 0                  03840000
003850           MOVE AM-CNDSTK-479BEFF OF DCLDZBEFFTV                  03850000
003860         TO AM-CND-FORM-AS      OF VMDZ510I                       03860000
003870        ELSE                                                      03870000
003880           MOVE AM-INTERSK-479BEFF OF DCLDZBEFFTV                 03880000
003890         TO AM-INTER-FORM-AS    OF VMDZ510I                       03890000
003900        END-IF.                                                   03900000
003910        MOVE CO-IDPRKSK-479BEFF OF DCLDZBEFFTV                    03910000
003920       TO NR-ID-040SECU       OF VMDZ510I.                        03920000
003930        MOVE NS-IRMOSTK-479BEFF OF DCLDZBEFFTV                    03930000
003940       TO NS-SEQ-040IRMO      OF VMDZ510I.                        03940000
003950        MOVE DA-UBSECIS-479BEFF OF DCLDZBEFFTV                    03950000
003960       TO DA-UB-FORM-AS       OF VMDZ510I.                        03960000
003970        MOVE DA-CREVTPD-479EVEF OF DCLDZEVEFTV                    03970000
003980       TO DA-COMPTABILISATION-OPER OF VMDZ510I.                   03980000
003990        MOVE DA-CREVTPD-479EVEF OF DCLDZEVEFTV                    03990000
004000       TO DA-EXEC-OORD        OF VMDZ510I.                        04000000
004010                                                                  04010000
004020        MOVE NX-CPCRESK-479BEFF OF DCLDZBEFFTV                    04020000
004030       TO NS-RANK-COUP        OF VMDZ510I.                        04030000
004040        MOVE NX-CPAIDSK-479BEFF OF DCLDZBEFFTV                    04040000
004050       TO NX-CPAID-STOCK      OF VMDZ510I.                        04050000
004060*    MOVE NX-CPFDU-STOCK      OF VMBEFF                           04060000
004070                                                                  04070000
004080* EXTRA ZONES OPVULLEN                                            04080000
004090                                                                  04090000
004100        EVALUATE WS-CT-OPD                                        04100000
004110          WHEN 00                                                 04110000
004120               MOVE 'MU' TO CO-TYPOPER-OORD OF VMDZ510I           04120000
004130          WHEN OTHER                                              04130000
004140               MOVE '??' TO CO-TYPOPER-OORD OF VMDZ510I           04140000
004150               DISPLAY 'ABEND VERKEERDE CT-OPD = '                04150000
004160               WS-CT-OPD                                          04160000
004170               DISPLAY DCLDZBEFFTV                                04170000
004180               DISPLAY DCLDZEVEFTV                                04180000
004190               CALL USERABEN                                      04190000
004200        END-EVALUATE.                                             04200000
004210* UITGIFTE = SRW DUS '1'                                          04210000
004220        MOVE '1' TO CO-ISSUIN-OORD OF VMDZ510I.                   04220000
004230        MOVE 001 TO NB-ST-OORD OF VMDZ510I.                       04230000
004240* EFFECT = IKB = DEXIA DUS '1'                                    04240000
004250        MOVE '1' TO CO-STIN-OORD OF VMDZ510I.                     04250000
004260                                                                  04260000
004270        ADD 1 TO VOLGNUMMER.                                      04270000
004280        STRING 'CIR '                                             04280000
004290           CT-OPD-FORM-AS OF VMDZ510I ' '                         04290000
004300           VOLGNUMMER                                             04300000
004310           DELIMITED BY SIZE                                      04310000
004320       INTO NR-REFORD-OORD OF VMDZ510I.                           04320000
004330                                                                  04330000
004340* EXTRA'S ANNIE STEPPE                                            04340000
004350           STRING 'X'                                             04350000
004360            '000000'                                              04360000
004370            '      '                                              04370000
004380              DELIMITED BY SIZE                                   04380000
004390       INTO NR-TRANS-OORD  OF VMDZ510I.                           04390000
004400* 10=AGENCY 11=ZETEL                                              04400000
004410*    IF NR-CIO-FORM-AS OF VMDZ510I =                              04410000
004420*       NR-CIW-FORM-AS OF VMDZ510I                                04420000
004430              MOVE '10' TO CO-TYPKAN2-OORD OF VMDZ510I            04430000
004440*    ELSE                                                         04440000
004450*      MOVE '11' TO CO-TYPKAN2-OORD OF VMDZ510I                   04450000
004460*    END-IF.                                                      04460000
004470              MOVE 'DX' TO CO-BANK-OORD OF VMDZ510I.              04470000
004480                                                                  04480000
004490              MOVE WS-OLD-CI TO NR-CIINPTR-OORD OF VMDZ510I.      04490000
004500                                                                  04500000
004510*----------------------------------------------------------------*04510000
004520 WRITE-MUTATIES.                                                  04520000
004530*--------------                                                   04530000
004540     ADD 1 TO COUNT-TREATED                                       04540000
004550     WRITE FO-MUTATIES-REC FROM VMDZ510I                          04550000
004560     .                                                            04560000
004570                                                                  04570000
004580*----------------------------------------------------------------*04580000
004590 READ-MUTATIES.                                                   04590000
004600*-------------                                                    04600000
004610     READ FI-MUTATIES INTO    WS-MUTATIES                         04610000
004620        AT END                                                    04620000
004630        SET MUTATIES-EOF TO TRUE                                  04630000
004640     NOT AT END                                                   04640000
004650        CONTINUE                                                  04650000
004660     END-READ                                                     04660000
004670     .                                                            04670000
004680                                                                  04680000
004690/---------------------------------------------------------------* 04690000
004700*    ERROR HANDLING                                               04700000
004710*---------------------------------------------------------------* 04710000
004720                                                                  04720000
004730*DB2 GENERATED CURSOR OPEN FETCH CLOSE PARAGRAPHS              *  04730000
004740                                                                  04740000
004750 710-OPEN-DZEVEFC1.                                               04750000
004760D    DISPLAY '710-OPEN-DZEVEFC1.'                                 04760000
004770     MOVE 710 TO SQL-LOCATION                                     04770000
004780                                                                  04780000
004790     EXEC SQL                                                     04790000
004800       OPEN DZEVEFC1                                              04800000
004810     END-EXEC                                                     04810000
004820                                                                  04820000
004830     EVALUATE SQLCODE                                             04830000
004840       WHEN ZERO                                                  04840000
004850            SET DZEVEFC1-NOT-EOC TO TRUE                          04850000
004860       WHEN OTHER                                                 04860000
004870            DISPLAY 'ERROR WHILE OPENING CURSOR DZEVEFC1'         04870000
004880            PERFORM SQLERROR                                      04880000
004890     END-EVALUATE                                                 04890000
004900     .                                                            04900000
004910                                                                  04910000
004920 720-FETCH-DZEVEFC1.                                              04920000
004930D    DISPLAY '720-FETCH-DZEVEFC1.'                                04930000
004940     SET DZEVEFC1-NOT-EOC TO TRUE                                 04940000
004950     MOVE 720 TO SQL-LOCATION                                     04950000
004960                                                                  04960000
004970     EXEC SQL                                                     04970000
004980       FETCH DZEVEFC1                                             04980000
004990        INTO :DCLDZEVEFTV.CT-RKTEVPR-479EVEF                      04990000
005000           , :DCLDZEVEFTV.DA-CREVTPD-479EVEF                      05000000
005010           , :DCLDZEVEFTV.NR-CI1POS-479EVEF                       05010000
005020           , :DCLDZEVEFTV.NR-CI26POS-479EVEF                      05020000
005030           , :DCLDZEVEFTV.NR-IDGOOD-479EVEF                       05030000
005040           , :DCLDZEVEFTV.NR-ID-479EVEF                           05040000
005050     END-EXEC                                                     05050000
005060                                                                  05060000
005070     EVALUATE SQLCODE                                             05070000
005080       WHEN ZERO                                                  05080000
005090            CONTINUE                                              05090000
005100       WHEN 100                                                   05100000
005110            SET DZEVEFC1-EOC TO TRUE                              05110000
005120       WHEN OTHER                                                 05120000
005130            DISPLAY 'ERROR WHILE FETCHING CURSOR DZEVEFC1'        05130000
005140            DISPLAY 'CT-RK-TPROD    = ' CT-RKTPROD-479BEFF        05140000
005150                                        OF DCLDZBEFFTV            05150000
005160            DISPLAY 'NR-ID-STOCK-R1 = ' NR-IDSTOCK-479BEFF        05160000
005170                                        OF DCLDZBEFFTV            05170000
005180            DISPLAY 'NR-CD-STOCK    = ' NR-CDSTK-479BEFF          05180000
005190                                        OF DCLDZBEFFTV            05190000
005200            DISPLAY 'NS-DB-STOCK    = ' NS-DBSTK-479BEFF          05200000
005210                                        OF DCLDZBEFFTV            05210000
005220            PERFORM SQLERROR                                      05220000
005230     END-EVALUATE                                                 05230000
005240     .                                                            05240000
005250                                                                  05250000
005260 730-CLOSE-DZEVEFC1.                                              05260000
005270D    DISPLAY '730-CLOSE-DZEVEFC1.'                                05270000
005280     MOVE 730 TO SQL-LOCATION                                     05280000
005290                                                                  05290000
005300     EXEC SQL                                                     05300000
005310       CLOSE DZEVEFC1                                             05310000
005320     END-EXEC                                                     05320000
005330                                                                  05330000
005340     EVALUATE SQLCODE                                             05340000
005350       WHEN ZERO                                                  05350000
005360            CONTINUE                                              05360000
005370       WHEN OTHER                                                 05370000
005380            DISPLAY 'ERROR WHILE CLOSING CURSOR DZEVEFC1'         05380000
005390            PERFORM SQLERROR                                      05390000
005400     END-EVALUATE                                                 05400000
005410     .                                                            05410000
005420                                                                  05420000
005430                                                                  05430000
005440 600-GET-TIMESTAMP.                                               05440000
005450D    DISPLAY '600-GET-TIMESTAMP.'                                 05450000
005460     MOVE FUNCTION CURRENT-DATE TO TS-SYSTEM.                     05460000
005470     MOVE CC OF TS-SYSTEM       TO CC OF TS-TIMESTAMP             05470000
005480     MOVE YY OF TS-SYSTEM       TO YY OF TS-TIMESTAMP             05480000
005490     MOVE MM OF TS-SYSTEM       TO MM OF TS-TIMESTAMP             05490000
005500     MOVE DD OF TS-SYSTEM       TO DD OF TS-TIMESTAMP             05500000
005510     MOVE HH OF TS-SYSTEM       TO HH OF TS-TIMESTAMP             05510000
005520     MOVE MI OF TS-SYSTEM       TO MI OF TS-TIMESTAMP             05520000
005530     MOVE SS OF TS-SYSTEM       TO SS OF TS-TIMESTAMP             05530000
005540     MOVE TT OF TS-SYSTEM       TO TT OF TS-TIMESTAMP             05540000
005550     DISPLAY 'TIMESTAMP: ' TS-TIMESTAMP                           05550000
005560     .                                                            05560000
005570                                                                  05570000
005580*SQLERROR ROUTINE.                                                05580000
005590     EXEC SQL                                                     05590000
005600          INCLUDE SQLERROR                                        05600000
005610     END-EXEC.                                                    05610000
