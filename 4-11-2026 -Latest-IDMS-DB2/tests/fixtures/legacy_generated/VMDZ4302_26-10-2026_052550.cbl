000010 CBL ARITH(EXTEND)                                                00010000
000020 IDENTIFICATION DIVISION.                                         00020000
000030*------------------------                                         00030000
000040 PROGRAM-ID. VMDZ4302.                                            00040000
000050 AUTHOR.       PYTHON-AUTOMATION-USING-AI.                        00050000
000060*-----------------------------------------------------------------00060000
000070*         OPHALEN VAN EFFEKTEN MET EVENEMENTEN DIE TERUGBETAALD ZI00070000
000080*         1 MAAND VOOR DE EINDVERVALDAG                           00080000
000090*-----------------------------------------------------------------00090000
000100* 12 NOV 1997 MODIFIED BY PETER VERBEEK                           00100000
000110*             VERWIJDEREN BAREMA DER WAARDEN                      00110000
000120*-----------------------------------------------------------------00120000
000130* 19 JAN 1998 MODIFIED BY PETER VERBEEK                           00130000
000140*             EURO AANPASSINGEN                                   00140000
000150*-----------------------------------------------------------------00150000
000160* 11 DEC 2004 MODIFIED BY NICOLAS JORIS                           00160000
000170*             ADAPTATIONS DAISY SECURITIES SUITE AUX MODIFICATIONS00170000
000180*             DE LA DB.                                           00180000
000190*             CE PROGRAMME EST UNE ADAPTATION DE VM4OM003         00190000
000200*-----------------------------------------------------------------00200000
000210* MODIFIED BY VHEML                                               00210000
000220*   2007/11 : HERCOMPILATIE P20 2767 ENGELS UITTREKSEL            00220000
000230*-----------------------------------------------------------------00230000
000240*                                                                 00240000
000250 DATE-WRITTEN. 2026-10-26.                                        00250000
000260/                                                                 00260000
000270*-----------------------------------------------------------------00270000
000280 ENVIRONMENT DIVISION.                                            00280000
000290*-----------------------------------------------------------------00290000
000300 INPUT-OUTPUT SECTION.                                            00300000
000310 FILE-CONTROL.                                                    00310000
000320     SELECT EMISSIONS-I ASSIGN TO UT-S-DD010.                     00320000
000330     SELECT EFFEKT-O    ASSIGN TO UT-S-DD005.                     00330000
000340*                                                                 00340000
000350/                                                                 00350000
000360*-----------------------------------------------------------------00360000
000370 DATA DIVISION.                                                   00370000
000380*-----------------------------------------------------------------00380000
000390 FILE SECTION.                                                    00390000
000400 FD  EMISSIONS-I                                                  00400000
000410     BLOCK CONTAINS 0 RECORDS                                     00410000
000420     RECORD CONTAINS 40 CHARACTERS                                00420000
000430     RECORDING MODE F                                             00430000
000440     LABEL RECORDS STANDARD.                                      00440000
000450 01  EMISSIONS-I-REC PIC X(40).                                   00450000
000460*                                                                 00460000
000470 FD  EFFEKT-O                                                     00470000
000480     BLOCK CONTAINS 0 RECORDS                                     00480000
000490     RECORD CONTAINS 90 CHARACTERS                                00490000
000500     RECORDING MODE F                                             00500000
000510     LABEL RECORDS STANDARD.                                      00510000
000520 01  REFFEKT-O   PIC X(90).                                       00520000
000530*                                                                 00530000
000540*                                                                 00540000
000550*-----------------------------------------------------------------00550000
000560 WORKING-STORAGE SECTION.                                         00560000
000570*-----------------------------------------------------------------00570000
000580*                                                                 00580000
000590 01  CS-VM9BC50T         PIC X(8)    VALUE 'VM9BC50T'.            00590000
000600 01  WS-VM9BC50I.                                                 00600000
000610     COPY VM9BC50I     REPLACING ==:VM9BC50T:== BY ==BC50I==.     00610000
000620 01  WS-VM9BC50O.                                                 00620000
000630     COPY VM9BC50O     REPLACING ==:VM9BC50T:== BY ==BC50O==.     00630000
000640 01  WS-VM9BC50T.                                                 00640000
000650     05  TE-INTERFACE           PIC  X(001) OCCURS 32000.         00650000
000660 01  INPUT-RECORD.                                                00660000
000670     02  I-CO-INTERNE PIC X(11).                                  00670000
000680     02  I-DA-UB.                                                 00680000
000690         03  DD           PIC 99.                                 00690000
000700         03  FILLER       PIC X.                                  00700000
000710         03  MM           PIC 99.                                 00710000
000720         03  FILLER       PIC X.                                  00720000
000730         03  CCYY         PIC 9999.                               00730000
000740     02 I-DA-UE.                                                  00740000
000750         03  DD           PIC 99.                                 00750000
000760         03  FILLER       PIC X.                                  00760000
000770         03  MM           PIC 99.                                 00770000
000780         03  FILLER       PIC X.                                  00780000
000790         03  CCYY         PIC 9999.                               00790000
000800     02 FILLER PIC X(9).                                          00800000
000810*                                                                 00810000
000820 01  VARIABLES.                                                   00820000
000830     03  WS-DA-UE-MIN-1MAAND.                                     00830000
000840         05 CCYY          PIC 9(4).                               00840000
000850         05 MM            PIC 99.                                 00850000
000860         05 DD            PIC 99.                                 00860000
000870     03  USERABEN                  PIC X(8)    VALUE 'USERABEN'.  00870000
000880     03  SW-EOF                    PIC 9       VALUE 0.           00880000
000890     03  SW-168                    PIC X       VALUE 'N'.         00890000
000900     03  LAATSTE-DA-CR-EVENT-PROD  PIC 9(8)    VALUE 0.           00900000
000910     03  HULP-NR-ID-GOOD.                                         00910000
000920         05  FILLER                PIC 9(8)    COMP-3.            00920000
000930         05  HULP-DA-UB-TRANSF     PIC 9(8)    COMP-3.            00930000
000940         05  FILLER                PIC 9(6)    COMP-3.            00940000
000950         05  CT-OPD                PIC S9(3)   COMP-3.            00950000
000960         05  FILLER                PIC 9(3)    COMP-3.            00960000
000970         05  FILLER                PIC XX.                        00970000
000980*                                                                 00980000
000990     03  LAATSTE-OPD               PIC S9(3)   COMP-3.            00990000
001000     03  LAATSTE-CI                PIC X(6)    VALUE '000000'.    01000000
001010 01  UITREC.                                                      01010000
001020     03  UIT-NR-CI            PIC  9(06).                         01020000
001030     03  UIT-AM-CN-STOCK      PIC S9(12)V9(6).                    01030000
001040     03  UIT-CO-DEVISE        PIC  X(03).                         01040000
001050     03  FILLER               PIC X(22) VALUE SPACE.              01050000
001060     03  UIT-CO-INTERNE       PIC X(11).                          01060000
001070     03  FILLER               PIC X(12) VALUE SPACE.              01070000
001080     03  UIT-NR-ID-STOCK-CD   PIC  9(13).                         01080000
001090     03  FILLER               PIC  X(05) VALUE SPACES.            01090000
001100*                                                                 01100000
001110 01  ZONE-DATONLY.                                                01110000
001120     02  WS-DA-YMD.                                               01120000
001130         03  YY          PIC 99.                                  01130000
001140         03  MM          PIC 99.                                  01140000
001150         03  DD          PIC 99.                                  01150000
001160*                                                                 01160000
001170     02  WS-DA-DMY.                                               01170000
001180         03  DD          PIC 99.                                  01180000
001190         03  MM          PIC 99.                                  01190000
001200         03  YY          PIC 99.                                  01200000
001210*                                                                 01210000
001220     02  WS-DA-CYMD-N    PIC 9(8).                                01220000
001230     02  WS-DA-CYMD REDEFINES WS-DA-CYMD-N.                       01230000
001240         03  CCYY        PIC 9999.                                01240000
001250         03  MM          PIC 99.                                  01250000
001260         03  DD          PIC 99.                                  01260000
001270*                                                                 01270000
001280     02  WS-DA-UE.                                                01280000
001290         03  CCYY        PIC 9999.                                01290000
001300         03  MM          PIC 99.                                  01300000
001310         03  DD          PIC 99.                                  01310000
001320*                                                                 01320000
001330*-----------------------------------------------------------------01330000
001340                                                                  01340000
001350     EXEC SQL INCLUDE SQLERRWS END-EXEC.                          01350000
001360     EXEC SQL INCLUDE SQLCA END-EXEC.                             01360000
001370     EXEC SQL INCLUDE DZBEFFTV END-EXEC.                          01370000
001380     EXEC SQL INCLUDE DZEVEFTV END-EXEC.                          01380000
001390     EXEC SQL INCLUDE DZWCEFTV END-EXEC.                          01390000
001400                                                                  01400000
001410 01  WS-DZBEFFC1-FLAG               PIC X.                        01410000
001420     88  DZBEFFC1-NOT-EOC           VALUE 'N'.                    01420000
001430     88  DZBEFFC1-EOC               VALUE 'Y'.                    01430000
001440                                                                  01440000
001450 01  WS-DZEVEFC1-FLAG               PIC X.                        01450000
001460     88  DZEVEFC1-NOT-EOC           VALUE 'N'.                    01460000
001470     88  DZEVEFC1-EOC               VALUE 'Y'.                    01470000
001480                                                                  01480000
001490                                                                  01490000
001500     EXEC SQL DECLARE DZBEFFC1 CURSOR FOR                         01500000
001510       SELECT CT_RKTPROD_479BEFF                                  01510000
001520            , NR_IDSTOCK_479BEFF                                  01520000
001530            , NR_CDSTK_479BEFF                                    01530000
001540            , NS_DBSTK_479BEFF                                    01540000
001550       FROM DZBEFFTV                                              01550000
001560       WHERE CO_IDISSUS_479WCEF = :DCLDZWCEFTV.CO-IDISSUS-479WCEF 01560000
001570         AND NS_IRMOS_479WCEF = :DCLDZWCEFTV.NS-IRMOS-479WCEF     01570000
001580         AND DA_UBSECIS_479WCEF = :DCLDZWCEFTV.DA-UBSECIS-479WCEF 01580000
001590       FOR READ ONLY                                              01590000
001600       QUERYNO 254                                                01600000
001610     END-EXEC                                                     01610000
001620                                                                  01620000
001630     EXEC SQL DECLARE DZEVEFC1 CURSOR FOR                         01630000
001640       SELECT CT_RKTEVPR_479EVEF                                  01640000
001650            , NR_IDGOOD_479EVEF                                   01650000
001660            , NR_ID_479EVEF                                       01660000
001670       FROM DZEVEFTV                                              01670000
001680       WHERE CT_RKTPROD_479BEFF = :DCLDZBEFFTV.CT-RKTPROD-479BEFF 01680000
001690         AND NR_IDSTOCK_479BEFF = :DCLDZBEFFTV.NR-IDSTOCK-479BEFF 01690000
001700         AND NR_CDSTK_479BEFF = :DCLDZBEFFTV.NR-CDSTK-479BEFF     01700000
001710         AND NS_DBSTK_479BEFF = :DCLDZBEFFTV.NS-DBSTK-479BEFF     01710000
001720       ORDER BY NR_ID_479EVEF DESC                                01720000
001730       FOR READ ONLY                                              01730000
001740       QUERYNO 255                                                01740000
001750     END-EXEC.                                                    01750000
001760                                                                  01760000
001770                                                                  01770000
001780 01  WS-DB2-GENERATED.                                            01780000
001790     10  CS-PROGRAM               PIC X(8)    VALUE 'VMDZ4302'.   01790000
001800                                                                  01800000
001810 01  WS-TIMESTAMP-FIELDS.                                         01810000
001820     05 TS-SYSTEM.                                                01820000
001830        10  DA-SYS.                                               01830000
001840            15  DA-SYS-CCYY.                                      01840000
001850                20  CC            PIC X(2).                       01850000
001860                20  YY            PIC X(2).                       01860000
001870            15  MM                PIC X(2).                       01870000
001880            15  DD                PIC X(2).                       01880000
001890        10  HR-SYS.                                               01890000
001900            15  HH                PIC X(2).                       01900000
001910            15  MI                PIC X(2).                       01910000
001920            15  SS                PIC X(2).                       01920000
001930            15  TT                PIC X(2).                       01930000
001940     05 TS-TIMESTAMP.                                             01940000
001950        10  CC                    PIC X(2).                       01950000
001960        10  YY                    PIC X(2).                       01960000
001970        10  TE-MARKER1            PIC X             VALUE '-'.    01970000
001980        10  MM                    PIC X(2).                       01980000
001990        10  TE-MARKER2            PIC X             VALUE '-'.    01990000
002000        10  DD                    PIC X(2).                       02000000
002010        10  TE-MARKER3            PIC X             VALUE '-'.    02010000
002020        10  HH                    PIC X(2).                       02020000
002030        10  TE-MARKER4            PIC X             VALUE '.'.    02030000
002040        10  MI                    PIC X(2).                       02040000
002050        10  TE-MARKER5            PIC X             VALUE '.'.    02050000
002060        10  SS                    PIC X(2).                       02060000
002070        10  TE-MARKER6            PIC X             VALUE '.'.    02070000
002080        10  TT                    PIC X(2).                       02080000
002090        10  NNNN                  PIC 9(04)         VALUE 0.      02090000
002100                                                                  02100000
002110 LINKAGE SECTION.                                                 02110000
002120*-----------------------------------------------------------------02120000
002130 01  PARAM-DATONLY.                                               02130000
002140     03  LS-PARAM        PIC S9(4) COMP.                          02140000
002150     03  LS-DATE-IND     PIC X.                                   02150000
002160     03  LS-DA-DMY.                                               02160000
002170         05  DD          PIC 99.                                  02170000
002180         05  MM          PIC 99.                                  02180000
002190         05  YY          PIC 99.                                  02190000
002200/                                                                 02200000
002210*-----------------------------------------------------------------02210000
002220 PROCEDURE DIVISION USING PARAM-DATONLY.                          02220000
002230*-----------------------------------------------------------------02230000
002240*                                                                 02240000
002250* BEGINVERWERKING                                                 02250000
002260*                                                                 02260000
002270     PERFORM 600-GET-TIMESTAMP.                                   02270000
002280     IF LS-DATE-IND = '0'                                         02280000
002290        ACCEPT WS-DA-YMD FROM DATE                                02290000
002300        MOVE CORR WS-DA-YMD TO WS-DA-DMY                          02300000
002310     ELSE                                                         02310000
002320        MOVE LS-DA-DMY      TO WS-DA-DMY                          02320000
002330     END-IF                                                       02330000
002340     MOVE CORR WS-DA-DMY  TO WS-DA-CYMD.                          02340000
002350     MOVE YY OF WS-DA-DMY TO CCYY OF WS-DA-CYMD.                  02350000
002360*                                                                 02360000
002370     IF CCYY OF WS-DA-CYMD LESS 80                                02370000
002380        ADD 2000 TO CCYY OF WS-DA-CYMD                            02380000
002390     ELSE                                                         02390000
002400        ADD 1900 TO CCYY OF WS-DA-CYMD                            02400000
002410     END-IF                                                       02410000
002420*                                                                 02420000
002430     MOVE CS-PROGRAM TO PROGRAM-NAME.                             02430000
002440*>                                                                02440000
002450*> DB2 NOTE: obsolete IDMS BIND/READY status guard removed.       02450000
002460*>                                                                02460000
002470*> DB2 NOTE: obsolete IDMS BIND/READY status guard removed.       02470000
002480*>                                                                02480000
002490*> DB2 NOTE: obsolete IDMS BIND/READY status guard removed.       02490000
002500*>                                                                02500000
002510*> DB2 NOTE: obsolete IDMS BIND/READY status guard removed.       02510000
002520*> DB2 NOTE: obsolete IDMS BIND/READY status guard removed.       02520000
002530*> DB2 NOTE: obsolete IDMS BIND/READY status guard removed.       02530000
002540*                                                                 02540000
002550     OPEN INPUT  EMISSIONS-I                                      02550000
002560     OUTPUT EFFEKT-O.                                             02560000
002570*                                                                 02570000
002580     READ EMISSIONS-I INTO INPUT-RECORD                           02580000
002590        AT END MOVE 1 TO SW-EOF                                   02590000
002600     END-READ.                                                    02600000
002610*                                                                 02610000
002620     PERFORM VERWERK-EMISSIONS UNTIL SW-EOF = 1.                  02620000
002630*                                                                 02630000
002640     CLOSE EMISSIONS-I                                            02640000
002650                                                                  02650000
002660 EFFEKT-O.                                                        02660000
002670*                                                                 02670000
002680     STOP RUN.                                                    02680000
002690/                                                                 02690000
002700*-----------------------------------------------------------------02700000
002710 VERWERK-EMISSIONS.                                               02710000
002720*-----------------------------------------------------------------02720000
002730     INITIALIZE DCLDZWCEFTV                                       02730000
002740     MOVE CORR I-DA-UE TO WS-DA-UE.                               02740000
002750*                                                                 02750000
002760     PERFORM CALL-VM9BC50T                                        02760000
002770     MOVE BC50O-NR-ID-SECU    TO CO-IDISSUS-479WCEF OF DCLDZWCEFTV02770000
002780     MOVE BC50O-NS-SEQ-IRMO   TO NS-IRMOS-479WCEF OF DCLDZWCEFTV  02780000
002790     MOVE ZEROES              TO DA-CCYYMMDD                      02790000
002800     MOVE BC50O-DA-UBSEC-ISSU TO DA-CCYYMMDD                      02800000
002810     IF DA-CCYYMMDD = ZERO OR DA-CCYYMMDD = SPACES                02810000
002820        MOVE 00010101 TO DA-CCYYMMDD                              02820000
002830     END-IF                                                       02830000
002840     MOVE CORR DA-CCYYMMDD-R TO DA-DD-MM-CCYY                     02840000
002850     MOVE DA-DD-MM-CCYY      TO DA-UBSECIS-479WCEF OF DCLDZWCEFTV 02850000
002860*                                                                 02860000
002870*VMBWCEF.                                                         02870000
002880     MOVE 'SELECT-VMBWCEF' TO SQL-LOCATION                        02880000
002890     EXEC SQL                                                     02890000
002900    SELECT                                                        02900000
002910       CO_IDISSUS_479WCEF                                         02910000
002920    INTO                                                          02920000
002930       :DCLDZWCEFTV.CO-IDISSUS-479WCEF                            02930000
002940    FROM DZWCEFTV                                                 02940000
002950    WHERE                                                         02950000
002960       CO_IDISSUS_479WCEF = :DCLDZWCEFTV.CO-IDISSUS-479WCEF       02960000
002970       AND NS_IRMOS_479WCEF = :DCLDZWCEFTV.NS-IRMOS-479WCEF       02970000
002980       AND DA_UBSECIS_479WCEF = :DCLDZWCEFTV.DA-UBSECIS-479WCEF   02980000
002990    QUERYNO 442                                                   02990000
003000     END-EXEC                                                     03000000
003010*                                                                 03010000
003020     IF SQLCODE NOT = 0                                           03020000
003030        DISPLAY 'VMBWCEF    ' DCLDZWCEFTV                         03030000
003040        DISPLAY 'SQLCODE ' SQLCODE                                03040000
003050        DISPLAY ' '                                               03050000
003060     END-IF                                                       03060000
003070     IF SQLCODE = 0                                               03070000
003080        INITIALIZE DCLDZBEFFTV                                    03080000
003090        PERFORM 2100-OPEN-DZBEFFC1                                03090000
003100        PERFORM 2200-FETCH-DZBEFFC1                               03100000
003110     END-IF                                                       03110000
003120*                                                                 03120000
003130*                                                                 03130000
003140     PERFORM VERWERK-EFFEKT UNTIL DZBEFFC1-EOC.                   03140000
003150     PERFORM 2300-CLOSE-DZBEFFC1.                                 03150000
003160*                                                                 03160000
003170     READ EMISSIONS-I INTO INPUT-RECORD                           03170000
003180        AT END MOVE 1 TO SW-EOF                                   03180000
003190     END-READ.                                                    03190000
003200/                                                                 03200000
003210*-----------------------------------------------------------------03210000
003220 VERWERK-EFFEKT.                                                  03220000
003230*-----------------------------------------------------------------03230000
003240     MOVE 0        TO LAATSTE-DA-CR-EVENT-PROD.                   03240000
003250     MOVE 0        TO LAATSTE-OPD.                                03250000
003260     MOVE '000000' TO LAATSTE-CI.                                 03260000
003270     MOVE 0        TO SW-168                                      03270000
003280     INITIALIZE DCLDZEVEFTV                                       03280000
003290     PERFORM 3100-OPEN-DZEVEFC1.                                  03290000
003300     PERFORM 3200-FETCH-DZEVEFC1.                                 03300000
003310*                                                                 03310000
003320     PERFORM NEXT-VMBEVEF UNTIL DZEVEFC1-EOC.                     03320000
003330     PERFORM 3300-CLOSE-DZEVEFC1.                                 03330000
003340     IF SW-168 = 1                                                03340000
003350        MOVE LAATSTE-CI         TO UIT-NR-CI                      03350000
003360        MOVE AM-CN-STOCK        TO UIT-AM-CN-STOCK                03360000
003370        MOVE I-CO-INTERNE       TO UIT-CO-INTERNE                 03370000
003380        MOVE NR-ID-STOCK-CD     TO UIT-NR-ID-STOCK-CD             03380000
003390        MOVE BC50O-CO-CURR-SECU TO UIT-CO-DEVISE.                 03390000
003400        MOVE BC50O-CO-CURR-SECU TO WRITE.                         03400000
003410        MOVE BC50O-CO-CURR-SECU TO REFFEKT-O.                     03410000
003420        MOVE BC50O-CO-CURR-SECU TO FROM.                          03420000
003430        MOVE BC50O-CO-CURR-SECU TO UITREC.                        03430000
003440     END-IF.                                                      03440000
003450     PERFORM 2200-FETCH-DZBEFFC1.                                 03450000
003460*                                                                 03460000
003470*-----------------------------------------------------------------03470000
003480 NEXT-VMBEVEF.                                                    03480000
003490*-----------------------------------------------------------------03490000
003500     MOVE NR-IDGOOD-479EVEF OF DCLDZEVEFTV TO HULP-NR-ID-GOOD     03500000
003510     IF CT-RKTEVPR-479EVEF OF DCLDZEVEFTV = '0168' AND            03510000
003520        CT-OPD = 91 AND DA-CR-EVENT-PROD < WS-DA-CYMD             03520000
003530                                                                  03530000
003540        MOVE WS-DA-UE TO WS-DA-UE-MIN-1MAAND                      03540000
003550        IF MM OF WS-DA-UE-MIN-1MAAND < 2                          03550000
003560           MOVE 12 TO MM OF WS-DA-UE-MIN-1MAAND                   03560000
003570           SUBTRACT 1 FROM CCYY OF WS-DA-UE-MIN-1MAAND            03570000
003580        ELSE                                                      03580000
003590           SUBTRACT 1 FROM MM   OF WS-DA-UE-MIN-1MAAND            03590000
003600        END-IF                                                    03600000
003610                                                                  03610000
003620        IF WS-DA-UE-MIN-1MAAND NOT > DA-CR-EVENT-PROD             03620000
003630           MOVE 1 TO SW-168                                       03630000
003640        END-IF                                                    03640000
003650     END-IF.                                                      03650000
003660*                                                                 03660000
003670     IF CT-RKTEVPR-479EVEF OF DCLDZEVEFTV = '0060' AND            03670000
003680        DA-CR-EVENT-PROD NOT < WS-DA-CYMD                         03680000
003690        CONTINUE                                                  03690000
003700     ELSE                                                         03700000
003710        IF CT-RKTEVPR-479EVEF OF DCLDZEVEFTV   = '0060' AND       03710000
003720           LAATSTE-DA-CR-EVENT-PROD = 0                           03720000
003730           MOVE 1      TO LAATSTE-DA-CR-EVENT-PROD                03730000
003740           MOVE NR-CI  TO LAATSTE-CI                              03740000
003750           MOVE CT-OPD TO LAATSTE-OPD                             03750000
003760        ELSE                                                      03760000
003770           IF CT-RKTEVPR-479EVEF OF DCLDZEVEFTV = '0092' AND      03770000
003780              HULP-DA-UB-TRANSF > LAATSTE-DA-CR-EVENT-PROD AND    03780000
003790              HULP-DA-UB-TRANSF < WS-DA-CYMD-N                    03790000
003800              MOVE HULP-DA-UB-TRANSF TO LAATSTE-DA-CR-EVENT-PROD  03800000
003810              MOVE NR-CI             TO LAATSTE-CI                03810000
003820           END-IF                                                 03820000
003830        END-IF                                                    03830000
003840     END-IF                                                       03840000
003850*                                                                 03850000
003860     PERFORM 3200-FETCH-DZEVEFC1.                                 03860000
003870*-----------------------------------------------------------------03870000
003880 CALL-VM9BC50T.                                                   03880000
003890*-----------------------------------------------------------------03890000
003900     INITIALIZE WS-VM9BC50I.                                      03900000
003910     INITIALIZE WS-VM9BC50O.                                      03910000
003920     MOVE 'VMDZ4302'   TO BC50I-NM-CALLER                         03920000
003930     MOVE 'VM9BC50T'   TO BC50I-NM-BB                             03930000
003940     MOVE 'P'          TO BC50I-CO-TRANSMISSION                   03940000
003950     MOVE 'QUERY001'   TO BC50I-NM-FUNCTION                       03950000
003960     MOVE '2'          TO BC50I-CO-CLE                            03960000
003970     MOVE I-CO-INTERNE TO BC50I-NR-CLE-NO-INTERNE                 03970000
003980     MOVE 'Y'          TO BC50I-CO-DONNEES-FIXES.                 03980000
003990     MOVE 'Y'          TO BC50I-CO-CONDITIONS-EMISSION.           03990000
004000     MOVE 'Y'          TO BC50I-CO-CONDITIONS-VENTE.              04000000
004010     MOVE WS-DA-CYMD   TO BC50I-DA-DEMANDE.                       04010000
004020     MOVE WS-VM9BC50I  TO WS-VM9BC50T.                            04020000
004030     CALL CS-VM9BC50T USING WS-VM9BC50T.                          04030000
004040     MOVE WS-VM9BC50T TO WS-VM9BC50O.                             04040000
004050                                                                  04050000
004060                                                                  04060000
004070 2100-OPEN-DZBEFFC1.                                              04070000
004080D    DISPLAY '2100-OPEN-DZBEFFC1.'                                04080000
004090     MOVE 2100 TO SQL-LOCATION                                    04090000
004100                                                                  04100000
004110     EXEC SQL                                                     04110000
004120       OPEN DZBEFFC1                                              04120000
004130     END-EXEC                                                     04130000
004140                                                                  04140000
004150     EVALUATE SQLCODE                                             04150000
004160       WHEN ZERO                                                  04160000
004170            SET DZBEFFC1-NOT-EOC TO TRUE                          04170000
004180       WHEN OTHER                                                 04180000
004190            DISPLAY 'ERROR WHILE OPENING CURSOR DZBEFFC1'         04190000
004200            PERFORM SQLERROR                                      04200000
004210     END-EVALUATE                                                 04210000
004220     .                                                            04220000
004230                                                                  04230000
004240 2200-FETCH-DZBEFFC1.                                             04240000
004250D    DISPLAY '2200-FETCH-DZBEFFC1.'                               04250000
004260     SET DZBEFFC1-NOT-EOC TO TRUE                                 04260000
004270     MOVE 2200 TO SQL-LOCATION                                    04270000
004280                                                                  04280000
004290     EXEC SQL                                                     04290000
004300       FETCH DZBEFFC1                                             04300000
004310        INTO :DCLDZBEFFTV.CT-RKTPROD-479BEFF                      04310000
004320           , :DCLDZBEFFTV.NR-IDSTOCK-479BEFF                      04320000
004330           , :DCLDZBEFFTV.NR-CDSTK-479BEFF                        04330000
004340           , :DCLDZBEFFTV.NS-DBSTK-479BEFF                        04340000
004350     END-EXEC                                                     04350000
004360                                                                  04360000
004370     EVALUATE SQLCODE                                             04370000
004380       WHEN ZERO                                                  04380000
004390            CONTINUE                                              04390000
004400       WHEN 100                                                   04400000
004410            SET DZBEFFC1-EOC TO TRUE                              04410000
004420       WHEN OTHER                                                 04420000
004430            DISPLAY 'ERROR WHILE FETCHING CURSOR DZBEFFC1'        04430000
004440            DISPLAY 'CO-IDPRKB-STOCK  = ' CO-IDISSUS-479WCEF      04440000
004450                                          OF DCLDZWCEFTV          04450000
004460            DISPLAY 'NS-IRMO-STOCK    = ' NS-IRMOS-479WCEF        04460000
004470                                          OF DCLDZWCEFTV          04470000
004480            DISPLAY 'DA-UBSECIS-STOCK = ' DA-UBSECIS-479WCEF      04480000
004490                                          OF DCLDZWCEFTV          04490000
004500            PERFORM SQLERROR                                      04500000
004510     END-EVALUATE                                                 04510000
004520     .                                                            04520000
004530                                                                  04530000
004540 2300-CLOSE-DZBEFFC1.                                             04540000
004550D    DISPLAY '2300-CLOSE-DZBEFFC1.'                               04550000
004560     MOVE 2300 TO SQL-LOCATION                                    04560000
004570                                                                  04570000
004580     EXEC SQL                                                     04580000
004590       CLOSE DZBEFFC1                                             04590000
004600     END-EXEC                                                     04600000
004610                                                                  04610000
004620     EVALUATE SQLCODE                                             04620000
004630       WHEN ZERO                                                  04630000
004640            CONTINUE                                              04640000
004650       WHEN OTHER                                                 04650000
004660            DISPLAY 'ERROR WHILE CLOSING CURSOR DZBEFFC1'         04660000
004670            PERFORM SQLERROR                                      04670000
004680     END-EVALUATE                                                 04680000
004690     .                                                            04690000
004700                                                                  04700000
004710 3100-OPEN-DZEVEFC1.                                              04710000
004720D    DISPLAY '3100-OPEN-DZEVEFC1.'                                04720000
004730     MOVE 3100 TO SQL-LOCATION                                    04730000
004740                                                                  04740000
004750     EXEC SQL                                                     04750000
004760       OPEN DZEVEFC1                                              04760000
004770     END-EXEC                                                     04770000
004780                                                                  04780000
004790     EVALUATE SQLCODE                                             04790000
004800       WHEN ZERO                                                  04800000
004810            SET DZEVEFC1-NOT-EOC TO TRUE                          04810000
004820       WHEN OTHER                                                 04820000
004830            DISPLAY 'ERROR WHILE OPENING CURSOR DZEVEFC1'         04830000
004840            PERFORM SQLERROR                                      04840000
004850     END-EVALUATE                                                 04850000
004860     .                                                            04860000
004870                                                                  04870000
004880 3200-FETCH-DZEVEFC1.                                             04880000
004890D    DISPLAY '3200-FETCH-DZEVEFC1.'                               04890000
004900     SET DZEVEFC1-NOT-EOC TO TRUE                                 04900000
004910     MOVE 3200 TO SQL-LOCATION                                    04910000
004920                                                                  04920000
004930     EXEC SQL                                                     04930000
004940       FETCH DZEVEFC1                                             04940000
004950        INTO :DCLDZEVEFTV.CT-RKTEVPR-479EVEF                      04950000
004960           , :DCLDZEVEFTV.NR-IDGOOD-479EVEF                       04960000
004970           , :DCLDZEVEFTV.NR-ID-479EVEF                           04970000
004980     END-EXEC                                                     04980000
004990                                                                  04990000
005000     EVALUATE SQLCODE                                             05000000
005010       WHEN ZERO                                                  05010000
005020            CONTINUE                                              05020000
005030       WHEN 100                                                   05030000
005040            SET DZEVEFC1-EOC TO TRUE                              05040000
005050       WHEN OTHER                                                 05050000
005060            DISPLAY 'ERROR WHILE FETCHING CURSOR DZEVEFC1'        05060000
005070            DISPLAY 'CT-RK-TPROD    = ' CT-RKTPROD-479BEFF        05070000
005080                                        OF DCLDZBEFFTV            05080000
005090            DISPLAY 'NR-ID-STOCK-R1 = ' NR-IDSTOCK-479BEFF        05090000
005100                                        OF DCLDZBEFFTV            05100000
005110            DISPLAY 'NR-CD-STOCK    = ' NR-CDSTK-479BEFF          05110000
005120                                        OF DCLDZBEFFTV            05120000
005130            DISPLAY 'NS-DB-STOCK    = ' NS-DBSTK-479BEFF          05130000
005140                                        OF DCLDZBEFFTV            05140000
005150            PERFORM SQLERROR                                      05150000
005160     END-EVALUATE                                                 05160000
005170     .                                                            05170000
005180                                                                  05180000
005190 3300-CLOSE-DZEVEFC1.                                             05190000
005200D    DISPLAY '3300-CLOSE-DZEVEFC1.'                               05200000
005210     MOVE 3300 TO SQL-LOCATION                                    05210000
005220                                                                  05220000
005230     EXEC SQL                                                     05230000
005240       CLOSE DZEVEFC1                                             05240000
005250     END-EXEC                                                     05250000
005260                                                                  05260000
005270     EVALUATE SQLCODE                                             05270000
005280       WHEN ZERO                                                  05280000
005290            CONTINUE                                              05290000
005300       WHEN OTHER                                                 05300000
005310            DISPLAY 'ERROR WHILE CLOSING CURSOR DZEVEFC1'         05310000
005320            PERFORM SQLERROR                                      05320000
005330     END-EVALUATE                                                 05330000
005340     .                                                            05340000
005350                                                                  05350000
005360                                                                  05360000
005370 600-GET-TIMESTAMP.                                               05370000
005380D    DISPLAY '600-GET-TIMESTAMP.'                                 05380000
005390     MOVE FUNCTION CURRENT-DATE TO TS-SYSTEM.                     05390000
005400     MOVE CC OF TS-SYSTEM       TO CC OF TS-TIMESTAMP             05400000
005410     MOVE YY OF TS-SYSTEM       TO YY OF TS-TIMESTAMP             05410000
005420     MOVE MM OF TS-SYSTEM       TO MM OF TS-TIMESTAMP             05420000
005430     MOVE DD OF TS-SYSTEM       TO DD OF TS-TIMESTAMP             05430000
005440     MOVE HH OF TS-SYSTEM       TO HH OF TS-TIMESTAMP             05440000
005450     MOVE MI OF TS-SYSTEM       TO MI OF TS-TIMESTAMP             05450000
005460     MOVE SS OF TS-SYSTEM       TO SS OF TS-TIMESTAMP             05460000
005470     MOVE TT OF TS-SYSTEM       TO TT OF TS-TIMESTAMP             05470000
005480     DISPLAY 'TIMESTAMP: ' TS-TIMESTAMP                           05480000
005490     .                                                            05490000
005500                                                                  05500000
005510*SQLERROR ROUTINE.                                                05510000
005520     EXEC SQL                                                     05520000
005530          INCLUDE SQLERROR                                        05530000
005540     END-EXEC.                                                    05540000
